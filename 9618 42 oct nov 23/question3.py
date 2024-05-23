StackVowel = ["" for _ in range(0,100)]
StackConsonant = ["" for _ in range(0,100)]

global VowelTop
global ConsonantTop

VowelTop = 0
ConsonantTop = 0

def PushData(data):
    global VowelTop
    global ConsonantTop
    global StackVowel
    global StackConsonant

    if data.lower() == "a" or data.lower() == "e" or data.lower() == "i" or data.lower() == "o" or data.lower() == "u":
        if VowelTop == len(StackVowel):
            print("Stack Vowel is full")
        else:
            StackVowel[VowelTop] = data
            VowelTop = VowelTop + 1
    else:
        if ConsonantTop == len(StackConsonant):
            print("Consonant Stack if full")
        else:
            StackConsonant[ConsonantTop] = data
            ConsonantTop = ConsonantTop + 1


def ReadData():
    try:
        DataFile = open("StackData.txt", "r")
        try:
            for lines in range(0,100):
                data = DataFile.readline().strip()
                PushData(data)

        except:
            pass
    except:
        print("File Not Found")


def PopVowel():
    global StackVowel
    global VowelTop
    if VowelTop == 0:
        return  "No Data"
    else:
        VowelTop = VowelTop - 1
        removedElement = StackVowel[VowelTop]

        return removedElement

def PopConsonant():
    global StackConsonant
    global ConsonantTop
    if ConsonantTop == 0:
        return "No Data"
    else:
        ConsonantTop = ConsonantTop - 1
        removedElement = StackConsonant[ConsonantTop]
        return removedElement


ReadData()
print(StackVowel)
print(VowelTop)
print(StackConsonant)
print(ConsonantTop)
for count in range(0,5):
    userData = input("What do you want to POP ")
    if userData.lower() == "vowel":
        result = PopVowel()
        print(result)

    if userData.lower() == "consonant":
        result = PopConsonant()
        print(result)










