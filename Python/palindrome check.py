#Write a method to tell whether a 4-digit integer is palindromic? (1221 is palindromic, 1212 is not). Return a Boolean.
def isPal(arg1):
    checkPal = ""
    for i in range(len(arg1)-1, -1 , -1):
        checkPal += arg1[i]
    if(checkPal == arg1):
        return True
    return False
print(isPal("122222222222222322222222222222222221"))    
