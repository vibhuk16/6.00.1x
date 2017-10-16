"""
Write a function called dict_invert that takes in a dictionary with immutable values and returns 
the inverse of the dictionary. The inverse of a dictionary d is another dictionary whose keys are 
the unique dictionary values in d. The value for a key in the inverse dictionary is a sorted list 
of all keys in d that have the same value in d.
"""

def dict_invert(d):
    """
    d: dict
    Returns an inverted dictionary according to the instructions above
    """
    
    inv_map = {}
    for k, v in d.items():
        inv_map[v] = inv_map.get(v, [])
        inv_map[v].append(k)
        inv_map[v] = sorted(inv_map[v])
    return inv_map
