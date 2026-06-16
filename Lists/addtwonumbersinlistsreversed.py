l1 = list(input("Enter: "))
l2 = list(input("Enter: "))
num1 = ""
num2 = ""
for i in range(len(l1)-1,-1,-1):
    num1+=l1[i]
for i in range(len(l2)-1,-1,-1):
    num2+=l2[i]
num1 = int(num1)
num2 = int(num2)
print(num1,num2)
total = num1 + num2
total = str(total)
ltotal = []
for i in range(len(total)-1,-1,-1):
    ltotal.append(int(total[i]))
print(ltotal)