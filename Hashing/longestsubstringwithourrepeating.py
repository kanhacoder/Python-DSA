str1 = input("Enter any string: ")
longest = []
if len(str1)>0:
    for i in range(0,len(str1)):
            count = 1
            nstr = ""
            for j in range(i+1,len(str1)):
                if str1[i]!=str1[j]:
                    count+=1
                else:
                    longest.append(count)
                    break
    if len(longest)==0:
        print(0)
    else:
        print(max(longest))

else:
    print(0)