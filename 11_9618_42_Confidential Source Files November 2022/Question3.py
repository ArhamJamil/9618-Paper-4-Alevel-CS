global Queue 
global headpointer
global tailpointer 

Queue = [None for i in range(0,100)]
headpointer = 0
tailpointer = 1

def Enqueue(data: int):
    global Queue 
    global tailpointer 

    if tailpointer > 100:
        return False
    else:
        Queue[tailpointer] = data
        tailpointer = tailpointer + 1

        return True


for numbers in range(0,21):
    result = Enqueue(numbers)
if result == True :
    print("Sucessfull")
else:
    print("unsucessfull")


def RecursiveOuput(Start):
    global Queue
    total = 0 
    if Start == headpointer:
        return 0
    
    total = RecursiveOuput(Start - 1) + Queue[Start]
    return total  
    

result = RecursiveOuput(21)
print(result)
