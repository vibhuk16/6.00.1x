def laceStrings(s1, s2):
    """
    s1 and s2 are strings.

    Returns a new str with elements of s1 and s2 interlaced,
    beginning with s1. If strings are not of same length, 
    then the extra elements should appear at the end.
    For example, if we lace 'abcd' and 'efghi', 
    we would get the new string: 'aebfcgdhi'
    """
 
    result = ""
    maxLen = max(len(s1),len(s2))
    if maxLen == 0:
        return result
    for i in range(maxLen):
        try:
            result += s1[i]
        except:
            result += ""
        try:
            result += s2[i]
        except:
            result += ""
    return result
