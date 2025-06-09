
from typing import List
def bubbble(arr:List[int]) -> List[int]: 
    n=len(arr)
    for i in range(n):
        swapped = False
        for j in range (n-i-1):
            if arr[j]> arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True  
        if not swapped:
            break   
    return arr                

def selection(arr:List[int]) -> List[int]:
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr
if __name__ == "__main__":   
    n=int(input("enter the number of elements of the list: "))
    arr=list(map(int,input("enter the elements of the array: ").strip().split()))[:n]   
    print(bubbble(arr))
    print( selection(arr))