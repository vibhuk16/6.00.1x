 """
 Implement the function getGuessedWord that takes in two parameters 
 A string, secretWord, and a list of letters, lettersGuessed. 
 This function returns a string that is comprised of letters and underscores, 
 based on what letters in lettersGuessed are in secretWord
 """
 
def getGuessedWord(secretWord, lettersGuessed):
  """
  secretWord: String, the word the user is guessing
  lettersGuessed: list, what letters have been guessed so far
  returns: String, comprised of letters and underscores that represents
           what letters in secretWord have been guessed so far.
  """
  
  def getGuessedWord(secretWord, lettersGuessed):
    guessedWord = ""
    for word in secretWord:
        if word not in lettersGuessed:
            guessedWord += "_"
        else:
            guessedWord += word
    return guessedWord
