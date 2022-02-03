# Write a function that takes a string and reverses all the vowels and leaves everything else in place. For example: "united states" -> "enated stitus"
def vowelSwitch(arg):
    vowelList = []
    reverted = ""
    for i in arg:
        if i in "AEIOUaeiou":
            vowelList.append(i)
    for i in range(0, len(arg)):
        if arg[i] in "AEIOUaeiou":
            reverted += vowelList.pop()
        else:
            reverted += arg[i]
    return reverted        
print(vowelSwitch("united states"))            
    
