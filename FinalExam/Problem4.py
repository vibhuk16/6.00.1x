def isPermutation(list1,list2):
    """
    Used to test if a couple of list are permutations of each other.
    We define a permutation as follows:
    
      1)The lists have the same number of elements
      2)List elements appear the same number of times in both lists
      
    """
    
    if len(list1) != len(list2):
        return False;  
    for i in range(0, len(list1)):
        if list1.count(list1[i]) != list2.count(list1[i]):
            return False

def is_list_permutation(L1, L2):
    """
    L1 and L2: lists containing integers and strings
    Returns False if L1 and L2 are not permutations of each other. 
            If they are permutations of each other, returns a 
            tuple of 3 items in this order: 
            the element occurring most, how many times it occurs, and its type
    """
    
    if (isPermutation(list1,list2) == False): 
        return False 
    elif not list1:
        return (None, None, None)
    else:
        mostOccurItem = max(list1, key=list1.count)  
        numberOfTimes = list1.count(mostOccurItem)
        theType = type(mostOccurItem)
    return (mostOccurItem, numberOfTimes, theType)
