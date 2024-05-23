
playerArray = [["", 0] for _ in range(0,11)]

def ReadHighScores():
    global playerArray
    try:
        File = open("HighScore.txt", "r")
        index = 0
        while index != 10:
            Data1 = File.readline().strip()
            Data2 = File.readline().strip()
            playerArray[index][0] = Data1
            playerArray[index][1] = int(Data2)
            index = index + 1

        File.close()

    except:
        print("File Not Found")


def OutputHighScores():
    global playerArray
    for index in range(0, 10):
        print(playerArray[index][0], " ", playerArray[index][1])

ReadHighScores()
OutputHighScores()

name = input("Enter player name ")
score = int(input("Enter player score"))
while len(name) != 3 and score >=1 and score <= 100000:
    name = input("Enter player name ")
    score = int(input("Enter player score"))



def addTopTen(name, score):
    global playerArray
    count = 0
    for index in range(0, len(playerArray)):
        if int(playerArray[index][1]) <= score:
            count = index

    if count != 0:
        playerArray[count][0] = name
        playerArray[count][1] = score

print("Before: ")
print(playerArray)

print("After: ")
addTopTen(name, score)
print(playerArray)

def WriteTopTen():
    global playerArray
    try:
        File = open("NewHighScores.txt", "w")
        for index in range(0,len(playerArray)):
            File.write(playerArray[index][0]+"\n")

            File.write(str(playerArray[index][1])+"\n")
        File.write("hello")
    except:
        print("File not Found")

WriteTopTen()