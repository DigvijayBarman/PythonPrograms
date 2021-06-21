numList = [10, 15, 25, 62, 76, 12, 17, 10]
oddList = []
evenList = []
def sort():
    i=0
    while i < len(numList):
        if (numList[i] % 2 != 0):
            evenList.append(numList[i])
            i=i+1
        else:
            oddList.append(numList[i])
            i=i+1
def valcheck():

    if numList[0] == numList[len(numList)-1]:
        return True
    else:
        return False

print("Odd Number list", oddList)
print("even number list", evenList)
print ("Check equivalence of values of first and last number: ", valcheck())
