# Great observation! The **space complexity of O(n)** in your code comes from the fact that **Python slicing creates a new list** rather than modifying the original list in-place.

### **Why O(n) Space Complexity?**
# ```python
# arr[:] = arr[x:] + arr[:x]
# ```
# - **`arr[x:] + arr[:x]` creates a new list**.
# - This **new list requires additional memory** proportional to the size of `arr`.
# - Since you're using `list slicing`, it allocates a **new copy** of the data rather than shifting elements in place.
# - The total number of elements being stored **remains `n`**, so the space complexity is **O(n)**.

# ### **Reducing Space Complexity to O(1)**
# If you want **in-place rotation (O(1) space complexity)**, you should use the **reversal algorithm** instead of slicing:
# ```python


# ### **Comparison**
# | Method               | Time Complexity | Space Complexity |
# |----------------------|----------------|-----------------|
# | **Slicing Approach**   | O(n)           | **O(n)** (new list created) |
# | **Reversal Algorithm** | O(n)           | **O(1)** (in-place modification) |




# Rotate the array to x positions
# by using slicing technique    




from typing import List
def rotation(arr: List[int],n:int,x:int) -> List[int]:
    if n<=2 or x%n == 0:
        return arr 
    arr[:] = arr[x:] + arr[:x]
    return arr
    


if __name__ == "__main__":
    n = int(input("Enter the number of elements in the array: "))
    arr = list(map(int, input("Enter the elements of the array: ").strip().split()))[:n]
    x = int(input("Enter the value of x: "))
    print("before the rotation: ", " ".join(map(str,arr)))
    print("after the roatation: ", " ".join(map(str,rotation(arr,n,x))))


# Time complexity: O(n)
# Space complexity: O(n)    
# where n is the number of elements in the array
# This code rotates the array to the left by x positions using slicing technique.
# If n is less than or equal to 2, or if x is a multiple of n, the array remains unchanged.
# The slicing technique is used to create a new array with the elements shifted to the left by x positions.
# The original array is modified in place using the slice assignment.
# The function returns the modified array after rotation.
# The code takes input for the number of elements in the array, the elements of the array, and the value of x.


# Example:# Input:
# Enter the number of elements in the array: 5  
# Enter the elements of the array: 1 2 3 4 5
# Enter the value of x: 2   
# Output:
# before the rotation:  1 2 3 4 5
# after the rotation:  3 4 5 1 2
# Explanation: The array is rotated to the left by 2 positions, resulting in the new order of elements.
# Example 2:
# Input:
# Enter the number of elements in the array: 4
# Enter the elements of the array: 10 20 30 40
# Enter the value of x: 4
# Output:   
# before the rotation:  10 20 30 40
# after the rotation:  10 20 30 40  


# Explanation: Since x is equal to the number of elements in the array, the array remains unchanged.
# Example 3:        
# Input:
# Enter the number of elements in the array: 3  
# Enter the elements of the array: 5 6 7
# Enter the value of x: 1
# Output:

# before the rotation:  5 6 7
# after the rotation:  6 7 5    


# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



# divide and conquer strategy by reversing different segments of the array before reversing the entire array, effectively rotating it left.






from typing import List

def reversedss(arr: List[int], start: int, end: int) -> None:
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1


def rotation(arr: List[int], n: int, x: int) -> None:
    if n<2 or x%n == 0:
        return 
    x = x%n
    reversedss(arr, 0,x-1)
    reversedss(arr, x, n-1)
    reversedss(arr, 0, n-1)   



if __name__ == "__main__" :
    n=int(input("enter the number of the elements in the array: "))
    arr=list(map(int,input("enter the elements of the array: ").strip().split()))[:n]
    x=int(input("enter the value of x: "))
    print("before the rotation: ", " ".join(map(str,arr)))
    rotation(arr,n,x)
    print("after the rotation: ", " ".join(map(str,arr)))



# Time complexity: O(n)
# Space complexity: O(1)
# where n is the number of elements in the array
# This code rotates the array to the left by x positions using the reversal algorithm.
# The reversal algorithm involves reversing different segments of the array before reversing the entire array, effectively rotating it left.
# The function `reversedss` reverses a segment of the array in place.
# The `rotation` function checks if the array has less than 2 elements or if x is a multiple of n, in which case it returns without modifying the array.
# The value of x is adjusted to be within the bounds of the array length.
# The segments of the array are reversed in three steps to achieve the desired rotation.
# The code takes input for the number of elements in the array, the elements of the array, and the value of x.  
# The modified array is printed after the rotation.
# Example:      
# Input:
# enter the number of the elements in the array: 5  
# enter the elements of the array: 1 2 3 4 5
# enter the value of x: 2
# Output:
# before the rotation:  1 2 3 4 5
# after the rotation:  3 4 5 1 2
# Explanation: The array is rotated to the left by 2 positions, resulting in the new order of elements.
# Example 2:
# Input:
# enter the number of the elements in the array: 4
# enter the elements of the array: 10 20 30 40
# enter the value of x: 4

# Output:
# before the rotation:  10 20 30 40 
# after the rotation:  10 20 30 40
# Explanation: Since x is equal to the number of elements in the array, the array remains unchanged.


































