class Character:
    def __init__(self, Name, Xposition, Yposition):
        self.Xposition = Xposition
        self.Yposition = Yposition
        self.Name = Name

    def GetXPosition(self):
        return self.Xposition

    def GetYPosition(self):
        return self.Yposition

    def SetXPosition(self, Xpos):

        self.Xposition += Xpos
        if self.Xposition > 10000:
            self.Xposition = 10000

        elif self.Xposition < 0:
            self.Xposition = 0

    def SetYPosition(self, Ypos):

        self.Yposition += Ypos

        if self.Yposition > 10000:
            self.Yposition = 10000

        elif self.Yposition < 0:
            self.Yposition = 0

    def Move(self, direction):
        if direction.lower() == "up":
            self.SetYPosition(10)

        elif direction.lower() == "down":
            self.SetYPosition(-10)

        elif direction.lower() == "left":
            self.SetXPosition(-10)

        elif direction.lower() == "right":
            self.SetXPosition(10)





class BikeCharacter(Character):
    def __init__(self, Name, Xposition, Yposition):
        super().__init__(Name, Xposition, Yposition)

    def Move(self, direction):
        if direction.lower() == "up":
            self.SetYPosition(20)

        elif direction.lower() == "down":
            self.SetYPosition(-20)

        elif direction.lower() == "left":
            self.SetXPosition(-20)

        elif direction.lower() == "right":
            self.SetXPosition(20)

        # return super().Move(direction)

Jack = Character("Jack", 50, 50)
Karla = BikeCharacter("Karla", 100, 50)

characterInput = input("Enter the name of character to move ")
directionInput = input("Enter direction to move up, down, left, right ")

if characterInput.lower() == Jack.Name.lower():
    Jack.Move(directionInput.lower())
    print(Jack.Name, " new positiion is X = ",
          Jack.GetXPosition(), " Y = ", Jack.GetYPosition())

if characterInput.lower() == Karla.Name.lower():
    Karla.Move(directionInput)
    print(Karla.Name, " new positiion is Y = ",
          Karla.GetYPosition(), " X = ", Karla.GetXPosition())
