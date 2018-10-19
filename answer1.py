/* Write a function that takes two arrays as input, each array contains a list of A-Z; Your program should return True if the 2nd
array is a subset of 1st array, or False if not. */

def isSubset(first, second):
    map = {}
    for char in first:
        map[char] = True
    for char in second:
        if(char not in map):
            return False
    return True
