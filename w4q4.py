li = [5, 2, 9, 1, 6]

n = len(li)

for i in range(n):
    for j in range(0, n - i - 1):
        if li[j] > li[j + 1]:
            li[j], li[j + 1] = li[j + 1], li[j]

print("Ascending:", li)

for i in range(n):
    for j in range(0, n - i - 1):
        if li[j] < li[j + 1]:
            li[j], li[j + 1] = li[j + 1], li[j]

print("Descending:", li)
