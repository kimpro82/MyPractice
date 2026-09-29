#include <iostream>
#include <coroutine>
#include <expected>
#include <thread>
#include <chrono>
#include <exception>
#include <future>
#include <utility>

// 1. Monadic Error Definition for Barista Operations
enum class BrewingError {
    OutOfBeans,
    GrinderOnFire,
    ExistentialCrisis
};

// A task coroutine that can suspend while awaiting asynchronous work.
struct Task {
    struct promise_type;
    using handle_type = std::coroutine_handle<promise_type>;

    struct promise_type {
        std::promise<void> completion;
        std::exception_ptr exception;

        Task get_return_object() {
            return Task{handle_type::from_promise(*this)};
        }
        std::suspend_never initial_suspend() noexcept { return {}; }
        std::suspend_always final_suspend() noexcept { return {}; }
        void return_void() noexcept {}
        void unhandled_exception() noexcept {
            exception = std::current_exception();
        }
    };

    explicit Task(handle_type coroutine)
        : coroutine_(coroutine), completion_(coroutine_.promise().completion.get_future()) {}
    Task(const Task&) = delete;
    Task& operator=(const Task&) = delete;
    Task(Task&& other) noexcept
        : coroutine_(std::exchange(other.coroutine_, {})),
          completion_(std::move(other.completion_)) {}
    ~Task() {
        if (coroutine_) {
            coroutine_.destroy();
        }
    }

    void get() {
        completion_.get();
        if (coroutine_.promise().exception) {
            std::rethrow_exception(coroutine_.promise().exception);
        }
    }

private:
    handle_type coroutine_;
    std::future<void> completion_;
};

struct BoilWaterAwaitable {
    int target_temp;

    bool await_ready() const noexcept { return false; }

    void await_suspend(std::coroutine_handle<Task::promise_type> coroutine) const {
        std::thread([coroutine, temp = target_temp]() {
            std::this_thread::sleep_for(std::chrono::milliseconds(150));
            std::cout << "[Hardware] Water successfully boiled to " << temp << "°C!\n";
            coroutine.resume();
            if (coroutine.done()) {
                coroutine.promise().completion.set_value();
            }
        }).detach();
    }

    void await_resume() const noexcept {}
};

Task boil_water() {
    co_await BoilWaterAwaitable{95};
}

std::expected<int, BrewingError> espresso_order(int cup_id) {
    if (cup_id == 4) {
        return std::unexpected(BrewingError::GrinderOnFire);
    }
    if (cup_id == 7) {
        return std::unexpected(BrewingError::OutOfBeans);
    }
    return cup_id;
}

void report_error(BrewingError error) {
    switch (error) {
        case BrewingError::GrinderOnFire:
            std::cout << "\n[CRITICAL ERROR] Grinder on fire! Evacuating the office.\n";
            break;
        case BrewingError::OutOfBeans:
            std::cout << "\n[WARNING] Out of coffee beans! Emergency restocking needed.\n";
            break;
        case BrewingError::ExistentialCrisis:
            std::cout << "\n[INFO] Developer paused to stare into the void.\n";
            break;
        }
}

Task run_brewing_pipeline() {
    for (int cup_id = 1;; ++cup_id) {
        auto result = espresso_order(cup_id);
        if (!result) {
            report_error(result.error());
            co_return;
        }

        co_await BoilWaterAwaitable{95};

        std::cout << "[Barista] Pouring Espresso Cup #" << *result << "\n";
        std::cout << "[Success] Consumed Espresso Unit: " << *result << "\n\n";
    }
}

int main() {
    std::cout << "=== [PROJECT CAFFEINE-FLOW] INITIALIZING PIPELINE ===\n\n";

    auto pipeline = run_brewing_pipeline();
    std::cout << "[Main] Brewing runs asynchronously; main can continue working.\n";
    pipeline.get();

    std::cout << "=== [PROJECT CAFFEINE-FLOW] SHUTTING DOWN SAFELY ===\n";
    return 0;
}
