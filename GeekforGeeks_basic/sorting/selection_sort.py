



from typing import List
def selectionSort(arr:List[int]) -> List[int]:
    n=len(arr)
    for i in range(n):
        min_index=i
        for j in range(i+1,n):
            if arr[j]<arr[min_index]:
                min_index=j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr



__name__ == "__main__"
n=int(input("enter the number of elements of the list"))
arr=list(map(int,input("enter the elements of the array: ").strip().split()))[:n]
result = selectionSort(arr)
print(result)
# Time Complexity: O(n^2) in the worst case, O(n) in the best case
# Space Complexity: O(1) as it sorts the array in place
# Stable: No, it does not maintain the relative order of equal elements
# In-place: Yes, it does not require additional space for sorting
# Adaptive: No, it does not adapt to the existing order of elements 
# Comparison-based: Yes, it compares elements to determine their order