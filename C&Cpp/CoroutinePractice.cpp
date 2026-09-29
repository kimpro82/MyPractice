#include <iostream>
#include <iomanip>
#include <coroutine>
#include <expected>
#include <thread>
#include <chrono>
#include <exception>
#include <future>
#include <syncstream>
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
    std::chrono::milliseconds delay;

    bool await_ready() const noexcept { return false; }

    void await_suspend(std::coroutine_handle<Task::promise_type> coroutine) const {
        std::thread([coroutine, temp = target_temp, wait = delay]() {
            std::this_thread::sleep_for(wait);
            std::osyncstream(std::cout)
                << "[Hardware] Water successfully boiled to " << temp << "°C!\n";
            coroutine.resume();
            if (coroutine.done()) {
                coroutine.promise().completion.set_value();
            }
        }).detach();
    }

    void await_resume() const noexcept {}
};

constexpr auto brew_delay = std::chrono::seconds{1};

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

void report_successful_cup(int cup_id) {
    std::osyncstream output(std::cout);
    output << "[Barista] Pouring Espresso Cup #" << cup_id << "\n";
    output << "[Success] Consumed Espresso Unit: " << cup_id << "\n\n";
}

void brew_cup_synchronously(int cup_id) {
    auto result = espresso_order(cup_id);
    if (!result) {
        report_error(result.error());
        return;
    }

    std::this_thread::sleep_for(brew_delay);
    std::cout << "[Hardware] Water successfully boiled to 95°C!\n";
    report_successful_cup(*result);
}

Task brew_cup_asynchronously(int cup_id) {
    co_await BoilWaterAwaitable{95, brew_delay};
    report_successful_cup(cup_id);
}

int main() {
    std::cout << "=== [PROJECT CAFFEINE-FLOW] INITIALIZING PIPELINE ===\n\n";

    constexpr int cup_count = 3;
    const auto sync_start = std::chrono::steady_clock::now();
    for (int cup_id = 1; cup_id <= cup_count; ++cup_id) {
        brew_cup_synchronously(cup_id);
    }
    const auto sync_elapsed = std::chrono::duration<double>(
        std::chrono::steady_clock::now() - sync_start).count();
    std::cout << "[Synchronous] " << cup_count << " cups completed in "
              << std::fixed << std::setprecision(2) << sync_elapsed << " seconds.\n\n";

    const auto async_start = std::chrono::steady_clock::now();
    auto cup1 = brew_cup_asynchronously(1);
    auto cup2 = brew_cup_asynchronously(2);
    auto cup3 = brew_cup_asynchronously(3);
    cup1.get();
    cup2.get();
    cup3.get();
    const auto async_elapsed = std::chrono::duration<double>(
        std::chrono::steady_clock::now() - async_start).count();
    std::cout << "[Asynchronous] " << cup_count << " cups completed in "
              << std::fixed << std::setprecision(2) << async_elapsed << " seconds.\n";

    std::cout << "=== [PROJECT CAFFEINE-FLOW] SHUTTING DOWN SAFELY ===\n";
    return 0;
}
