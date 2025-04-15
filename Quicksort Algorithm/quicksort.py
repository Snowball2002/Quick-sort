import time
import random
import matplotlib.pyplot as plt
import numpy as np

def partition(arr, low, high):
    """
    This function takes the last element as pivot, places
    the pivot element at its correct position in sorted
    array, and places all smaller elements to the left of
    pivot and all greater elements to the right of pivot.
    """
    pivot = arr[high]  # pivot element
    i = low - 1  # index of smaller element
    
    for j in range(low, high):
        # If current element is smaller than or equal to pivot
        if arr[j] <= pivot:
            # increment index of smaller element
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quicksort(arr, low, high):
    """
    Iterative implementation of QuickSort to avoid recursion depth issues
    arr[] --> Array to be sorted,
    low --> Starting index,
    high --> Ending index
    """
    # Create an auxiliary stack
    size = high - low + 1
    stack = [0] * size
    
    # Initialize top of stack
    top = -1
    
    # Push initial values of low and high to stack
    top = top + 1
    stack[top] = low
    top = top + 1
    stack[top] = high
    
    # Keep popping from stack while it's not empty
    while top >= 0:
        # Pop high and low
        high = stack[top]
        top = top - 1
        low = stack[top]
        top = top - 1
        
        # Set pivot element at its correct position
        p = partition(arr, low, high)
        
        # If there are elements on the left side of pivot,
        # push left side to stack
        if p - 1 > low:
            top = top + 1
            stack[top] = low
            top = top + 1
            stack[top] = p - 1
            
        # If there are elements on the right side of pivot,
        # push right side to stack
        if p + 1 < high:
            top = top + 1
            stack[top] = p + 1
            top = top + 1
            stack[top] = high

def measure_performance(arr):
    """
    Measure and return the execution time of quicksort on the provided array
    """
    arr_copy = arr.copy()  # Create a copy so we don't modify the original
    start_time = time.time()
    quicksort(arr_copy, 0, len(arr_copy) - 1)
    end_time = time.time()
    return end_time - start_time, arr_copy

# Example sequences
sequence_a = [10, 80, 3, 19, 14, 7, 5, 12]
print("Original Sequence A:", sequence_a)
time_a, sorted_a = measure_performance(sequence_a)
print("Sorted Sequence A:", sorted_a)
print(f"Time taken: {time_a:.6f} seconds\n")

# Generate random sequences
random.seed(42)  # For reproducibility
sequence_b = [random.randint(1, 1000) for _ in range(100)]
sequence_c = [random.randint(1, 10000) for _ in range(1000)]

print(f"Testing with sequence B (100 random integers)")
time_b, sorted_b = measure_performance(sequence_b)
print(f"Time taken: {time_b:.6f} seconds\n")

print(f"Testing with sequence C (1000 random integers)")
time_c, sorted_c = measure_performance(sequence_c)
print(f"Time taken: {time_c:.6f} seconds\n")

# Generate different cases for analysis
def generate_test_cases(size):
    # Best case: Already sorted array
    best_case = list(range(size))
    
    # Worst case: Reverse sorted array
    worst_case = list(range(size, 0, -1))
    
    # Average case: Random array
    avg_case = [random.randint(1, size*10) for _ in range(size)]
    
    return best_case, worst_case, avg_case

# Test different sizes to analyze time complexity
sizes = [10, 100, 500, 1000, 2000, 3000]
best_times = []
worst_times = []
avg_times = []

for size in sizes:
    best_case, worst_case, avg_case = generate_test_cases(size)
    
    best_time, _ = measure_performance(best_case)
    best_times.append(best_time)
    
    worst_time, _ = measure_performance(worst_case)
    worst_times.append(worst_time)
    
    avg_time, _ = measure_performance(avg_case)
    avg_times.append(avg_time)
    
    print(f"Size {size}: Best={best_time:.6f}s, Worst={worst_time:.6f}s, Avg={avg_time:.6f}s")

# Plot performance analysis
plt.figure(figsize=(12, 8))
plt.plot(sizes, best_times, 'g-', marker='o', label='Best Case')
plt.plot(sizes, avg_times, 'b-', marker='s', label='Average Case')
plt.plot(sizes, worst_times, 'r-', marker='^', label='Worst Case')

# Plot the theoretical curves
n_range = np.array(sizes)
plt.plot(n_range, n_range * np.log2(n_range) * 1e-5, 'k--', label='O(n log n)')
plt.plot(n_range, n_range**2 * 1e-6, 'k:', label='O(n²)')

plt.xlabel('Input Size (n)')
plt.ylabel('Time (seconds)')
plt.title('Quicksort Algorithm Performance Analysis')
plt.legend()
plt.grid(True)
plt.savefig('quicksort_performance.png')
plt.savefig('quicksort_performance.pdf')

print("\nPerformance analysis completed! Check 'quicksort_performance.png' and 'quicksort_performance.pdf' for the visual results.")
