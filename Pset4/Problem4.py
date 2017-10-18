"""
You'll need to implement the helper calculateHandlen function
Returns the length (number of letters) in the current hand.
"""

def calculateHandlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string int)
    returns: integer
    """
    
    handLen = 0
    for letter in hand.keys():
        handLen += hand[letter]
    return handLen
