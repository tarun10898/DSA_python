from typing import List

def merge_sort(arr: List[int]) -> List[int]:
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = merge_sort(arr[:mid])  # Store sorted left half
        right_half = merge_sort(arr[mid:])  # Store sorted right half

        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

    return arr  # Ensure the sorted array is returned

if __name__ == "__main__":
    arr = list(map(int, input("Enter the elements of the array: ").strip().split()))
    print("Sorted array:", merge_sort(arr))


# Time Complexity: O(n log n) in all cases (best, average, worst)
# Space Complexity: O(n) due to the use of additional arrays for merging
# Stable: Yes, it maintains the relative order of equal elements
# In-place: No, it requires additional space for merging
# Adaptive: No, it does not adapt to the existing order of elements
# Comparison-based: Yes, it compares elements to determine their order
# Note: Merge sort is a divide-and-conquer algorithm that divides the array into halves, sorts each half, and then merges them back together.
# It is efficient for large datasets and is often used in external sorting algorithms.
# Merge sort is particularly useful for sorting linked lists and is a stable sorting algorithm.
# It is widely used in applications where stability is important, such as sorting records with multiple fields.
# Merge sort is not an in-place sorting algorithm, as it requires additional space for the temporary arrays used during the merge process.
# It is a fundamental algorithm in computer science and is often used as a benchmark for other sorting algorithms.
