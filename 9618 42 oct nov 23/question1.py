import _datetime

class Character:
    def __init__(self, name, dateofbirth, intelligence, speed):
        self.__CharacterName = name
        self.__DataOfBirth = dateofbirth
        self.__Intelligence = intelligence
        self.__Speed = speed

    def GetName(self):
        return self.__CharacterName

    def GetIntelligence(self):
        return self.__Intelligence

    def SetIntelligence(self, val):
        self.__Intelligence = val

    def Learn(self):
        newIntelligence = (0.1 * self.GetIntelligence()) + self.GetIntelligence()
        self.SetIntelligence(newIntelligence)

    def ReturnAge(self):
        currentDate = "22 may 2023"
        birth = int(self.__DataOfBirth.split(" ")[2])
        age = int(currentDate.split(" ")[2]) - birth
        return age



FirstCharacter = Character("Royal", "1 january 2019", 70, 30)

FirstCharacter.Learn()
print("Name:", FirstCharacter.GetName(), " age: ", FirstCharacter.ReturnAge(), " intelligence: ", int(FirstCharacter.GetIntelligence()))


class MagicCharacter(Character):
    def __init__(self, name, dateofbirth, intelligence, speed, element):
        super().__init__(name, dateofbirth, intelligence, speed)
        self.__Element = element

    def Learn(self):
        if self.__Element == "water" or self.__Element == "fire":
            newIntelligence = (0.2 * super().GetIntelligence()) + super().GetIntelligence()
            super().SetIntelligence(newIntelligence)

        else:
            if self.__Element == "earth":
                newIntelligence = (0.3 * super().GetIntelligence()) + super().GetIntelligence()
                super().SetIntelligence(newIntelligence)

            else:
                newIntelligence = (0.1 * super().GetIntelligence()) + super().GetIntelligence()
                super().SetIntelligence(newIntelligence)



FirstMagic = MagicCharacter("Light", "3 March 2018", 75, 22 , "fire")
FirstMagic.Learn()
print("Name:", FirstMagic.GetName(), " age: ", FirstMagic.ReturnAge(), " intelligence: ", int(FirstMagic.GetIntelligence()) )

