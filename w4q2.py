def is_palindrome(s):
    temp = ""
    for ch in s:
        temp = ch + temp
    return s == temp

s=input("enter string to check palindrome\n")

if(is_palindrome(s.lower())):
    print("String is palindrome")
else:
    print("String is not palindrome")    