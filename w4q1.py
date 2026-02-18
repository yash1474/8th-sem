n=int(input("Enter no. of elements"))
print("Enter elements")
li=[]
sum=0
for i in range(n):
    temp=int(input())
    li.append(temp)
    sum+=li[i]

avg=sum/n
print(f"sum= {sum} and average ={avg}")