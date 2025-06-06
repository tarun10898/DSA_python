
# Given a sorted array, the task is to remove duplicates from the array in-place and return the new length of the array.    
# The function should modify the input array such that each element appears only once, and the order of elements is preserved.



from typing import List
def noDuplicates(arr:List[int],n:int) -> List[int]:
    if not arr:
        return []
    unique_elements = [arr[0]]
    for i in range(1, n):
        if arr[i] != arr[i-1]:
            unique_elements.append(arr[i])
    return unique_elements

if __name__ == "__main__":
    n= int(input("enter the number of elements of the array:"))
    arr= list(map(int,input("enter the elements of the  array: ").strip().split()))[:n]
    print("The values are: ", " ".join(map(str, noDuplicates(arr, n))))

# Time Complexity: O(n)
# Space Complexity: O(n)
# where n is the number of elements in the array.
# The function iterates through the array once, comparing each element to the previous one to find unique elements.

# The space complexity is O(n) because we are storing the unique elements in a new list.
# Example:
# Input: [1, 1, 2, 2, 3]
# Output: [1, 2, 3]
# Input: [1, 2, 3, 4, 5]
# Output: [1, 2, 3, 4, 5]
# Input: [1, 1, 1, 1, 1]    
# Output: [1]
# Input: [] 
# Output: []


# Note: The input array is assumed to be sorted in non-decreasing order.
# The function modifies the input array in-place, but for demonstration purposes, it returns a new list of unique elements. 



# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------



# impove the space complexity to O(1) by modifying the input array in-place
from typing import List
def noDuplicates(arr:List[int],n:int) -> int:
    if n == 0:
        return 0
    unique_index = 0
    for i in range(1, n):
        if arr[i] != arr[unique_index]:
            unique_index += 1
            arr[unique_index] = arr[i]
    return unique_index + 1


if __name__ == "__main__":
    n=int(input("enter the number of the elements to be entered in the array: "))
    arr=list(map(int,(input("enter the elements of the array: ").strip().split()))[:n])
    new_length = noDuplicates(arr, n)
    print(" The values are: ", " ".join(map(str, arr[:new_length])))


# Time Complexity: O(n)
# Space Complexity: O(1)    
# where n is the number of elements in the array.
# The function iterates through the array once, comparing each element to the previous one to find unique elements. 
# The space complexity is O(1) because we are modifying the input array in-place without using any additional data structures.
# Example:
# Input: [1, 1, 2, 2, 3]
# Output: [1, 2, 3]
# Input: [1, 2, 3, 4, 5]
# Output: [1, 2, 3, 4, 5]
# Input: [1, 1, 1, 1, 1]    
# Output: [1]
# Input: []
# Output: []

# Note: The input array is assumed to be sorted in non-decreasing order.
# The function modifies the input array in-place, and the new length of the array is returned.  









