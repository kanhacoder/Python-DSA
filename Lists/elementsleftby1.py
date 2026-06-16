lst = list(input("Enter any list: "))
l = []
for j in range(1,len(lst)):
    l.append(lst[j])
l.append(lst[0])
print(l)