string1 = "A man, a plan, a canal: Panama"
nstr = ""
for i in string1:
    if i.isalnum():
        nstr+=i.lower()
rstr = nstr[::-1]
if rstr==nstr:
    print("True")
else:
    print("False")