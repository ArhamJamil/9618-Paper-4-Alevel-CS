global Animal
global Colour
global AnimalTopPointer
global ColourTopPointer

Animal = [None] * 20
Colour = [None] * 10
AnimalTopPointer = 0
ColourTopPointer = 0

def PushAnimal(DataToPush: str) :
    global AnimalTopPointer
    global Animal

    if AnimalTopPointer == 20 :
        return False
    else:
        Animal[AnimalTopPointer] = DataToPush
        AnimalTopPointer = AnimalTopPointer + 1
        return True
    

def PopAnimal():
    global AnimalTopPointer
    global Animal

    returnData = ""

    if AnimalTopPointer == 0 :
        return ""
    else:
        returnData = Animal[AnimalTopPointer - 1]
        AnimalTopPointer = AnimalTopPointer - 1
        return returnData
    

def PushColour(DataToPush: str) :
    global ColourTopPointer
    global Colour

    if ColourTopPointer == 10 :
        return False
    else:
        Colour[ColourTopPointer] = DataToPush
        ColourTopPointer = ColourTopPointer + 1
        return True
    

def PopColour():
    global ColourTopPointer
    global Colour

    returnData = ""

    if ColourTopPointer == 0 :
        return ""
    else:
        returnData = Colour[ColourTopPointer - 1]
        ColourTopPointer = ColourTopPointer - 1
        return returnData
    


def ReadData():
    try:
        File = open("AnimalData.txt", "+r")
        data = File.readline().strip()
        while data != "":
            PushAnimal(data)
            data = File.readline().strip()

        try:
            File2 = open("ColourData.txt", "+r")
            data2 = File2.readline().strip()
            while data2 != "":
                PushColour(data2)
                data2 = File2.readline().strip()
        except:
            print("ColourData.txt not found")

    except:
        print("AnimalData.txt does not exists")

def OutputItem():
    animalData = PopAnimal()
    colourData = PopColour()

    if animalData == "":
        print("No Animal")
        PushColour(colourData)
    elif colourData == "":
        print("No Colour")
        PushAnimal(animalData)
    else:
        print(colourData, animalData)

ReadData()
OutputItem()
OutputItem()
OutputItem()
OutputItem()
# print(Animal)
# print(Colour)
