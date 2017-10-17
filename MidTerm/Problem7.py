"""
Write a function called score that meets the specifications below.
"""

import string
def score(word, f):
    """
    word, a string of length > 1 of alphabetical characters (upper and lowercase)
    f, a function that takes in two int arguments and returns an int
    Returns the score of word as defined by the method:

    1) Score for each letter is its location in the alphabet (a=1 ... z=26) 
       times its distance from start of word.  
       Ex. the scores for the letters in 'adD' are 1*0, 4*1, and 4*2.
    2) The score for a word is the result of applying f to the
       scores of the word's two highest scoring letters. 
       The first parameter to f is the highest letter score, 
       and the second parameter is the second highest letter score.
       Ex. If f returns the sum of its arguments, then the 
           score for 'adD' is 12 
    """

    scorer = lambda c:ord(c.lower())-96
    scores = [i*scorer(c) for i,c in enumerate(word)]
    top = sorted(scores)[-2:]
    if scores == []:
        return 0
    return f(*top)
def f(x,y):
    return x+y
