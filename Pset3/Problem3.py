"""
Implement the function getAvailableLetters that takes in one parameter 
A list of letters, lettersGuessed This function returns a string that is comprised 
of lowercase English letters all lowercase English letters that are not in lettersGuessed
"""
 
import string
def getAvailableLetters(lettersGuessed):
    """
    lettersGuessed: List, what letters have been guessed so far
    returns: String, comprised of letters that represents what letters have not
             yet been guessed.
    """
    
    allLetters = string.ascii_lowercase
    while lettersGuessed != []:
        for letter in lettersGuessed:
            endLetters = "".join(allLetters.rsplit(letter))
            allLetters = endLetters
        return endLetters
    return allLetters
