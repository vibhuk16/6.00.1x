"""
Write a recursive Python function, given a non-negative integer N, 
to count and return the number of occurrences of the digit 7 in N.
"""

def count7(N):
    """
    N: a non-negative integer
    """
    
    if N == 0: 
        return N
    if N % 10 == 7: 
        return count7(N // 10) + 1
    else:
        return count7(N // 10)
