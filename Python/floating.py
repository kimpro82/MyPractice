"""Compare the memory usage and execution speed of numeric data types.

This module creates equally sized datasets using Python ``float``,
``decimal.Decimal``, NumPy ``float32``, and NumPy ``float64`` values. The
datasets are prepared during initialization so that dataset construction is
excluded from the measurements.

The benchmark measures two characteristics:

* Total memory usage, including nested objects and container overhead, through
    :func:`pympler.asizeof.asizeof`.
* The time required to multiply every value by ``1.05``. Python lists use
    list comprehensions, while NumPy arrays use vectorized multiplication.
* The cost of crossing the Python/NumPy boundary. Additional measurements
    compare direct NumPy operations with cases that convert a list to an array
    or an array result back to a list for every timed operation.

Use :class:`DataBenchmarkSuite` to collect individual measurements or call
its :meth:`DataBenchmarkSuite.run_report` method to print a formatted summary.

Example:
        benchmark = DataBenchmarkSuite(data_size=10_000)
        benchmark.run_report()

Date: 2026-08-27
Author: kimpro82
"""

import timeit
import sys
from decimal import Decimal
from typing import Callable, Dict, List, Any
import numpy as np
from pympler import asizeof

class DataBenchmarkSuite:
    """Benchmark memory usage and operation performance for floating-point data types."""
    
    def __init__(self, data_size: int = 10_000):
        self.data_size = data_size
        self._datasets = self._initialize_datasets()

    def _initialize_datasets(self) -> Dict[str, Any]:
        """Create datasets for comparison, excluding constructor overhead from measurements."""
        return {
            "Python float": [float(i) for i in range(self.data_size)],
            "Decimal": [Decimal(str(i)) for i in range(self.data_size)],
            "NumPy float32": np.arange(self.data_size, dtype=np.float32),
            "NumPy float64": np.arange(self.data_size, dtype=np.float64),
        }

    def measure_memory(self) -> Dict[str, int]:
        """Measure the actual total memory usage of each data structure in bytes."""
        memory_results = {}
        for name, data in self._datasets.items():
            # Recursively measure contained objects and overhead with pympler.
            memory_results[name] = asizeof.asizeof(data)
        return memory_results

    def measure_execution_time(self, number: int = 1_000) -> Dict[str, float]:
        """Measure operation speed for each data type using optimized operations."""
        timings = {}
        
        # 1. Python float (list comprehension)
        stmt_float = "[v * 1.05 for v in self._datasets['Python float']]"
        timings["Python float"] = timeit.timeit(stmt=stmt_float, globals={'self': self}, number=number)

        # 2. Decimal (list comprehension)
        stmt_dec = "[v * Decimal('1.05') for v in self._datasets['Decimal']]"
        timings["Decimal"] = timeit.timeit(
            stmt=stmt_dec,
            globals={'self': self, 'Decimal': Decimal},
            number=number,
        )

        # 3. NumPy float32 (vectorized operation)
        stmt_np32 = "self._datasets['NumPy float32'] * 1.05"
        timings["NumPy float32"] = timeit.timeit(stmt=stmt_np32, globals={'self': self}, number=number)

        # 4. NumPy float64 (vectorized operation)
        stmt_np64 = "self._datasets['NumPy float64'] * 1.05"
        timings["NumPy float64"] = timeit.timeit(stmt=stmt_np64, globals={'self': self}, number=number)

        return timings

    def measure_conversion_overhead(self, number: int = 1_000) -> Dict[str, float]:
        """Measure the cost of converting between Python lists and NumPy arrays."""
        python_values = self._datasets["Python float"]
        numpy_values = self._datasets["NumPy float64"]
        conversion_timings = {}

        statements = {
            "NumPy direct operation": "numpy_values * 1.05",
            "Python list operation": "[value * 1.05 for value in python_values]",
            "List to NumPy each time": "np.asarray(python_values) * 1.05",
            "NumPy to list each time": "(numpy_values * 1.05).tolist()",
            "List-NumPy round trip": "(np.asarray(python_values) * 1.05).tolist()",
        }
        benchmark_globals = {
            "np": np,
            "numpy_values": numpy_values,
            "python_values": python_values,
        }

        for name, statement in statements.items():
            conversion_timings[name] = timeit.timeit(
                stmt=statement,
                globals=benchmark_globals,
                number=number,
            )

        return conversion_timings

    def run_report(self) -> None:
        """Format the results and print a readable report."""
        print(f"=== [Benchmark Report] Data Size: {self.data_size:,} elements ===\n")
        
        memory_data = self.measure_memory()
        time_data = self.measure_execution_time()

        print(f"{'Data Type':<18} | {'Memory (Bytes)':<15} | {'Execution Time (s)':<18}")
        print("-" * 58)
        
        for name in memory_data.keys():
            mem = memory_data[name]
            sec = time_data[name]
            print(f"{name:<18} | {mem:>15,d} | {sec:>18.5f}")

        print("\n=== [Python/NumPy Conversion Overhead] ===\n")
        conversion_data = self.measure_conversion_overhead()
        print(f"{'Operation':<28} | {'Execution Time (s)':<18}")
        print("-" * 50)
        for name, seconds in conversion_data.items():
            print(f"{name:<28} | {seconds:>18.5f}")


if __name__ == "__main__":
    benchmark = DataBenchmarkSuite(data_size=10_000)
    benchmark.run_report()
