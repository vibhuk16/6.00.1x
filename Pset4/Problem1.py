"""
The function getWordScore should accept as input a string of lowercase letters (a word) 
and return the integer score for that word, using the game's scoring rules.
Scoring:
    -The score for the hand is the sum of the scores for each word formed.
    
    -The score for a word is the sum of the points for letters in the word, 
     multiplied by the length of the word, plus 50 points if all n letters are used on the first word created.
    
    -Letters are scored as in Scrabble; A is worth 1, B is worth 3, C is worth 3, D is worth 2, E is worth 1, and so on. 
     We have defined the dictionary SCRABBLE_LETTER_VALUES that maps each lowercase letter to its Scrabble letter value.

    -Be sure to check that the hand actually has 1 'w', 2 'e's, and 1 'd' before scoring the word!
"""

def getWordScore(word, n):
    """
    Returns the score for a word. Assumes the word is a valid word.

    The score for a word is the sum of the points for letters in the
    word, multiplied by the length of the word, PLUS 50 points if all n
    letters are used on the first turn.

    Letters are scored as in Scrabble; A is worth 1, B is worth 3, C is
    worth 3, D is worth 2, E is worth 1, and so on (see SCRABBLE_LETTER_VALUES)

    word: string (lowercase letters)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    returns: int >= 0
    """
    
    freq = {}
    for letter in word:
        freq[letter] = freq.get(letter,0) + 1
    points = 0
    letterCount = 0
    for letter in freq.keys():
        points += SCRABBLE_LETTER_VALUES[letter] * freq[letter] * len(word)
    if len(word) == n:
        points += 50
    return points
