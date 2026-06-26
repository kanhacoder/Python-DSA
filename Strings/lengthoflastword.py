string1 = "   fly me   to   the moon  "
length = 0
for i in range(len(string1)-1,1,-1):
    if string1[i].isalpha():
        length+=1
    if string1[i].isspace() and length!=0:
        print(length)
        break
