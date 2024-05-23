class SaleData:
    def __init__(self, id , quantity):
        self.id = id
        self.quantity = quantity

CircularQueue = [SaleData("", -1) for _ in range(0,5)]
Head = 0
Tail = 0 
NumberOfItems = 0

def Enqueue(record):
    global CircularQueue
    global Head
    global Tail
    global NumberOfItems
    
    if NumberOfItems == len(CircularQueue):
        print("Queue is full")
        return -1

    CircularQueue[Tail] = record
    Tail = (Tail + 1) % len(CircularQueue)
    NumberOfItems += 1
    return 1

def Dequeue():
    global CircularQueue
    global Head
    global Tail
    global NumberOfItems
    
    if NumberOfItems == 0:
        print("Queue is empty")
        return None
    
    returnData = CircularQueue[Head]
    Head = (Head + 1) % len(CircularQueue)
    NumberOfItems -= 1
    return returnData

def EnterRecord(id, qty):
    result = Enqueue(SaleData(id,qty))
    if result != -1:
        print("Stored")

EnterRecord("ADF", 10)
EnterRecord("OOP", 1)
EnterRecord("BXW", 5)
EnterRecord("XXZ", 22)
EnterRecord("HQR", 6)
EnterRecord("LLP", 3)

# print(Dequeue().id)
# print(Dequeue().id)
# print(Dequeue().id)
# print(Dequeue().id)
# print(Dequeue().id)
# print(Dequeue().id)

EnterRecord("LLP", 3)

for index in range(Head, Head + NumberOfItems):
    print("Id:", CircularQueue[index % len(CircularQueue)].id, "Quantity:", CircularQueue[index % len(CircularQueue)].quantity)
