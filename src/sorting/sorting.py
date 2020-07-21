# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(leftHalf, rightHalf):
    elements = len(leftHalf) + len(rightHalf)
    merged_arr = [0] * elements
    
    # index variables for leftHalf, rightHalf, and merged_arr, respectively
    i = j = k = 0

    # merge both arrays until either array reaches end
    while i < len(leftHalf) and j < len(rightHalf):

        # if leftHalf value is smaller or equal to rightHalf value
        if leftHalf[i] <= rightHalf[j]:

            # add leftHalf value to merged_arr and increment leftHalf index
            merged_arr[k] = leftHalf[i]
            i += 1

        # if leftHalf value is larger than rightHalf value
        else:

            # add rightHalf value to merged_arr and increment rightHalf index
            merged_arr[k] = rightHalf[j]
            j += 1
        
        # increment merged_arr index after a value has been added
        k += 1

    # iterate through leftHalf array
    while i < len(leftHalf):

        # add leftHalf values first since they're sorted and smaller than rightHalf values
        merged_arr[k] = leftHalf[i]
        i += 1
        k += 1

    # iterate through rightHalf array
    while j < len(rightHalf):
        # add rightHalf values secind since they're sorted and larger than leftHalf values
        merged_arr[k] = rightHalf[j]
        j += 1
        k += 1
    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # base case(s)
    if len(arr) <= 1:
        return arr

    # split input array into 2 roughly equal pieces
    middleIdx = len(arr) // 2
    leftHalf = arr[:middleIdx]
    rightHalf = arr[middleIdx:]

    # recursively call merge_sort on both halves until each array has length 1
    return merge(merge_sort(leftHalf), merge_sort(rightHalf))

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):
    # Your code here
    pass


def merge_sort_in_place(arr, l, r):
    # Your code here
    pass

# arr1 = [3, 7, 19, 22]
# arr2 = [16]
# print(merge(arr1, arr2))
