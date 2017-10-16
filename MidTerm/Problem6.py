"""
Implement a function that meets the specifications below.
"""

def max_val(t): 
    """ 
    t, tuple or list
    Each element of t is either an int, a tuple, or a list
    No tuple or list is empty
    Returns the maximum int in t or (recursively) in an element of t 
    """ 
    
    result = []
    if isinstance(t, int):
        result.append(t)
        return result
    elif isinstance (t, (tuple,list)):
        def update_result(t):
            for item in t:
                if isinstance(item, (tuple,list)):
                    update_result(item)
                else:
                    result.append(item)
        update_result(t)
    return max(result)
