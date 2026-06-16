str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")
dict1 = {}
dict2 = {}
for char in str1:
    if char not in dict1:
        dict1[char] = 1
    else:
        dict1[char] += 1
for char in str2:
    if char not in dict2:
        dict2[char] = 1
    else:
        dict2[char] += 1
if dict1 == dict2:
    print("True")
else:
    print("False  ")
print(dict1)
print(dict2)