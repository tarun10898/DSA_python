# Problem Statement: Find the largest element in an array.
# Given an array of integers, the task is to find the largest element in the array.

# ---------------------------------------------------------------code--------------------------------------------------------------
from typing import List
def largestElement(arr:List[int]) -> int:
    if not arr:
        raise ValueError("Array cannot be empty")
    largest = arr[0]
    for i in arr:
        if i>largest:
            largest = i
    return largest


if __name__ == "__main__":
    n=int(input("enter the number of elements in tha array: "))
    arr=list(map(int,input("enter the elements of the array: ").strip().split()))[:n]
    result=largestElement(arr)
    print("The largest element in the array is:", result)

# Time Complexity: O(n)
# Space Complexity: O(1)
# where n is the number of elements in the array.
# The function iterates through the array once, comparing each element to find the largest one.
# The space complexity is O(1) because we are using a constant amount of extra space for the largest variable.  
# Example:
# Input: [1, 2, 3, 4, 5]            
# Output: 5
# Input: [5, 4, 3, 2, 1]
# Output: 5


