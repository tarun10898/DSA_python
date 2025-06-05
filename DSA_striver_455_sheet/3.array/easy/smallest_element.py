
# Problem Statement: Find the smallest element in an array.
# Given an array of integers, the task is to find the smallest element in the array.        
# ---------------------------------------------------------------code--------------------------------------------------------------

from typing import List
def smallestElement(arr:List[int]) -> int:
    if not arr:
        raise ValueError("Array cannot be empty")
    smallest= arr[0]
    for i in arr:
        if i < smallest:
            smallest = i
    return smallest

if __name__ == "__main__":
    n=int(input("enter the number of elements of the array: "))
    arr=list(map(int,input("enter the elements of the array: ").strip().split()))[:n]
    print( smallestElement(arr) )

# Time Complexity: O(n)
# Space Complexity: O(1)    
# where n is the number of elements in the array.
# The function iterates through the array once, comparing each element to find the smallest one.    

# The space complexity is O(1) because we are using a constant amount of extra space for the smallest variable.
# Example:  
# Input: [1, 2, 3, 4, 5]            
# Output: 1 

# Input: [5, 4, 3, 2, 1]
# Output: 1
