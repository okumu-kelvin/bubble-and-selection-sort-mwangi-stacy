def selection_sort(arr):
    for i in range (len(arr)):
        minpos=i
        for j in range(i+1, len(arr)):
            if arr[j]<arr[minpos]:
                minpos=j

        temp=arr[i]
        arr[i]= arr[minpos]
        arr [minpos] = temp
        return(arr)

        print(arr)
arr=[32,45,67,89,73,68,38,90,21,44,18]
selection_sort(arr)
print("Sorted list:", arr)
