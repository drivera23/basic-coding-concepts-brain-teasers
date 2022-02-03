#Write a function that takes in a string and then returns a string containing the first letter for each word in the string.

def firstOfEach(string):
    L = string.split()
    newstr = ""
    for i in L:
        newstr += i[0]
    return newstr
print (firstOfEach("hey iron"))  
