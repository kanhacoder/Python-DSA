def atoi():
    s = input("Enter any string: ")

    s = s.lstrip()

    if not s:
        return 0

    sign = 1
    i = 0

    if s[0] == "-":
        sign = -1
        i += 1
    elif s[0] == "+":
        i += 1

    num = 0

    while i < len(s) and s[i].isdigit():
        num = num * 10 + int(s[i])
        i += 1

    num *= sign

    if num < -2147483648:
        return -2147483648

    if num > 2147483647:
        return 2147483647

    return num


print(atoi())


# def atoi():    
#     string1 = input("Enter any string: ")
#     newstr = ""
#     boole = True
#     if len(string1)!=0:
#         if i[0] in [".", ",", "@", "#", "$", "%", "&", "*","-","+"] and i[1] in i[1] in [".", ",", "@", "#", "$", "%", "&", "*","-","+"]:
#             return 0
#         else:
#             for i in string1:
#                 if i.isspace():
#                     continue
#                 elif i.isalpha() or i in [".", ",", "@", "#", "$", "%", "&", "*"]:
#                     if newstr=="":
#                         return 0
#                     else:
#                         if int(newstr)>2147483648 or int(newstr)<-2147483648:
#                             if int(newstr)<0:
#                                 return -2147483648
#                             else:
#                                 return 2147483648
#                         else:
#                             return int(newstr)
#                 elif i.isnumeric():
#                     newstr+=i
#                     boole = False
#                 elif boole and i in ["-","+"]:
#                     newstr+=i
#                     boole = False
#                 elif not boole and i in ["-","+"]:
#                     #print(newstr)
#                     if newstr=="" or newstr in ["-","+"]:
#                         return 0
#                     else:
#                         return newstr
#                     # if int(newstr)>2147483648 or int(newstr)<-2147483648:
#                     #     if int(newstr)<0:
#                     #         return -2147483648
#                     #     else:
#                     #         return 2147483648
#                     # else:
#                     #     return int(newstr)
#     else:
#         return 0
#     if int(newstr)>2147483648 or int(newstr)<-2147483648:
#         if int(newstr)<0:
#             return -2147483648
#         else:
#             return 2147483648
#     else:
#         return int(newstr)
# print(atoi())
