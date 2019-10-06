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



import random
import time


#sizesArr = [50, 100, 150, 200, 250, 300, 300, 400, 450, 500]

#sizes = [1500, 3000, 4500, 6000, 7500, 9000, 10500, 12000, 13500, 15000]
sizes = [2000, 4000, 6000, 8000, 10000, 12000, 14000, 16000, 18000, 20000]
#sizesArr = [500, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 40000]
for i in range(len(sizes)):
    numsArr = []
    for j in range(sizes[i]):
        numsArr.append(random.randint(0, 10000))
    start = time.time()
    numsArr = insertSort(numsArr)
    end = time.time()
    print(end - start)
        
