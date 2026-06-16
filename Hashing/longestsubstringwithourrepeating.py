str1 = input("Enter any string")
lst = []
length = 0
z = {}
for i in str1:
    if i not in z:
        z[i]=1
        length+=1
    else:
        lst.append(length)
        z[i]+=1
        length = 0
        z={}
print(max(lst))