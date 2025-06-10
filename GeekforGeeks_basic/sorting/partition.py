
from typing import List
def partition(arr:List[int],pivot:int) -> List[int]:
    n=len(arr)
    arr[pivot], arr[n-1] = arr[n-1], arr[pivot]
    temp = [0] * n
    for x in  arr :
        if x <= arr[n-1]:
            temp.append(x)
    for x in arr:
        if x > arr[n-1]:
            temp.append(x)
    for i in range(n):
        arr[i] = temp[i]
    return arr




if __name__ == "__main__":
    n=int(input("enter the number of elements of the array: "))
    arr = list(map(int,input("enter the elements of the array: ").strip().split()))[:n]
    pivot = int(input("enter the number: "))
    print(partition(arr, pivot))