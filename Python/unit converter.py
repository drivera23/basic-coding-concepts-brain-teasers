# Convert Kelvin degrees to Celsius to Farenheit with doubles.
 #Use the K-C conversion with 0° C == 273.15° K and C-F conversion with 0° C = 32° F, 100° C = 212° F. One degree Kelvin equals one degree Celsius. (How many degrees F equal 1° C?)
 
def KtoC(testKtoC):
    return (testKtoC - 273.15)
def CtoF(testCtoF):
    return((testCtoF * 9/5) + 32)
def FtoC(testFtoC):
    return((testFtoC - 32) * 5/9)
def CtoK(testCtoK):
    return(testCtoK + 273.15)

print(KtoC(0)) # -273.15
print(CtoF(1)) # 33.8
print(FtoC(73)) # 22.77777777777778
print(CtoK(11)) # 284.15
