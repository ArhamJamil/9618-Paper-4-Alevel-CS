class Vehicle:
    def __init__(self, ID, MaxSpeed, IncreaseAmount):
        self.__ID = ID
        self.__MaxSpeed = MaxSpeed
        self.__CurrentSpeed = 0
        self.__IncreaseAmount = IncreaseAmount
        self.__HorizontalPosition = 0

    def GetCurrentSpeed(self):
        return self.__CurrentSpeed

    def GetIncreaseAmount(self):
        return self.__IncreaseAmount

    def GetMaxSpeed(self):
        return self.__MaxSpeed

    def GetHorizontalPosition(self):
        return self.__HorizontalPosition

    def SetCurrentSpeed(self, Cspeed):
        self.__CurrentSpeed = Cspeed

    def SetHorizontalPosition(self, Xpos):
        self.__HorizontalPosition = Xpos

    def IncreaseSpeed(self):
        self.__CurrentSpeed = self.__CurrentSpeed + self.__IncreaseAmount
        if self.__CurrentSpeed > self.__MaxSpeed:
            print("Current speed can't exceed its maximum speed")
        else:
            self.__HorizontalPosition = self.__HorizontalPosition + self.__CurrentSpeed



class Helicopter(Vehicle):
    def __init__(self, ID, MaxSpeed, IncreaseAmount, VerticalChange, MaxHeight):
        super().__init__(ID, MaxSpeed, IncreaseAmount)
        self.__VerticalPosition = 0
        self.__VerticalChange = VerticalChange
        self.__MaxHeight = MaxHeight

    def GetVerticalPosition(self):
        return self.__VerticalPosition

    def IncreaseSpeed(self):
        if self.__VerticalPosition > self.__MaxHeight:
            print("Vertical Position of a helicopter can't exceeds its maximum height")
        else:
            self.__VerticalPosition = self.__VerticalPosition + self.__VerticalChange

        self.__CurrentSpeed = self.GetCurrentSpeed() + self.GetIncreaseAmount()
        if self.__CurrentSpeed > self.GetMaxSpeed():
            print("Current speed of Helicpoter can't exceed its maximum speed")
        else:
            self.__HorizontalPosition = self.GetHorizontalPosition() + self.__CurrentSpeed

        return super().IncreaseSpeed()

    

def OutputVehicle(vehicleType):
    if isinstance(vehicleType, Helicopter):
        print("Horizontal Position : ",vehicleType.GetHorizontalPosition())
        print("Speed : ",vehicleType.GetCurrentSpeed())
        print("Vertical Position : ",vehicleType.GetVerticalPosition())
    else:
        print("Horizontal Position : ",vehicleType.GetHorizontalPosition())
        print("Speed : ",vehicleType.GetCurrentSpeed())


car = Vehicle("Tiger", 100, 20)
helicopter = Helicopter("Lion", 350, 40, 3, 100)



car.IncreaseSpeed()
car.IncreaseSpeed()
print("CAR")
OutputVehicle(car)

helicopter.IncreaseSpeed()
helicopter.IncreaseSpeed()
print("HELICOPTER")
OutputVehicle(helicopter)