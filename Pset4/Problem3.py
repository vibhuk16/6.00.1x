"""
Implement the isValidWord function
Returns True if word is in the wordList and is entirely
composed of letters in the hand. Otherwise, returns False.
"""

def isValidWord(word, hand, wordList):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.
   
    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """
    
    handTemp = hand.copy()
    if word in wordList:
        for letter in word:
            if letter in handTemp.keys():
                handTemp[letter] -= 1
                if handTemp[letter] < 0:
                    return False
            else:
                return False
    else:
        return False
    return True
