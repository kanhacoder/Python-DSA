bracket = input("Enter paranthesis: ")
stack = []
for i in bracket:
    if i=="(" or i=="{" or i=="[":
        stack.append(i)
        #print(i)
    if i==")" and stack[len(stack)-1]=="(":
         stack.pop()
    elif i=="}" and stack[len(stack)-1]=="{":
         stack.pop()
    elif i=="]" and stack[len(stack)-1]=="[":
         stack.pop()
if len(stack)==0:
    print("Balanced")
else:
    print("Not balanced")


'''
(({]))

({)}

'''

# bracket = input("Enter paranthesis: ")
# st = []
# t =-1

# for c in bracket:
#     if(c=='(' or c=='{' or c=='['):
#         st.append(c)
#         t+=1
#     elif not st:
#         print("Not Balanced")
#         break
#     else:
#         if c==')' and st[t] == '(':
#             st[t]=None
#             t-=1
        