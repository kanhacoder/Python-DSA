stri = input("Enter any string: ")
stack = []
z = ""
for i in range(len(stri)-1,-1,-1):
    stack.append(stri[i])
for i in stack:
    z+=i
print(z)