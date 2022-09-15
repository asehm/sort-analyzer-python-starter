# SORT ANALYZER STARTER CODE

import time

# RETURN DATA FROM FILE AS AN ARRAY OF INTERGERS
def loadDataArray(fileName):
    temp = []

    # Read file line by line
    fileref = open(fileName, "r")
    for line in fileref:
        line = line.strip()  # Clean up line
        temp.append(int(line))  # Add integer to temp list

    fileref.close()

    return temp

def bubbleSort(anArray):
    n = len(anArray)
    for i in range(n - 1):
        for x in range(n-i-1):
            if anArray[x] > anArray[x + 1]:
                anArray[x], anArray[x + 1] = anArray[x + 1], anArray[x]

def selectionSort(anArray):
    n = len(anArray)
    for i in range(n):
        min = i
        for x in range(i+1, n):
            if anArray[x] < anArray[min]:
                min = x
        anArray[i], anArray[min] = anArray[min], anArray[i]

def insertionSort(anArray):
    n = len(anArray)
    for i in range(1, n):
        ins = anArray[i]
        x = i - 1
        while x >= 0 and ins < anArray[x]:
            anArray[x + 1] = anArray[x]
            x = x - 1
        anArray[x + 1] = ins

def timeArray(anArray, sortMethod):
    startTime = time.time()
    sortMethod(anArray)
    endTime = time.time()
    print(f"{sortMethod} Sort Random Data: {endTime - startTime} seconds")

# LOAD DATA FILE INTO GLOBAL VARIABLES
randomData = loadDataArray("data-files/random-values.txt")
reversedData = loadDataArray("data-files/reversed-values.txt")
nearlySortedData = loadDataArray("data-files/nearly-sorted-values.txt")
fewUniqueData = loadDataArray("data-files/few-unique-values.txt")

# VERIFY LOADED DATA BY PRINTING FIRST 50 ELEMENTS


# EXAMPLE OF HOW TO TIME DURATION OF A SORT ALGORITHM
# startTime = time.time()
# bubbleSort(randomData)
# endTime = time.time()
# print(f"Bubble Sort Random Data: {endTime - startTime} seconds")
timeArray(randomData, insertionSort)
timeArray(reversedData, insertionSort)
timeArray(nearlySortedData, insertionSort)
timeArray(fewUniqueData, insertionSort)