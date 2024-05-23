ArrayNodes = [[-1, -1, -1] for _ in range(0,20)]
RootPointer = -1
FreeNode = 0

def AddNodes():
    global ArrayNodes
    global RootPointer
    global FreeNode

    NodeData = int(input("Enter Data "))

    if FreeNode <= 19:
        ArrayNodes[FreeNode][0] = -1
        ArrayNodes[FreeNode][1] = NodeData
        ArrayNodes[FreeNode][2] = -1
        print("freepointer :", FreeNode)
        print("root :",RootPointer)
        if RootPointer == -1:
            RootPointer = 0
        else:
            Placed = False
            CurrentNode = RootPointer
            while Placed == False:
                if NodeData < ArrayNodes[CurrentNode][1]:
                    if ArrayNodes[CurrentNode][0] == -1:
                        ArrayNodes[CurrentNode][0] = FreeNode
                        Placed = True
                    else:
                        CurrentNode = ArrayNodes[CurrentNode][0]
                        print("cur node: ", CurrentNode)
                else:
                    if ArrayNodes[CurrentNode][2] == -1:
                        ArrayNodes[CurrentNode][2] = FreeNode
                        Placed = True
                    else:
                        CurrentNode = ArrayNodes[CurrentNode][2]

        FreeNode = FreeNode + 1

    else:
        print("tree is full")

def PrintAll():
    for index in range(0, len(ArrayNodes)):
        print("LeftPointer: ", ArrayNodes[index][0], "Data: ", ArrayNodes[index][1], "RightPointer: ", ArrayNodes[index][2])


for count in range(0,10):
    AddNodes()

PrintAll()

def InOrder(root):
    if ArrayNodes[root][0] != -1:
        InOrder(ArrayNodes[root][0])

    print(ArrayNodes[root][1])

    if ArrayNodes[root][2] != -1:
        InOrder(ArrayNodes[root][2])

InOrder(RootPointer)