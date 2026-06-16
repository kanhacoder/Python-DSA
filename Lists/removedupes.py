lst = list(input("Enter any list: "))
for i in lst:
    count = 0
    for j in lst:
        if j==i:
            count+=1
    if count>1:
        for k in lst:
            if i==k:
                lst.remove(k)
print(lst) 