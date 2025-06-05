# Insertion is a basic but frequently used operation. Arrays in most languages can not be dynamically shrinked or expanded. Here, we will work with such arrays and try to insert an element at the end of the array.

# You need to modify the given array arr. The size of the array is given by sizeOfArray. You need to insert an element at the end. Array already have the sizeofarray -1 elements. Find Kth Rotation

# Examples :

# Input: sizeOfArray = 6, arr[] = {1, 2, 3, 4, 5}, element = 90
# Output: 1 2 3 4 5 90
# Explanation: After inserting 90 at the end, we have array elements as 1 2 3 4 5 90.
# Input: sizeOfArray = 4, arr[] = {1, 2, 3}, element = 50
# Output: 1 2 3 50
# Explanation: After inserting 50 at the end, we have array elements as 1 2 3 50.
# Your Task:
# You don't need to read input or print anything. You only need to complete the function insertAtEnd() that takes arr, sizeOfArray, element as input and modifies the given array arr as per requirements. The driver code takes care of the printing.

# Expected Time Complexity: O(1).
# Expected Auxiliary Space: O(1).

# Constraints:
# 1 <= sizeOfArray <= 1000
# 0 <= element, arri <= 106

# ---------------------------------------------------------code--------------------------------------------------------#
def insertAtEnd(arr, sizeOfArray, element):
    arr.append(element)  # Append the element at the end of the array
    return arr
n=int(input("enter the size of the array: "))
arr = list(map(int, input("enter the elements of the array: ").strip().split()))[:n-1]
element = int(input("enter the element to be inserted at the end: "))
result = insertAtEnd(arr, n, element)
print(" ".join(map(str, result)))  # Print the modified array   











