# Selection Sorting
# def selectionSort(arr,size):
#     for step in range(size):
#         minimum = step
#         for i in range(step+1,size):
#             if arr[i] < arr[minimum]:
#                 minimum = i
#                 (arr[step],arr[minimum]) = (arr[minimum],arr[step])
#
# input = [1,6,8,2,9,14]
# size = len(input)
# selectionSort(input,size)
# print("Sorted array in Ascending Order:")
# print(input)


# Bubble Sorting
# def bubbleSorting(arr):
#     for i in range(len(arr)):
#         for j in range(0,len(arr)-i-1):
#             if arr[j] > arr[j+1]:
#                 (arr[j],arr[j+1]) = (arr[j+1],arr[j])
#
# input = [-2,45,0,11,-9]
# bubbleSorting(input)
# print("Sorted Array in ascending order")
# print(input)


# Insertion Sorting
# def insertionSorting(arr):
#     for step in range(1,len(arr)):
#         key = arr[step]
#         j = step - 1
#
#         while j>= 0 and key < arr[j]:
#             arr[j+1] = arr[j]
#             j-=1
#         arr[j+1] = key
#
# input = [9,5,1,4,3]
# insertionSorting(input)
# print("sorted array in Ascending Order")
# print(input)