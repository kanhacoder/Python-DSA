# PROBLEM SKIPPED AS OF 19-06-2026

s = input("Enter any string: ")
p = input("Enter any pattern: ")
l = []
ns = ""
yn = True
if s=="" and (p=="" or p==".*" or (p[0].isalpha()and p[1]=="*")):
    print(True)
else:
    for i in s:
        l.append(i)
    for i in range(0,len(s)):
        if s[i]==p[i]:
            ns+=i
        elif p[i]==".":
            ns+=i
        elif i=="*" and i<1 and yn:
            if s[i]==p[i-1]:
                ns+=i
                count = 0
                for j in range(i,len(s)+1):
                    if s[j]==s[i]:
                        count+=1
                if count==len(s)-i:
                    print("True")
                    break