class Picture:
    def __init__(self, desc, width, height, frameColor):
        self.__Description = desc
        self.__Width = width
        self.__Height = height
        self.__FrameColour = frameColor

    def GetDescription(self):
        return self.__Description

    def GetHeight(self):
        return self.__Height

    def GetWidth(self):
        return self.__Width
    def GetColour(self):
        return  self.__FrameColour

    def SetDescription(self, newDesc):
       self.__Description = newDesc


PictureArray = [Picture("", "", "", "") for _ in range(0,100)]
print(PictureArray)

def ReadData():
    try:
        DataFile = open("Pictures.txt", "r")
        try:
            count = 0
            for index in range(21):
                desc = DataFile.readline().strip()
                print(desc)
                width = int(DataFile.readline().strip())
                print(width)
                height = int(DataFile.readline().strip())
                print(height)
                color = DataFile.readline().strip()
                print(color)

                PictureArray[index] = Picture(desc,width,height,color)
                count = count + 1

            return count
        except:
            pass


    except:
        print("File Not FFound")


result = ReadData()




width = int(input("Enter width\n"))
height = int(input("Enter height\n").lower())
colour = input("Enter colour\n").lower()

for index in range(0, result):
    if (((PictureArray[index].GetWidth()) <= width) and ((PictureArray[index].GetHeight()) <= height) and
            ((PictureArray[index].GetColour()).lower() == colour)):

        print("Description : ", PictureArray[index].GetDescription())
        print("Width : ", PictureArray[index].GetWidth())
        print("Height : ", PictureArray[index].GetHeight())
        print("Color : ", PictureArray[index].GetColour())

