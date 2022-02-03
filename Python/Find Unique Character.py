#Write a function to find the first character in a String that doesn't repeat. For example, inputting "google" should return 'l'.


def unique(word):
    val = ""
    for letter in range(len(word)):
        if word[letter] in word[letter+1:] or word[letter] in word[:letter]:
            continue
        else:
            val += word[letter]
            break
    return val

print(unique("google"))    
