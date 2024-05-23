class SaleData:
    def __init__(self, ID, Quantity) -> None:
        self.ID = ID
        self.Quantity = Quantity


global CircularQueue
global HeadPointer
global TailPointer
global NumberOfItems

CircularQueue = [None] * 5
for Index in range(0, len(CircularQueue)):
    CircularQueue[Index] = SaleData("", -1)


HeadPointer = 0
TailPointer = 0
NumberOfItems = 0


def Enqueue(newrecord):
    global TailPointer
    global HeadPointer
    global NumberOfItems

    if NumberOfItems == len(CircularQueue) - 1:
        print("Queue is Full")
        return -1
    else:
        if TailPointer == len(CircularQueue) - 1:
            TailPointer = 0
        CircularQueue[TailPointer] = newrecord
        TailPointer = TailPointer + 1
        NumberOfItems = NumberOfItems + 1
        return 1


def Dequeue():
    global TailPointer
    global HeadPointer
    global NumberOfItems

    if NumberOfItems == 0:
        print("Queue is empty")
        return None
    else:
        if HeadPointer == len(CircularQueue) - 1:
            HeadPointer = 0
        
        deletedRecord = CircularQueue[HeadPointer]
        CircularQueue[HeadPointer] = None
        HeadPointer = HeadPointer + 1
        NumberOfItems = NumberOfItems -1
        return deletedRecord


def EnterRecord(ID, Quantity):
    response = Enqueue(SaleData(ID, Quantity))
    if response == 1:
        print("Stored")
    else:
        print("Full")


for i in range(0, len(CircularQueue)):
    Id = input("Enter Item ID ")
    Qty = int(input("Enter item Qty "))

    EnterRecord(Id, Qty)
    print(NumberOfItems)

print(CircularQueue)
Dequeue()
print(NumberOfItems)
print(CircularQueue)

EnterRecord("LLP", 3)
print(NumberOfItems)
print(CircularQueue)
