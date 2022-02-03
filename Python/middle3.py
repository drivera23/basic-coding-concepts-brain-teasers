# Given a string of odd length, return the string length 3 from its middle, so "Candy" yields "and". The string length will be at least 3. 
# Test cases are
    #   middleThree("Candy") → "and"
    #   middleThree("and") → "and"
    #   middleThree("solving") → "lvi"

test = "Peter"
middle = len(test) // 2
print(test[middle-1: middle+2])
