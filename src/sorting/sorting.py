# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(leftHalf, rightHalf):
    elements = len(leftHalf) + len(rightHalf)
    merged_arr = [0] * elements
    
    i = j = k = 0

    # merge 
    while i < len(leftHalf) and j < len(rightHalf):
        if leftHalf[i] <= rightHalf[j]:
            merged_arr[k] = leftHalf[i]
            i += 1
        else:
            merged_arr[k] = rightHalf[j]
            j += 1
        k += 1
    while i < len(leftHalf):
        merged_arr[k] = leftHalf[i]
        i += 1
        k += 1
    while j < len(rightHalf):
        merged_arr[k] = rightHalf[j]
        j += 1
        k += 1
    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # base case(s)
    if len(arr) <= 1:
        return arr

    # split array into 2 roughly equal pieces
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

arr1 = [3, 7, 19, 22]
arr2 = [16]
print(merge(arr1, arr2))
