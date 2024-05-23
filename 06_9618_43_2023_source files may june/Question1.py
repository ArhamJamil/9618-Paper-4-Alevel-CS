DataArray = [0] * 25
DataFile = open("Data.txt", "r")

for lines in range(0, 25):
    DataArray[lines] = int(DataFile.readline().strip())


def PrintArray(arr):
    for index in range(0, len(arr)):
        print(arr[index], end=" ")

PrintArray(DataArray)

def LinearSearch(arr, searchVal):
    count = 0
    for index in range(0, len(arr)):
        if arr[index] == searchVal:
            count = count + 1

    return count

userInput = int(input("Enter Whole number b/w 0 and 100\n"))
if userInput >= 0 and userInput <= 100:
    timesFound = LinearSearch(DataArray, userInput)
    print("The number ",userInput," is found ", timesFound, " times")