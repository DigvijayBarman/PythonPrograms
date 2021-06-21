strg = input("Enter a string")
print("Reversed string: ", strg[::-1])

def palindromecheck():
 if (strg == strg[::-1]):
     print("String is a palindrome")
 else:
     print("String not palindrome")

def insertSpace():
    strn=strg
    print(" ".join(strn))

palindromecheck()
insertSpace()
