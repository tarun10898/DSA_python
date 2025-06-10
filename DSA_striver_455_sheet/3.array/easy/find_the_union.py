


from typing import List,Set
def unions(arr1:List[int], arr2:List[int] ) -> Set[int]:
    return set(arr1+arr2)



if __name__ == "__main__":
    arr2 = list(map(int,input("enter the elements of tht e array 2 : ").strip().split()))
    arr1 = list(map(int,input("enter the emelemtnsof the first array1 ").strip().split()))

    print(unions(arr1,arr2))



    # time complexity O(m+n)
    # spcae complexity O(m+n)




# Two pointers method

def unions(arr1,arr2):
    i,j = 0,0
    union = []
    while i<len(arr1) and j<len(arr2):
        if arr1[i] <= arr2[j]:
            if not union or union[-1] != arr1[i]:
                union.append(arr1[i]) 
            i+=1
        else:
            if not union or union[-1] != arr2[j]:
                union.append(arr2[j])
            j+=1    
    while i< len(arr1):
        if not union or union[-1] != arr1[i]:
            union.append(arr1[i]) 
        i+=1
    while j< len(arr2):
        if not union or union[-1] != arr2[j]:
            union.append(arr2[j])
        j+=1

    return union


if __name__ == "__main__":
    arr2 = list(map(int,input("enter the elements of tht e array 2 : ").strip().split()))
    arr1 = list(map(int,input("enter the emelemtnsof the first array1 ").strip().split()))

    print(unions(arr1,arr2))



    # time complexity: O(m+n)
    # space complexity: O(1)


    # if the sorting is done befor moving into the set then the time complexity becomes O(nlogn+mlogm)