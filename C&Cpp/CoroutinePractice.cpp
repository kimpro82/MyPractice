#include <iostream>
#include <coroutine>
#include <generator>
#include <ranges>
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
            coroutine.promise().completion.set_value();
        }).detach();
    }

    void await_resume() const noexcept {}
};

Task boil_water() {
    co_await BoilWaterAwaitable{95};
}

// 2. Lazy Data Stream using C++23 std::generator & std::expected
std::generator<std::expected<int, BrewingError>> infinite_espresso_stream() {
    int cup_id = 1;
    while (true) {
        // Simulate minor kitchen hazards based on cup ID
        if (cup_id == 4) {
            co_yield std::unexpected(BrewingError::GrinderOnFire);
            co_return;
        }
        if (cup_id == 7) {
            co_yield std::unexpected(BrewingError::OutOfBeans);
            co_return;
        }

        // std::generator is synchronous, so wait for the separate task coroutine.
        boil_water().get();

        std::cout << "[Barista] Pouring Espresso Cup #" << cup_id << "\n";
        co_yield cup_id++;
    }
}

// 4. Main Pipeline Execution (Combining Ranges & Monadic Error Handling)
int main() {
    std::cout << "=== [PROJECT CAFFEINE-FLOW] INITIALIZING PIPELINE ===\n\n";

    // Obtain the lazy generator stream
    auto stream = infinite_espresso_stream();

    // Apply C++20 std::ranges to safely take only the first 10 items from the stream
    auto processed_stream = std::views::take(std::move(stream), 10);

    for (auto&& result : processed_stream) {
        // Monadic error management on std::expected
        if (!result.has_value()) {
            switch (result.error()) {
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
            break; // Terminate pipeline safely without exceptions
        }

        std::cout << "[Success] Consumed Espresso Unit: " << *result << "\n\n";
    }

    std::cout << "=== [PROJECT CAFFEINE-FLOW] SHUTTING DOWN SAFELY ===\n";
    return 0;
}
