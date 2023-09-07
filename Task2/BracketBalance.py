flag=1
sequence=input("enter the sequence of brackets")
stack=[]
for i in range(len(sequence)-1,-1,-1):
    if(sequence[i]=='('and i==len(sequence)-1):
        flag=0
        break
    else:
        if(sequence[i]==')'):
            stack.append(')')
        elif(sequence[i]=='(' and len(stack)!=0):
            stack.pop()
        elif (sequence[i] == '(' and len(stack) == 0):
            flag=0
            break
if(len(stack)==0 and flag==1):
    print("yes")
elif(len(stack)!=0 or flag==0):
    print("no")