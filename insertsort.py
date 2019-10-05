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



# insertSort function code is based on pseudocode shown on page 7 of pdf for
# Analysis of Sorting lecture

# insertSort function takes an array of integers, sorts those integers, and
# returns the sorted array
def insertSort(numsArr):
    # loop through array starting at second item, which is the start of the
    # unsorted part of the array (that will become shorter with each iteration)
    for i in range(1, len(numsArr)):
        # store the current value 
        val = numsArr[i]
        # we will compare value at j to our current value
        j = i - 1

        # keep comparing our stored value to the values to left of it until we
        # find one that's greater or we run out of values to compare
        while numsArr[j] > val and j >= 0:
            numsArr[j + 1] = numsArr[j]
            j -= 1

        # put stored value in its place within the sorted portion of array
        numsArr[j + 1] = val            

    return numsArr



# read entire input file and store each line as an array of integers
input = getInput("data.txt")

for numsArr in input:
    # remove first element, which represents number of integers to be sorted,
    # so that only integers to be sorted remain
    numsArr.pop(0)

    numsArr = insertSort(numsArr)

    writeOutput(numsArr, 'insert.txt')

