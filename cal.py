c1 = input("Please Select and enter operator: (%, *, +, -,) ")
c2 = int(input(" PLease Enter 1st number: "))
c3 = int(input(" PLease Enter 2nd Number: "))

if c1 == "+":
    print("this is a +:) ", c2 + c3)
elif c1 == "-":
    print("This is a -:)", c2 - c3)
elif c1 == "*":
    print("This is a *:)", c2 * c3)
elif c1 == "%":
    print("This is a %:)", c2 / c3)
else:
    print("PLease Check And Try Again:) ") 
