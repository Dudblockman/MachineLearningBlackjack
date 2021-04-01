import Deck

class controller:
    
    def __init__(self):
        self.cards = list()
    
    def giveCard(self, cardid: int):
        print("You are dealt a " + str(Deck.deck.pointValue(cardid)))
        self.cards.append(cardid)
    
    def handSize(self):
        return len(self.cards)

    def returnGameResult(self, result: int): #1 if win, 0 if loss
        if(result == 1):
            print("congratulations, you Win!")
        else:
            print("mmmm, I'm sorry, you failed.")

    def getHand(self):
        return self.cards

    def requestDecision(self, dealerCard: int):
        return input("'hit' or 'stand'?")

class humanController(controller):

    def __init__(self):
        self.cards = list()

    def returnGameResult(self, result: int):
        if(result == 1):
            print("congratulations, you Win!")
        else:
            print("mmmm, I'm sorry, you failed.")

#class aiController(controller):

class cardGame:

    def evaluateHand(self, hand):
        aces = 0
        baseValue = 0

        for card in hand:
            cardVal = Deck.deck.pointValue(card)

            if(cardVal == 1):
                aces += 1
            else:
                baseValue += cardVal


        #Solve for max viable hand value
        maxNonBust = baseValue + (11 * aces)
        maxedAceCount = aces

        #Aces default at 11, so reduce them to 1 until they are out or bust
        while (maxedAceCount > 0 and maxNonBust > 21):
            maxedAceCount += -1
            maxNonBust += -10

        #Evaluate Bust
        busted = False
        if(maxNonBust > 21):
            busted = True

        return baseValue, aces, maxNonBust, busted



    def playRound(self):
        #Intro
        print("Welcome to Round " + str(6 - self.roundCounter) + "!")
        self.roundCounter += -1

        #Handle Dealer
        dealerHandValue, dealerAces, dealerMax, dealerBust = self.evaluateHand(self.dealerHand)

        #print("The dealers hand value is: " + str(dealerHandValue) + " baseVal, " + str(dealerAces) + " Aces, " + str(dealerMax) + " maxVal, bust=" + str(dealerBust))

        if(dealerMax < 17):
            self.dealerHand.append(self.theDeck.draw())
            print("The dealer draws a card.")
        else:
            print("The dealer stands")

        #Handle Player
        playerHandValue, playerAces, playerMax, playerBust = self.evaluateHand(self.gamblerController.getHand())

        print("Your hand value is: " + str(playerHandValue) + " baseVal, " + str(playerAces) + " Aces, " + str(playerMax) + " maxVal, bust=" + str(playerBust))


        if(self.gamblerController.requestDecision(self.publicDealerCard) == 'hit'):
            print("You choose to draw.")
            newCard = self.theDeck.draw()
            self.gamblerController.giveCard(newCard)
        else:
            print("You choose to Stand")
            self.inProgress = False

        
        #Evaluate Round
        playerHandValue, playerAces, playerMax, playerBust = self.evaluateHand(self.gamblerController.getHand())
        dealerHandValue, dealerAces, dealerMax, dealerBust = self.evaluateHand(self.dealerHand)

        if(playerBust):
            self.inProgress = False
            print("You are BUSTED!")
        
        if(self.inProgress):
            self.playRound()
        else:
            print("GAME OVER: Dealer Value of " + str(dealerMax) + ", Player Value of " + str(playerMax)) #END GAME

            outcome = 0
            if((playerBust) or (playerMax < dealerMax and not dealerBust)):
                outcome = 0
                print("You Lose!")
            else:
                outcome = 1
                print("You Win!")
            
            self.gamblerController.returnGameResult(outcome)

    def __init__(self):
        #Setup Game
        self.inProgress = True
        self.roundCounter = 5

        #Determine Controller Type
        self.gamblerController = humanController()
        self.dealerHand = []


        #Deal Cards
        self.theDeck = Deck.deck()
        self.theDeck.shuffle()

        self.dealerHand.append(self.theDeck.draw())
        self.dealerHand.append(self.theDeck.draw())

        self.gamblerController.giveCard(self.theDeck.draw())
        self.gamblerController.giveCard(self.theDeck.draw())

        #Start Game
        self.publicDealerCard = self.dealerHand[0]

        print("The dealer is showing: " + str(Deck.deck.pointValue(self.publicDealerCard)))

        self.playRound() #start game

        #evaluates a hand, returns: basicValue, AceCount


        


#MAIN

theGame = cardGame()
