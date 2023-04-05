# Linear Searching
# Q1. Given an array arr[] of n elements, rite a function to search a given element x in arr[]

# def search(arr,n,x):
#     for i in range(0,n):
#         if (arr[i] == x):
#             return i
#     return -1
# arr= [2,3,4,10,40]
# x=1
# n=len(arr)
# result= search(arr,n,x)
# if (result == -1):
#     print("Element is not present in array")
# else:
#     print("Element is present at index:", result)


# Binary Search
#  Q1. Given a sorted array arr[] of n element, write a function to search a given element x in arr[].
# A simple approach is to do Linear Search. the time complexity of above algorithm is O(n).Another approach to perform
# the same task is using Binary Searching.

# def binarySearch (arr,l,r,x):
#     # Check base case
#     if r >= 1:
#         mid = l+(r-l)//2
#     # If element is present at the middle  itself
#         if arr[mid] == x:
#             return mid
#         # If elements are smaller than mid, than it can only be present in left subarray
#         elif arr[mid] > x:
#             return binarySearch(arr,l,mid-1,x)
#         # Else the element can only be present in right subarray
#         else:
#             return binarySearch(arr,mid+1,r,x)
#     else:
#         # Element is not present in the array
#         return -1
# arr = [2,3,4,10,40]
# x = 10
# # Function Call
# result = binarySearch(arr,0,len(arr)-1,x)
# if result != -1:
#     print(f"Element is present at index {result}")
# else:
#     print("Element is not present in the array")



# Binary Search
# def binarySearch(array,x,low,high):
#     while low<= high:
#         mid = low + (high - low)
#         if array[mid] == x:
#             return mid
#         elif array[mid] < x:
#             low = mid+1
#         else:
#             high = mid-1
#     return -1
# array = [3,4,5,6,7,8,9]
# print(array)
# x = int(input())
# result = binarySearch(array,x,0,len(array)-1)
# if result != -1:
#     print(f"Element is present at {result}")
# else:
#     print("Not Found!")
