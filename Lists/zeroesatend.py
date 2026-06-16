lst = list(input("Enter any list: "))
new = []
zeroes = 0
for i in lst:
    if int(i)==0:
        zeroes += 1
    else:
        new.append(int(i))
for i in range(0,zeroes):
    new.append(0)
print(new)