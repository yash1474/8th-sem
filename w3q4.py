s=input("Enter your string\n")
count=0
for i in s:
    if i in "aeiouAEIOU":
        count+=1

print(f"there are {count} vowels in string")