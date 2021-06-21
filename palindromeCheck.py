strg = input("Enter a string")
print("Reversed string: ", strg[::-1])

def palindromecheck():
 if (strg == strg[::-1]):
     print("String is a palindrome")
 else:
     print("String not palindrome")

def insertSpace():
    strn=strg
    n= len(strn)
    res = list(strn)
    for i in range(1, n-1):
        res.insert(i, ' ')
        res = ''.join(res)

    print("New string: ", str(res))

palindromecheck()
insertSpace()
