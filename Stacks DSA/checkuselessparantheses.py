bracket = input("Input an expression with brackets")
for i in range(0,len(bracket)):
    if (bracket[i]=="(" or bracket[i]=="{" or bracket[i]=="[") and (bracket[i+1]=="(" or bracket[i+1]=="{" or bracket[i+1]=="[" or bracket[i+1]==")" or bracket[i+1]=="}" or bracket[i+1]=="]"):
        print("True")
        break
    else:
        print("False")
        break