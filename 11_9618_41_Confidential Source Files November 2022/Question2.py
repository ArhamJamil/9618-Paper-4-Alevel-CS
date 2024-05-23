class Card:
    def __init__(self, Number, Colour):
        self.__Number = Number
        self.__Colour = Colour

    def GetNumber(self):
        return self.__Number

    def GetColour(self):
        return self.__Colour
    

class Hand:
    def __init__(self,obj1, obj2, obj3, obj4, obj5):
        self.__FirstCard = 0
        self.__NumberCards = 5
        self.__Cards = [obj1, obj2, obj3, obj4, obj5]

    def GetCard(self, cardIndex):
        return self.__Cards[cardIndex]
    



Card1 = Card(1, "red")
Card2 = Card(2, "red")
Card3 = Card(3, "red")
Card4 = Card(4, "red")
Card5 = Card(5, "red")
Card6 = Card(1, "blue")
Card7 = Card(2, "blue")
Card8 = Card(3, "blue")
Card9 = Card(4, "blue")
Card10 = Card(5, "blue")
Card11 = Card(1, "yellow")
Card12 = Card(2, "yellow")
Card13 = Card(3, "yellow")
Card14 = Card(4, "yellow")
Card15 = Card(5, "yellow")


Player1 = Hand(Card1, Card2, Card3, Card4, Card11)
Player2 = Hand(Card12, Card13, Card14, Card15, Card6)

def CalculateValue(playerHand):
    cardScore = 0
    for index in range(0, 5):
        card = playerHand.GetCard(index)
        if card.GetColour() == "red":
            cardScore = cardScore + 5
        if card.GetColour() == "blue":
            cardScore = cardScore + 10
        if card.GetColour() == "yellow":
            cardScore = cardScore + 15

    return cardScore

Player1_Score = CalculateValue(Player1)
Player2_Score = CalculateValue(Player2)

if Player1_Score > Player2_Score:
    print("Player 1 wins with extra Points: ", (Player1_Score - Player2_Score))
elif Player2_Score > Player1_Score:
    print("Player 2 wins with extra Points: ", (Player2_Score - Player1_Score))
else:
    print("Both player have Same Points !!! Match Draw")




