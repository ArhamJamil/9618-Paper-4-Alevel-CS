def IterativeVowels(Value):
    Total = 0
    LengthString = len(Value)
    for X in range(0, LengthString):
        FirstCharacter = Value[0:1]

        if FirstCharacter.lower() == "a" or FirstCharacter.lower() == "e" or FirstCharacter.lower() == "i" or FirstCharacter.lower() == "o" or FirstCharacter.lower() == "u":
            Total = Total + 1

        Value = Value[1: len(Value)]

    return Total



word = IterativeVowels("house")
print(word)

def RecursiveVowels(Value):
    Total = 0
    LengthString = len(Value)
    if LengthString == 0 :
        return 0
  
    # print(Value)
    FirstCharacter = Value[LengthString - 1]

    if FirstCharacter.lower() == "a" or FirstCharacter.lower() == "e" or FirstCharacter.lower() == "i" or FirstCharacter.lower() == "o" or FirstCharacter.lower() == "u":
      
        Total = Total + 1
     
    LengthString = LengthString -1
    Value = Value[0: LengthString]
    Total = Total + RecursiveVowels(Value) 
    
    # print(LengthString)
    return Total
   



word2 = RecursiveVowels("house")
print(word2)