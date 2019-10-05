# getInput code is partially based on code found here:
# https://www.w3resource.com/python-exercises/file/python-io-exercise-7.php

# getInput function takes a file name as input, reads the file one line at a
# time, and adds the contents of that line (converted from string of numbers to
# individual integers) to an array. It returns an array of those integer arrays 
# with a length equal to the number of lines in file.
def getInput(fileName):
    inputArr = []

    with open(fileName) as f:
        for line in f:
            # next line of code is from this stack overflow question:
            # https://stackoverflow.com/questions/6429638/how-to-split-a-string-
            # of-space-separated-numbers-into-integers
            data = [int(n) for n in line.split()]
            inputArr.append(data)

        return inputArr



# writeOutput function takes an array of integers and a file name. It creates
# a string of sorted numbers by joining the integers with a separating space,
# and then appends that string to the file.
def writeOutput(array, fileName):
    sortedNumsStr = ' '.join([str(n) for n in array])

    # code for writing to file is from here:
    # https://stackabuse.com/reading-and-writing-lists-to-a-file-in-python/
    with open(fileName, 'a') as filehandle:
        filehandle.write('%s\n' % sortedNumsStr)



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



# read entire input file and store each line as an array of integers
input = getInput("data.txt")

for numsArr in input:
    # remove first element, which represents number of integers to be sorted,
    # so that only integers to be sorted remain
    numsArr.pop(0)

    numsArr = mergeSort(numsArr)

    writeOutput(numsArr, 'merge.txt')

