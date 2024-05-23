def IterativeCalculate(Number):
    Total = 0
    ToFind = 0

    ToFind = Number
    while Number != 0:
        if ToFind % Number == 0:
            Total = Total + Number

        Number = Number - 1

    return Total


def RecursiveValue(Number, ToFind):
    if Number == 0:
        return 0

    if ToFind % Number == 0:

        Number =  Number + RecursiveValue(Number - 1, ToFind)
    else:
       Number =  RecursiveValue(Number -1, ToFind )

    return Number

result = IterativeCalculate(10)
print(result)

result2 = RecursiveValue(10, 10)
print(result2)