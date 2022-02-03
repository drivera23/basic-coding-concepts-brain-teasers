#Write a function that accepts two lists and returns whether the two lists have at least one overlapping value. (e.g. [2, 3, 4], [5, 8, 3] -> True) 


def findOL(arg1, arg2):
    for i in arg1:
        if i in arg2:
            return True
    return False        
    
arg1 = [2, 3, 4] 
arg2 = [5, 8, 3]

print(findOL(arg1, arg2))
