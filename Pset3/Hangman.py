# Hangman game

import random
import string

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    Depending on the size of the word list, this function may take a while to finish.
    """
    
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)
    Returns a word from wordlist at random
    """
    
    return random.choice(wordlist)

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()
secretWord = chooseWord(wordlist)

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
  
    guessedWord = ""
    for letter in secretWord:
        if letter not in lettersGuessed:
            guessedWord += " _ "
        else:
            guessedWord += letter
    return guessedWord

"""
Implement the function getAvailableLetters that takes in one parameter 
A list of letters, lettersGuessed This function returns a string that is comprised 
of lowercase English letters all lowercase English letters that are not in lettersGuessed
"""

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

"""
 Implement the function hangman, which takes one parameter - the secretWord the user is to guess. 
 This starts up an interactive game of Hangman between the user and the computer. 
 Be sure you take advantage of the three helper functions, isWordGuessed, getGuessedWord, and getAvailableLetters, 
 that you've defined in the previous part.
"""

def hangman(secretWord):    
    """
    secretWord: string, the secret word to guess.
    Starts up an interactive game of Hangman.
    * At the start of the game, let the user know how many 
      letters the secretWord contains.
    * Ask the user to supply one guess (i.e. letter) per round.
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.
    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.
    Follows the other limitations detailed in the problem write-up.
    """
    
    guesses = 8
    secretWordLength = len(secretWord)
    lettersGuessed = []
    print("Welcome to the game, Hangman!")
    print("I am thinking of a word that is", secretWordLength, "letters long.")
    while not isWordGuessed(secretWord, lettersGuessed) and guesses > 0 :
        print("-------------")
        print("You have", guesses, "guesses left.")
        print("Available letters:", getAvailableLetters(lettersGuessed))
        guess = input("Please guess a letter: ").lower()
        if guess in lettersGuessed:
            print("Oops! You've already guessed that letter:", getGuessedWord(secretWord, lettersGuessed))
        else:
            lettersGuessed.append(guess)
            if guess in secretWord:
                print("Good Guess :", getGuessedWord(secretWord, lettersGuessed))
            else:
                guesses -= 1
                print("Oops! That letter is not in my word:", getGuessedWord(secretWord, lettersGuessed))
        if isWordGuessed(secretWord, lettersGuessed):
            print("-------------")
            print("Congratulations, you won!")
    print("-------------")
print("Sorry, you ran out of guesses. The word was ", secretWord)
