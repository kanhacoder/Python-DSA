str1 = input("Enter any string: ")
dict1 = {}
for i in str1:
    if i.lower() not in dict1:
        if i.isspace()==False:
            dict1[i.lower()] = 1
    else:
        if i.isspace()==False:
            dict1[i.lower()] += 1
for i in str1:
    if dict1[i.lower()]==1:
        print(i)
        break