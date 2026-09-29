#include <iostream>
#include <coroutine>
#include <generator>
#include <ranges>
#include <expected>
#include <thread>
#include <chrono>
#include <utility>

// 1. Monadic Error Definition for Barista Operations
enum class BrewingError {
    OutOfBeans,
    GrinderOnFire,
    ExistentialCrisis
};

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

        // std::generator is a synchronous range and does not support co_await.
        std::this_thread::sleep_for(std::chrono::milliseconds(150));
        std::cout << "[Hardware] Water successfully boiled to 95°C!\n";

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
