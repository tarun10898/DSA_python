
# Problem Statement: Find the second largest element in an array.
# Given an array of integers, the task is to find the second largest element in the array.

from typing import List
def secondLargest(arr:List[int], n:int)->int:
    if n<2 :
        raise ValueError("Array must contain at least two elements")
    first,second = float('-inf'), float('-inf')
    for i in arr:
        if i>first:
            second = first
            first = i
        elif i>second and i!=first:
            second = i
    if second == float('-inf'):
        raise ValueError("There is no second largest element in the array") 
    return second    


if __name__ == "__main__":
    n=int(input("enter the numbers in the array: "))
    arr = list(map(int,input("enter the elements of tha array: ").strip().split()))[:n]
    print(secondLargest(arr,n))


# Time Complexity: O(n)
# Space Complexity: O(1)
# where n is the number of elements in the array.
# The function iterates through the array once, comparing each element to find the second largest one.  
# The space complexity is O(1) because we are using a constant amount of extra space for the first and second variables.
# Example:  
# Input: [1, 2, 3, 4, 5]
# Output: 4
# Input: [5, 4, 3, 2, 1]
# Output: 4