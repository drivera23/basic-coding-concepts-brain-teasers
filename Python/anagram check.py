#Write a function which takes two strings and returns true if they are anagrams.


def Anagram(arg1, arg2):
    spLit = []
    for i in arg1:
        spLit.append(i)
    for i in arg2:
        if i not in spLit:
            return False;
    return True

print(Anagram("matte", "tamti")) 
