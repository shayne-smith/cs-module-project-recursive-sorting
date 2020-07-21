# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    # Your code here
    if start <= end:
        # calculate mid
        mid = (end + start) // 2

        # base case
        if target == arr[mid]:
            return mid
        
        # recursively call binary_search on left half of array 
        # if target is smaller than the middle value
        if target < arr[mid]:
            return binary_search(arr, target, start, mid - 1)

        # recursively call binary_search on right half of array
        # if target is larger than the middle value
        if target > arr[mid]:
            return binary_search(arr, target, mid + 1, end)
        
    return -1 # if target wasn't found


# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
def agnostic_binary_search(arr, target):
    # Your code here
    pass

arr1 = [-9, -8, -6, -4, -3, -2, 0, 1, 2, 3, 5, 7, 8, 9]
print()

