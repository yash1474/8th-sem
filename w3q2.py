a=int(input("Enter first number \n"))
b=int(input("Enter second number \n"))
c=int(input("Enter third number \n"))
if(a>=b and a>=c):
    print(f"{a} is largest number")
elif(b>=a and b>=c):
    print(f"{b} is largest number")
else:
     print(f"{c} is largest number")