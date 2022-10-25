instr=input()
instr=instr.split('/')
num=instr[0]
deno=[]
if(len(instr)>1):
    deno=instr[1]
denominator=[]
numerator=[]
flag=0
lst=['1','x','0']
for i in range(len(num)):
    if(num[i]=='^'):
        if(flag==0):
            flag=1
        else:
            flag=0
        continue
    if(num[i]=='x'):
        if(i==len(num)-1):
            continue
        if(num[i+1]=='^'):
            continue
        else:
            lst[2]='1'
            continue
    if num[i]=='+' or num[i]=='-':
        lst[2]=str(int(lst[2]))
        if(lst[0]!='1'):
            lst[0]=lst[0][1:len(lst[0])]
        numerator.append(lst)
        numerator.append(num[i])
        flag=0
        lst=['1','x','0']
    else:
        if(i==0):
            if(num[i]=='x'):
                continue
        if(flag==0):
            lst[0]+=num[i]
        else:
            lst[2]+=num[i]
lst[2]=str(int(lst[2]))
if(lst[0]!='1'):
    lst[0]=lst[0][1:len(lst[0])]
numerator.append(lst)
lst=[]

derivative=[]

for i in range(len(numerator)):
    if(len(numerator[i])==1):
        derivative.append(numerator[i])
        continue
    elif(numerator[i][2]=='0'):
        if(len(derivative)==0):
            continue
        derivative.pop()
        continue
    elif(numerator[i][2]=='1'):
        numerator[i].pop()
        numerator[i].pop()
        derivative.append(numerator[i])
    else:
        numerator[i][0]=str(int(numerator[i][0])*int(numerator[i][2]))
        numerator[i][2]=str(int(numerator[i][2])-1)
        derivative.append(numerator[i])

numerator=derivative

if(len(numerator)==0):
    print(0)
elif(len(numerator)==1):
    if(len(numerator[0])==1):
        print(numerator[0][0],end='')
    else:
        if(numerator[0][2]=='1'):
            print(f'{numerator[0][0]}{numerator[0][1]}',end='')
        else:
            print(f'{numerator[0][0]}{numerator[0][1]}^{numerator[0][2]}',end='')
else:
    for i in range(len(numerator)):
        if(len(numerator[i])==1):
            print(numerator[i][0],end='')
        else:
            if(numerator[i][2]=='1'):
                print(f'{numerator[i][0]}{numerator[i][1]}',end='')
            else:
                print(f'{numerator[i][0]}{numerator[i][1]}^{numerator[i][2]}',end='')
