 """
 Implement the function isWordGuessed that takes in two parameters 
 A string, secretWord, and a list of letters, lettersGuessed. 
 This function returns a boolean - True if secretWord has been guessed 
 and False otherwise.
 """
 
 def isWordGuessed(secretWord, lettersGuessed):
    """
    secretWord: String, the word the user is guessing
    lettersGuessed: List, what letters have been guessed so far
    returns: Boolean, True if all the letters of secretWord are in lettersGuessed;
             False otherwise
    """
    
    for letter in secretWord:
        if letter not in lettersGuessed:
            return False
    return True
