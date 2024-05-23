class Character:
    def __init__(self, Name, XCoordinate, YCoordinate):
        # DECLARE NAME: STRING
        # DECLARE __XCoordinate: INTERGER
        # DECLARE __YCoordiante: INTERGER
        self.__Name = Name
        self.__XCoordinate = XCoordinate
        self.__YCoordiante = YCoordinate

    def GetName(self):
        return self.__Name
    
    def GetX(self):
        return self.__XCoordinate
    
    def GetY(self):
        return self.__YCoordiante
    
    def ChangePosition(self, XChange, YChange):

        self.__XCoordinate = self.__XCoordinate + XChange
        self.__YCoordiante =  self.__YCoordiante + YChange


character = [None for i in range(0, 10) ]

try:
    File = open("Characters.txt", "r")
    
    for lines in range(0, 10):
        name = File.readline().strip()
        x_coordinate = File.readline().strip()
        y_coordinate = File.readline().strip()

        character[lines] = Character(name, int(x_coordinate), int(y_coordinate))

    File.close()

except:
    print("File not Found")

print(character[9].GetName().lower())

characterPosition = 0

Found = False
while Found is not True:
    userInput = input("Enter Character name ")
    for count in range(0,10):
        if userInput.lower() == character[count].GetName().lower():
            characterPosition = count
            Found = True
        
       


positionInput = input("Enter A,W,S,D to move character ")
if positionInput == "A" or positionInput == "a":
    character[characterPosition].ChangePosition(-1, 0)

elif positionInput == "W" or positionInput == "w":
    character[characterPosition].ChangePosition(0, 1)

elif positionInput == "S" or positionInput == "s":
    character[characterPosition].ChangePosition(0, -1)

elif positionInput == "D" or positionInput == "d":
    character[characterPosition].ChangePosition(1, 0)
else:
    positionInput = input("Enter A,W,S,D to move character ")


print( character[characterPosition].GetName() , " has changed coordinates to X = ", character[characterPosition].GetX(), " and Y = ", character[characterPosition].GetY() )

