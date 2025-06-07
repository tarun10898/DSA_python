

from typing import List
def dicti(arr:List[int]) -> dict:
    hasmap = {}
    for value in arr:
        if value in hasmap:
            hasmap[value] += 1
        else:
            hasmap[value] = 1

    return hasmap


__name__ =="__main__"
n = int(input("Enter the number of elements in the array: "))   
arr = list(map(int, input("Enter the elements of the array: ").strip().split()))[:n]
# for index, value in enumerate(arr):
#     print(f"Element at index {index} is {value}")
print(dicti(arr))