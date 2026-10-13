a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
c=int(input("Enter Third number: "))
d=int(input("Enter Fourth number: "))

if (a >= b and a>=c and a>=d)  :
    print("print is greatest ",a)
elif(b>=c and b>=d):
    print("Second largest",b)
elif (c>=d):
    print("Third Largest",c)   
else:
    print("fourth largest",d)
         