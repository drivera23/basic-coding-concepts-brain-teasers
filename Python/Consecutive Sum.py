#Write a function that takes in a list of numbers and returns a list of numbers containing the cumulative sum for the list. (e.g. [4, 23, 6] -> [4, 27, 33])

consecutive = [4, 23, 6]
for i in range(1, len(consecutive)):
    consecutive[i] = consecutive[i] + consecutive[i-1]
print(consecutive) 
