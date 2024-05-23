global Queue 
global HeadPointer 
global Tailpointer

Queue = [None for _ in range(0,50)]
HeadPointer = -1
TailPointer = 0


def Enqueue(data):
    global Queue
    global TailPointer

    if TailPointer == len(Queue):
        print("Queue is full , Data push limit reached")
    else:
        Queue[TailPointer] = data
        TailPointer = TailPointer + 1


def Dequeue():
    global Queue
    global HeadPointer

    if TailPointer == 0:
        return "Empty"
    else:
        HeadPointer = HeadPointer + 1
        returnData = Queue[HeadPointer]
        return returnData
    

def ReadData():
    try:
        File = open("QueueData.txt", "r")
        FileData = File.readlines()
        for i in range(0, len(FileData) ):
            Enqueue(FileData[i].strip())

    except:
        print("file not found")
    

class RecordData:
    def __init__(self, Id, Total):
        self.id = Id
        self.total = Total


global Records 
global NumberRecords

Records = [RecordData(" ", 0) for _ in range(0,50)]
NumberRecords = 0

def TotalData():
    global NumberRecords
    global Records

    DataAccessed = Dequeue()
    Flag = False

    if NumberRecords == 0:
        Records[NumberRecords].id = DataAccessed
        Records[NumberRecords].total = 1
        Flag = True
        NumberRecords = NumberRecords + 1
    else:
        for X in range(0, (NumberRecords - 1)):
            if Records[X].id == DataAccessed:
                Records[X].total = Records[X].total + 1
                Flag = True

    if Flag == False:
        Records[NumberRecords].id = DataAccessed
        Records[NumberRecords].total = 1
        NumberRecords = NumberRecords + 1


def OutputRecords():
    global Records
    for index in range(0, NumberRecords):
        print("ID ", Records[index].id, " Total ", Records[index].total)



ReadData()
for call in range(0, TailPointer):
    TotalData()
OutputRecords()
