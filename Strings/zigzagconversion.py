string1 = input("Enter any string: ")
numrow = int(input("Enter the number of rows: "))
dict1 = []
y = 0
z = numrow
finalstr = ""
for i in string1:
    if numrow==1:
        finalstr=string1
        break
    else: 
        if y<numrow:
            y+=1
            dict1.append([i,y])
        elif y==numrow:
            y=numrow+1
            z-=1
            dict1.append([i,z])
        elif z>1:
            z-=1
            dict1.append([i,z])
        elif z==1:
            y=0
            z=numrow
            y+=2
            dict1.append([i,y])
for i in range(1,numrow+1):
    for k in dict1:
        if k[1]==i :
            finalstr+=k[0]
print(finalstr)
        