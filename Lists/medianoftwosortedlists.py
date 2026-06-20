list1 = eval(input("Enter first list of numbers: "))
list2 = eval(input("Enter second list of numbers: "))
for i in list2:
    list1.append(i)
list1.sort()
total = 0
if len(list1)%2==0:
    index1 = len(list1)//2
    index2 = index1 - 1
    print((list1[index1]+list1[index2])/2)
else:
    print((list1[len(list1)/2]))