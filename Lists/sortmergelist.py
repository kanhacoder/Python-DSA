lst1 = list
lst2 = [2,4,6,8]
for i in lst2:
    for j in lst1:
        if j>i:
            z = lst1.index(j)
            lst1.insert(z,i)
            break
print(lst1)