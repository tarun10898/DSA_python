
# def missingNumber(arr,n):
#     temp = set(arr)
#     missing = []
#     for i in range(1,n+1):
#         if i not in temp:
#             missing.append(i)
#     return missing

def missingNumber(arr,n):
    arr1=set(arr)
    missing= []
    num = 1
    while num<=n:
        if num not in arr1:
            missing.append(num)
        num+=1    
    return missing



n=int(input("enter the numbe to find the missing elements of the array: "))
arr=list(map(int,input("enter the values in the array: " )))
print(missingNumber(arr,n))



# time,space complexity is O(n) 


def missingNumber(arr, n):
    for i in range(len(arr)):  # Place numbers in correct positions
        while 1 <= arr[i] <= n and arr[i] != arr[arr[i] - 1]:
            arr[arr[i] - 1], arr[i] = arr[i], arr[arr[i] - 1]  # Swap elements

    missing = [i + 1 for i in range(n) if i >= len(arr) or arr[i] != i + 1]
    return missing

n = int(input("Enter the upper bound of the sequence: "))
arr = list(map(int, input("Enter the values in the array: ").split()))

print("Missing numbers:", missingNumber(arr, n))


# time complexity is O(n)
# space complexity is O(1)