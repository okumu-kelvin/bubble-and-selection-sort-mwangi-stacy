def bubble_sort(unsorted_list):
    for i in range (len(unsorted_list)-1,0, -1):
        for j in range(i):
            if unsorted_list[j]>unsorted_list[j+1]:
                temp=unsorted_list[j]
                unsorted_list[j]=unsorted_list[j+1]
                unsorted_list[j+1]=temp

unsorted_list=[7,9,3,5,1]
bubble_sort(unsorted_list),
#Print the Sorted List
print("Sorted list: ",unsorted_list)
