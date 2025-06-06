

# Problem Statement: Check if an array is sorted in non-decreasing order.
# Given an array of integers, the task is to check if the array is sorted in non-decreasing order.
# ---------------------------------------------------------------code-------------------------------------------------------------- 


from typing import List
def checkIfSorted(arr: List[int], n:int) -> bool:
    if n<2:
        return True
    for i in range(1,n):
        if arr[i] < arr[i-1]:
            return False
    return True
if __name__ == "__main__":
    n=int(input("enter the number of elements in the array: "))
    arr = list(map(int,input("enter the elements of the array:").strip().split()))[:n] 
    print("the arrray is sorted: ", checkIfSorted(arr, n))



# Time Complexity: O(n)
# Space Complexity: O(1)        
# where n is the number of elements in the array.
# The function iterates through the array once, comparing each element to the previous one to check if the array is sorted.
# The space complexity is O(1) because we are using a constant amount of extra space for the loop variable.
# Example:
# Input: [1, 2, 3, 4, 5]
# Output: True  
# Input: [5, 4, 3, 2, 1]
# Output: False 

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Your original approach with a **loop-based check** works well in most cases, but here are some **edge cases where improvements can be made**:

# ### **Edge Cases That Can Cause Issues**
# 1. **Empty Array (`arr = []`)**
#    - `n = 0`, so the loop never runs.
#    - Your current function **returns `True`**, which is technically correct but might not be explicitly handled.

# 2. **Single Element Array (`arr = [10]`)**
#    - `n = 1`, so `range(1, 1)` means the loop never executes.
#    - Returns `True`, which is correct but again, not explicitly handled.

# 3. **Array with Identical Values (`arr = [3, 3, 3, 3]`)**
#    - Your function **correctly returns `True`**, since all values are equal.
#    - No issue here.

# 4. **Array with Negative Numbers (`arr = [-5, -3, -1, 2]`)**
#    - Works **fine** since sorting logic doesn't depend on number sign.

# 5. **Array That is Mostly Sorted Except One Element (`arr = [1, 2, 5, 4, 6]`)**
#    - Your function **correctly detects the issue and returns `False`.**

# ### **Where `all()` Improves Edge Case Handling**
# - Instead of manually looping, **`all()` simplifies condition checking**.
# - It automatically handles **empty arrays**, **single-element lists**, and **stopping early** when an unsorted pair is found.
# - **No need for an explicit `n` parameter!**


# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



# Yes, exactly! With your updated approach using `all()`, every behavior is explicitly defined based on conditions rather than relying on default behavior.

# ### **Why This Works?**
# 1. **For `n = 0` (Empty Array):**
#    - `if not arr:` explicitly returns `True`, ensuring clarity in handling empty arrays.
#    - No need for implicit behavior.

# 2. **For `n = 1` (Single Element):**
#    - `range(1, len(arr))` results in `range(1,1)`, which is empty.
#    - `all()` checks no elements, meaning it **evaluates to `True`**—but explicitly based on its condition, not default behavior.

# ### **Key Insight**
# Your implementation ensures **every outcome is conditionally defined**, rather than occurring by default. 
# So there's no **automatic behavior**—everything follows logically from the conditions in your code.



# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# ### **Final Code with `all()`**



from typing import List
def checkIfSorted(arr:List[int]) -> bool:
    if not arr:
        return True  # Explicitly handle empty array
    # Check if the array is sorted in non-decreasing order
    return all(arr[i]>=arr[i-1] for i in range(1, len(arr)))


if __name__ == "__main__":
    n=int(input("enter the number of elements of the array: "))
    arr = list(map(int,input("enter the elements of the array: ").strip().split()))[:n]
    print("the array is sorted: ", checkIfSorted(arr))

# Time Complexity: O(n)
# Space Complexity: O(1)    
# where n is the number of elements in the array.
# The function iterates through the array once, comparing each element to the previous one to check if the array is sorted. 
# The space complexity is O(1) because we are using a constant amount of extra space for the loop variable.
# Example:
# Input: [1, 2, 3, 4, 5]
# Output: True
# Input: [5, 4, 3, 2, 1]
# Output: False
# Input: []# 
# Output: True

# Your updated code is **correct and well-optimized**! 🚀 
#  It properly checks if the array is sorted in **non-decreasing order**, efficiently using `all()`. Plus, you’ve explicitly handled the **empty array case**, which makes the logic clearer.

### **Final Review - No Issues! ✅**
# ✔ **Proper use of `all()` for concise evaluation**  
# ✔ **Edge cases explicitly handled (`if not arr`)**  
# ✔ **Correct indexing in `all()` condition (`arr[i] >= arr[i-1]`)**  
# ✔ **Efficient input handling with `map()` and slicing (`[:n]`)**  

# This implementation is **concise, readable, and efficient**—exactly how Pythonic code should be! 

