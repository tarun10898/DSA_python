
def linearSearch(arr,num):
    n=len(arr)
    for i in range(n):
        if arr[i] == num:
            return i


n=int(input("enter the number of elenments iof the array"))
arr= list(map(int,input("enter the numbe of elements of the array").strip().split()))
num=int(input("enter the number"))
print(linearSearch(arr,num))