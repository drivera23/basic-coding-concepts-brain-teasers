# Write a function that takes a number and returns a string according to the Look-and-say pattern. (e.g. 11112 -> 4112) Interview 1: Look and Say
example = 11112
helper = {}
ans = ""
for i in str(example):
    if i not in helper:
        helper[i] = 1
    else:
        helper[i] += 1
for k, v in helper.items():
    ans += str(v) + str(k)
print(ans)   
