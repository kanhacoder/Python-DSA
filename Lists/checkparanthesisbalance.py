# ()()()(((((((())))))))
# ((())())
def check():
    stack = input("Enter paranthesis: ")
    z = False
    op = 0
    #cl = 0
    if stack[0]=="(":
        z = True
        op+=1
    elif stack[0]==")":
        print("Not balanced")
        return
    if z:
        for i in range (1,len(stack)):
            if stack[i]==")":
                op-=1
            else:
                op+=1
    if op==0:
        print("Balanced")
    else:
        print("Not balanced")
check()

# (((((())))
'''
(({]))

({)}


}
{()}
'''