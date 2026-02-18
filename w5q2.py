import numpy as np

a = np.array([10, 20, 30])
b = np.array([1, 2, 3])
n=int(input("enter array operation_ 1.addition \n 2.subtraction \n 3. multiplication \n4.division\n 5.to power"))
if n==1:
    print(a + b)
elif n==2:
    print(a - b)
elif n==3:
    print(a * b)
elif n==4:
    print(a / b)
elif n==5:
    print(a ** b)
else:
    print("try again")
