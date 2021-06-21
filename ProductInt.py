def product(x, y):
    return x*y

n1= int(input("Enter the 1st number "))
n2= int(input("Enter the second number "))

if product(n1, n2) >= 1200:
    print(product(n1, n2), "is larger than 1200")
    print("Sum= ", product(n1,n2)+1200)
else:
    print(product(n1, n2), "is smaller than 1200")
    print("Difference = ", product(n1, n2)-1200)


