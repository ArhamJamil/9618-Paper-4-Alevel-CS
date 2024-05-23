global Animals

Animals = ["" for _ in range(0,10)]

Animals[0] = "horse"
Animals[1] = "lion"
Animals[2] = "rabbit"
Animals[3] = "mouse"
Animals[4] = "bird"
Animals[5] = "deer"
Animals[6] = "whale"
Animals[7] = "elephant"
Animals[8] = "kangaroo"
Animals[9] = "tiger"


def SortDescending():
    global Animals
    ArrayLength = len(Animals)  
    Temp = ""

    for X in range (0, ArrayLength -1):
        for Y in range(0, ArrayLength - X - 1):
            if Animals[Y][0:1] < Animals[Y+1][0:1]:
                Temp = Animals[Y]
                Animals[Y] = Animals[Y+1]
                Animals[Y+1] = Temp



SortDescending()
for index in range(0, len(Animals)):
    print(Animals[index])

print(Animals)
