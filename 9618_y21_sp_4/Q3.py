TheData = [20, 3, 4, 8, 12, 99, 4, 26, 4]

def InsertionSort(arr = TheData):
    for count in range(1, len(arr)):
        DataToInsert =arr[count]
        Inserted = 0
        NextValue = count - 1
        while NextValue >= 0 and Inserted != 1:
            if DataToInsert < arr[NextValue] :
                TheData[NextValue+1] = TheData[NextValue]
                NextValue = NextValue - 1
                TheData[NextValue+1] = DataToInsert

            else:
                Inserted = 1


def OutputData(arr):
    for index in range(0, len(arr)):
        print(arr[index])

print("Before Sorting: ")
OutputData(TheData)

print("After Sorting: ")
InsertionSort()
OutputData(TheData)

def Search(val):
    for index in range(0, len(TheData)):
        if TheData[index] == val:
            return True
    return False
        

userInput = int(input("Enter Whole number to search "))
result = Search(userInput)
if result == True:
    print("Number Found")
else:
    print("Number not Found")