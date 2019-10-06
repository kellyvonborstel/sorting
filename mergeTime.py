# merge function was written by me based on my own understanding/memory of how
# to merge two sorted arrays (have done this before on leetcode)

# merge function take two sorted arrays, merges them into a single sorted array,
# and returns the merged array.
def merge(arr1, arr2):
    merged = []

    # until both arrays are empty, compare first value of each array, remove
    # the lesser value from its array and append value to merged array
    while arr1 and arr2:
        if arr1[0] < arr2[0]:
            merged.append(arr1.pop(0))
        else:
            merged.append(arr2.pop(0))

    # if any integers remain in first array, append them to merged array
    if arr1:
        merged.extend(arr1)
        return merged

    # if any integers remain in second array, append them to merged array
    if arr2:
        merged.extend(arr2)
        return merged



# mergeSort function code is based on approach shown in this video:
# https://www.youtube.com/watch?v=alJswNJ4P3U&feature=youtu.be

# mergeSort function takes an array of integers, sorts those integers, and
# returns the sorted array
def mergeSort(numsArr):
    # if array length is less than 2, it's already sorted
    if len(numsArr) < 2:
        return numsArr

    # divide array into two subarrays of the left half and right half
    mid = len(numsArr) // 2
    leftHalf = numsArr[:mid]
    rightHalf = numsArr[mid:]

    # recursively call mergesort on each half
    leftHalf = mergeSort(leftHalf)
    rightHalf = mergeSort(rightHalf)

    # merge the sorted subarrays
    return merge(leftHalf, rightHalf)



import random
import time

sizes = [50000, 100000, 150000, 200000, 250000, 300000, 350000, 400000, 450000, 500000]
#sizes = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]
for i in range(len(sizes)):
    numsArr = []
    for j in range(sizes[i]):
        numsArr.append(random.randint(0, 10000))
    start = time.time()
    numsArr = mergeSort(numsArr)
    end = time.time()
    print(sizes[i], end - start)

