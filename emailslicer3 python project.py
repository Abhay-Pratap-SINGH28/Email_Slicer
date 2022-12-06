a=int(input("Enter Number of Email Id:-"))
l=[]
for i in range(0,a):
    e=input("Enter Email Id:-")
    l.append(e)
for i in l:
    s=""
    s1=""
    for j in i:
        if j=='@':
            break
        else:
            s=s+j
    r=i[::-1]
    r=r.upper()\

    for j in r:
        if j=='@':
            break
        else:
            s1=s1+j
    #print('User Name:',s,'and Domain:',s1[::-1])
    print('User Name:',s)
    print('Domain:',s1[::-1])