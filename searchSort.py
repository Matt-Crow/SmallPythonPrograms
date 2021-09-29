def printArray(array):
    print(" ")
    for itemNum in range(0, len(array)):
        print("#" + str(itemNum) + ": " + str(array[itemNum]))

def linearSearch(array, find):
    foundInd = -1
    found = False
    time = 0
    
    while time < len(array) and not found:
        if array[time] == find:
            print("Found " + str(find) + ", taking " + str(time + 1) + " iterations")
            found = True
        time += 1
    return foundInd

def binarySearch(array, find):
    selectSort(array)
    high = len(array) - 1
    low = 0
    
    time = 0
    foundInd = -1
    found = False
    
    while high >= low and not found:
        mid = (high + low) / 2
        if array[mid] > find:
            high = mid - 1
        elif array[mid] < find:
            low = mid + 1
        else:
            foundInd = mid
            found = True
            print("Found " + str(find) + ", taking " + str(time + 1) + " iterations")
        time += 1
    
    return found

"""
Primary advantage: performs the smallest number of swaps, so it works will when
                   it would be expensive to move or copy data
"""
def selectSort(array):
    for index in range(0, len(array)):
        #find the smallest element, starting at item
        indexOfSmallest = index
        for checkSizeIndex in range(index + 1, len(array)):
            if array[checkSizeIndex] < array[indexOfSmallest]:
                indexOfSmallest = checkSizeIndex
        temp = array[index]
        array[index] = array[indexOfSmallest]
        array[indexOfSmallest] = temp

def insertSort(array):
    for index in range(1, len(array)):
        shoveIndex = index
        while shoveIndex > 0 and array[shoveIndex] < array[shoveIndex - 1]:
            temp = array[shoveIndex]
            array[shoveIndex] = array[shoveIndex - 1]
            array[shoveIndex - 1] = temp
            shoveIndex -= 1


a = [5, 3, 2, 4, 1]
for i in range(1, 6):
    binarySearch(a, i)