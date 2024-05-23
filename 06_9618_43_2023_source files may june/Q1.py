DataArray = [0 for _ in range(0,25)]

try:
    DataFile = open("Data.txt", "r")
    data = DataFile.readlines()
    DataFile.close()

except:
    print("File Not Found ")

for index in range(0, len(data)):
    DataArray[index] = data[index].strip()

def PrintArray(arr):
    for count in range(0, len(arr)):
        print(arr[count], end=" ")

PrintArray(DataArray)

def LinearSearch(arr, searchValue):
    times = 0
    for index in range(0, searchValue):
        if searchValue == arr[index]:
            times = times + 1

    return times

userInput = int(input("Enter whole number b/w 0 and 100 inclusive "))
times = LinearSearch(DataArray, userInput)
print("The number ", userInput, " is found ", times, " times")