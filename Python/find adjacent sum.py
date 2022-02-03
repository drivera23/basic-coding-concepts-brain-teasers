#Write a function that returns whether two adjacent numbers in a list add up to 10. (e.g. [3, 7, 5, 2] -> True) Interview 1: Adjacent Sum


def AdSum(arr):
    for i in range (0, len(arr)-1):
        if arr[i]+arr[i+1] == 10:
            return True
    return False        

print(AdSum([5, 1, 5, 5]))
