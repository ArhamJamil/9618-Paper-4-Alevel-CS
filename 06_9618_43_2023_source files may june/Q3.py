global Animal
global Colour 
global AnimalTopPointer
global ColourTopPointer

Animal = [ "" for _ in range(0,20) ]
Colour = ["" for _ in range(0,10)]

AnimalTopPointer = 0
ColourTopPointer = 0

def PushAnimal(DataToPush):
    global Animal
    global AnimalTopPointer

    if AnimalTopPointer == 20:
        return False
    else:
        Animal[AnimalTopPointer] = DataToPush
        AnimalTopPointer = AnimalTopPointer + 1
        return True
    

def PopAnimal():
    global Animal
    global AnimalTopPointer
    returnAnimal = ""

    if AnimalTopPointer == 0 :
        return ""
    else:
        returnAnimal = Animal[AnimalTopPointer - 1]
        AnimalTopPointer = AnimalTopPointer - 1
        return returnAnimal


def PushColour(DataToPush):
    global Colour
    global ColourTopPointer

    if ColourTopPointer == 10:
        return False
    else:
        Colour[ColourTopPointer] = DataToPush
        ColourTopPointer = ColourTopPointer + 1
        return True
    

def PopColour():
    global Colour
    global ColourTopPointer
    returnColour = ""

    if ColourTopPointer == 0 :
        return ""
    else:
        returnColour = Colour[ColourTopPointer - 1]
        ColourTopPointer = ColourTopPointer - 1
        return returnColour



def ReadData():
    try:
        AnimalFile = open("AnimalData.txt", "r")
        ColourFile = open("ColourData.txt", "r")

        for lines in range(0, 8):
            Animaldata = AnimalFile.readline().strip()
            PushAnimal(Animaldata)
        AnimalFile.close()

        for lines in range(0,10):
            ColourData = ColourFile.readline().strip()
            PushColour(ColourData) 
        ColourFile.close()
    except:
        print("Filenot found")


def OutputItem():
    animal = PopAnimal()
    colour = PopColour()

    if animal == "":
        
        print("No animal ")
        PushColour(colour)

    elif colour == "":
 
        print("No colour")
        PushAnimal(animal)

    else:
        print(colour, animal)


ReadData()
OutputItem()
OutputItem()
OutputItem()
OutputItem()



