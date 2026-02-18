a=0
b=1
n=int(input("enter how many fibonacci numbers you want to print "))
if(n<0):
    print("inavlid number")
elif(n==1):
        print(f"{a}\n{b}\n")
else:
    print(f"{a}")
    for i in range(n-1):
        print(f"{b}")
        temp =a+b
        a=b
        b= temp
        
    