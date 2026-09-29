#include <iostream>
#include <coroutine>
#include <generator>
#include <ranges>
#include <expected>
#include <concepts>
#include <thread>
#include <chrono>

// 1. Monadic Error Definition for Barista Operations
enum class BrewingError {
    OutOfBeans,
    GrinderOnFire,
    ExistentialCrisis
};

// C++20 Concept for Type-Safe Custom Awaitables
template<typename T>
concept Awaitable = requires(T t, std::coroutine_handle<> h) {
    { t.await_ready() } -> std::convertible_to<bool>;
    { t.await_suspend(h) };
    { t.await_resume() };
};

// 2. Custom Awaitable for Async Water Boiling (co_await)
struct BoilWaterAwaitable {
    int target_temp;

    bool await_ready() const noexcept { return false; }

    void await_suspend(std::coroutine_handle<> h) const {
        // Simulate non-blocking hardware latency in a background thread
        std::thread([h, temp = target_temp]() {
            std::this_thread::sleep_for(std::chrono::milliseconds(150));
            std::cout << "[Hardware] Water successfully boiled to " << temp << "°C!\n";
            h.resume(); // Resume coroutine execution
        }).detach();
    }

    void await_resume() const noexcept {}
};

// Concept-constrained helper wrapper
template <Awaitable A>
auto perform_async_action(A&& awaitable) {
    return std::forward<A>(awaitable);
}

// 3. Lazy Infinite Data Stream using C++23 std::generator & std::expected
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

        // Non-blocking wait using our concept-constrained awaitable
        co_await perform_async_action(BoilWaterAwaitable{95});

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
    auto processed_stream = stream | std::views::take(10);

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
