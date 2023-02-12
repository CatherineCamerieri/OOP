import random
#instructions in this file
# The Coin class simulates a coin that can
# be flipped.

class Coin: #reserve word class (named class Coin) name of class always uppercase
    # The _ _init_ _ method initializes the
    # sideup data attribute with 'Heads'.

    def __init__(self): #short for initialization, only parameter is self (only the instance calling is getting effected)
        self.sideup = 'Heads' #only one attribute = sideup

    # The toss method generates a random number
    # in the range of 0 through 1. If the number
    # is 0, then sideup is set to 'Heads'.
    # Otherwise, sideup is set to 'Tails'.

    def toss(self): #uses the self parameter
        if random.randint(0, 1) == 0: #simulating tossing of coin
            self.sideup = 'Heads'
        else:
            self.sideup = 'Tails'

    # The get_sideup method returns the value
    # referenced by sideup.

    def get_sideup(self): #returning the value of the attribute
            return self.sideup
#more compartmentalized the better