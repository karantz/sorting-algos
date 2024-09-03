import time
import timeit
import psutil
import random
import platform
import matplotlib.pyplot as plt
from bubblesort import bubblesort
from insertionsort import insertionsort
from selectionsort import selectionsort

def benchmark_sorting_algorithm(sort_func, arr):
    return timeit.timeit(lambda: sort_func(arr.copy()), number=1)

# Benchmarking setup
input_sizes = [5, 10, 20, 100,200,500,1000]
bubble_times = []
insertion_times = []
selection_times = []

# Run benchmarks
for size in input_sizes:
    arr = [random.randint(0, 10000,) for _ in range(size)]
    
    bubble_times.append(benchmark_sorting_algorithm(bubblesort, arr))
    insertion_times.append(benchmark_sorting_algorithm(insertionsort, arr))
    selection_times.append(benchmark_sorting_algorithm(selectionsort, arr))

# Plotting the results
plt.figure(figsize=(10, 6))
plt.plot(input_sizes, bubble_times, label='Bubble Sort', marker='o')
plt.plot(input_sizes, insertion_times, label='Insertion Sort', marker='o')
plt.plot(input_sizes, selection_times, label='Selection Sort', marker='o')

plt.xlabel('Input Size (n)')
plt.ylabel('Time (seconds)')
plt.title('Sorting Algorithms Runtime Comparison')
plt.legend()
plt.grid(True)
plt.show()

def get_system_info():
    info = {
        "CPU": platform.processor(),
        "Cores": psutil.cpu_count(logical=True),
        "RAM": f"{round(psutil.virtual_memory().total / (1024**3), 2)} GB",
        "OS": platform.system(),
        "Python Version": platform.python_version(),
        
    }
    return info

system_info = get_system_info()
print("System Information:")
for key, value in system_info.items():
    print(f"{key}: {value}")