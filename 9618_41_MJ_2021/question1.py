class Node:
    def __init__(self, data=0, node=-1):
        self.data = data
        self.nextNode = node

startPointer = 0
emptylist = 5

linkedList = [Node() for _ in range(0,10)]
linkedList[0] = Node(1, 1)
linkedList[1] = Node(5, 4)
linkedList[2] = Node(6, 7)
linkedList[3] = Node(7, -1)
linkedList[4] = Node(2, 2)
linkedList[5] = Node(0, 6)
linkedList[6] = Node(0, 8)
linkedList[7] = Node(56, 3)
linkedList[8] = Node(0, 9)
linkedList[9] = Node(0, -1)

def outputNodes():
    global linkedList
    global startPointer

    currentPointer = startPointer
    while currentPointer != -1:
        print(linkedList[currentPointer].data)
        currentPointer = linkedList[currentPointer].nextNode

def insert_at_last(data):
    global emptylist
    global linkedList
    global startPointer

    newNode = Node(data, -1)
    temp = emptylist
    emptylist = linkedList[emptylist].nextNode

    linkedList[temp] = newNode
    currentNode = startPointer
    while linkedList[currentNode].nextNode != -1:
        currentNode = linkedList[currentNode].nextNode

    linkedList[currentNode].nextNode = temp

def insert_at_first(data):
    global startPointer
    global linkedList
    global emptylist

    if emptylist == -1:
        print("No empty space available to add a new node.")
        return

    newNodeIndex = emptylist
    emptylist = linkedList[emptylist].nextNode

    linkedList[newNodeIndex].data = data
    linkedList[newNodeIndex].nextNode = startPointer

    startPointer = newNodeIndex


def insert_after_node(index, data):
    global emptylist
    global linkedList

    if emptylist == -1:
        print("No empty space available to add a new node.")
        return
    else:
        temp = emptylist
        emptylist = linkedList[temp].nextNode

        newNode = Node(data, -1)

        linkedList[temp] = newNode

        currentNode = index

        linkedList[temp].nextNode = linkedList[currentNode].nextNode
        linkedList[currentNode].nextNode = temp

def delete_at_first():
    global emptylist
    global linkedList
    global startPointer

    if startPointer == -1:
        print("No further item to delete")
        return

    currentNode = startPointer
    startPointer = linkedList[currentNode].nextNode
    linkedList[currentNode] = Node(0, -1)
    linkedList[currentNode].nextNode = emptylist
    emptylist = currentNode


def delete_at_last():
    global linkedList
    global emptylist
    global startPointer

    if startPointer == -1:
        print("No further item to delete")
        return

    temp = emptylist

    currentNode = startPointer
    while linkedList[linkedList[currentNode].nextNode].nextNode != -1:
        currentNode = linkedList[currentNode].nextNode

    linkedList[linkedList[currentNode].nextNode].data = 0
    linkedList[linkedList[currentNode].nextNode].nextNode = -1
    print(linkedList[linkedList[currentNode].nextNode].data, "updated")
    emptylist = linkedList[currentNode].nextNode
    print(emptylist)
    linkedList[currentNode].nextNode = -1
    print(linkedList[currentNode].data, "cureent")

    # print(currentNode)




# insert_at_last(10)
# # insert_at_last(119)
# insert_at_first(100)
# insert_after_node(2,1003)
# insert_after_node(2,1004)
# insert_after_node(2,1005)
# insert_after_node(2,1006)

print(startPointer, ": StartPointer")
print(emptylist, ": emptylist")





outputNodes()

print(startPointer, ": StartPointer")
print(emptylist, ": emptylist")

delete_at_last()
delete_at_last()
outputNodes()

