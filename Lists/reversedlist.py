lst = list(input("Enter any list: "))
l = []
print(lst)
for i in range(0,len(lst)/2):
    # l.append(lst[0-i-1])
    lst[i]=lst[0-i-1]
print(lst)