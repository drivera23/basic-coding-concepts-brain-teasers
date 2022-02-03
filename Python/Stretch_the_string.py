def stretchStr(string):
    decompressed = ""
    for i in range(len(string)):
        if string[i] in "1234567890":
            afterL = string[i+1]
            for j in range(int(string[i])):
                decompressed += afterL
        elif string[i-1] in "1234567890":
            continue
        else:
            decompressed += string[i]
    return decompressed

print(stretchStr("2a2bc3d7f"))
