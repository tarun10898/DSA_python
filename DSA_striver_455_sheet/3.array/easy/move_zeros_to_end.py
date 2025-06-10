
# brute force

from typing import List
def zeros(arr:List[int],n:int) -> List[int]:
    temp=[]
    count =0
    for i in arr:
        if i != 0:
            temp.append(i)
            count +=1
    for i in range(count,n):
        temp.append(0)        
    return temp


if __name__ == "__main__":
    n=int(input("enter the no of elements in the array"))
    arr=list(map(int,input("enter the elements of the array").strip().split()))
    print(zeros(arr,n))


# optimize solution



from typing import List
def zeros(arr:List[int],n:int) -> List[int]:
    index = 0
    for i in range(n):
        if arr[i] != 0:
            if index != i:
                arr[index], arr[i] = arr[i],arr[index]
            index += 1 
    return arr        
    

if __name__ == "__main__":
    n=int(input("enter the elements in the array"))
    arr=list(map(int,input("enter the numbe of elements of the array").strip().split()))
    print(zeros(arr,n))
