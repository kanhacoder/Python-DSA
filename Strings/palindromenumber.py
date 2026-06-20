number = int(input("Enter any integer: "))
if number>0:
    numstr = str(number)
    numstr = numstr[::-1]
    numstr = int(numstr)
    if numstr>2**31:
        print(2**31)
    if numstr<-2**31:
        print(-2**31)
    if numstr == number:
        print(True)
    else:
        print(False)
else:
    print(False)