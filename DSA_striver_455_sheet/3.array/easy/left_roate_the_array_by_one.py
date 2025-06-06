

# left rotate the array by one
# Problem Statement: Rotate the array to the left by one position.      
# Given an array of integers, the task is to rotate the array to the left by one position.



from typing import List
def rotation(arr:List[int],n:int) -> List[int]:
    if n <= 1:
        return arr
    temporary = arr[0]
    for i in range(1,n):
        arr[i-1] = arr[i]
    arr[n-1] = temporary
    return arr

if __name__ == "__main__":
    n = int(input("enter the number of elements to be entered in to the list: "))
    arr = list(map(int, input("enter the elements of the array: ").strip().split()))[:n]
    print("before the iteration: ", " ".join(map(str, arr)))
    print("the values after iteration: ", " ".join(map(str, rotation(arr, n))))

# Time Complexity: O(n)
# Space Complexity: O(1)
# where n is the number of elements in the array.   
# # The function iterates through the array once, shifting each element to the left by one position.
# # The space complexity is O(1) because we are using a constant amount of extra space for the temporary variable.
# Example:
# # Input: [1, 2, 3, 4, 5]
# # Output: [2, 3, 4, 5, 1]
# # Input: [5, 4, 3, 2, 1]  
# # Output: [4, 3, 2, 1, 5]
# # Note: The function modifies the original array in place and returns the modified array.
# # The input array is assumed to be a list of integers.    
#     