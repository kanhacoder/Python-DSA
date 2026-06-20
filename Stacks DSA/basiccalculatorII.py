def calculator():    
    exp = input("Enter the expression to be calculated: ")
    sign = []
    result = 0
    for i in range(0,len(exp)):
        if exp[i]=="+" or exp[i]=="-":
            sign.append(exp[i-1])
            sign.append(exp[i])
            sign.append(exp[i+1])
        elif exp[i]=="*":
            sign.pop()
            num = int(exp[i-1])*int(exp[i+1])
            sign.append(str(num))
        elif exp[i]=="/":
            if len(sign)!=0:
                sign.pop()
            num = int(exp[i-1])//int(exp[i+1])
            sign.append(str(num))
    exp=""
    if "+" in sign or "-" in sign:
        for i in sign:
            exp+=i
        for i in range(0,len(sign)):
            if sign[i]=="+":
                num = int(sign[i-1])+int(sign[i+1])
                result+=num
            elif sign[i]=="-":
                num = int(sign[i-1])-int(sign[i+1])
                result+=num
        print(result)
    else:
        print(sign[0])
calculator()