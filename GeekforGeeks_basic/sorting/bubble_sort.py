

from typing import List
def bubble(arr:List[int],n:int) -> List[int]:
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr


__name__ == "__main__"
n=int(input("enter the number of elements of the array: "))   
arr=list(map(int, input("enter the elements of the array: ").strip().split()))[:n]
print(bubble(arr,n) )

# Time Complexity: O(n^2) in the worst case, O(n) in the best case
# Space Complexity: O(1) as it sorts the array in place     
# Stable: Yes, it maintains the relative order of equal elements
# In-place: Yes, it does not require additional space for sorting   
# Adaptive: Yes, it can be optimized to stop early if the array is already sorted
# Comparison-based: Yes, it compares elements to determine their order  
# Note: Bubble sort is not efficient for large datasets and is primarily used for educational purposes.
# It is a simple sorting algorithm that repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order.
# It is named "bubble sort" because smaller elements "bubble" to the top of the list.
# Bubble sort is not suitable for large datasets due to its O(n^2) time complexity, but it is easy to understand and implement.
# It is often used as an introductory algorithm in computer science education.
