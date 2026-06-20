lst1 = eval(input("Enter a list of integers: "))
newlst = []
for i in range(0,len(lst1)):
    if len(newlst)==len(lst1):
        break
    newlst.append(lst1[i])
    if len(newlst)==len(lst1):
        break
    newlst.append(lst1[len(lst1)-1-i])
print(newlst)