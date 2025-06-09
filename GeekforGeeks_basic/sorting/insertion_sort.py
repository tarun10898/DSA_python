

from typing import List
def insertion(arr:List[int]) -> List[int]:
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


if __name__ == "__main__":
    n=int(input("enter the number of elements of the array: "))
    arr= list(map(int,input("enter the elements of the array: " ).strip().split()))[:n]
    print(insertion(arr))