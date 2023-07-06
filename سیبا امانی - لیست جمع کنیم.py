N=[] 
M=[] 
T=[] 
##list1 
while True: 
    num=int(input('add1')) 
    x=len(N) 
    if num==0: 
     
        break 
    N.append(num) 
for i in range(x): 
    x11=N[i] 
print(N) 
##list2 
while True: 
    num2=int(input('add2')) 
    x2=len(M) 
    if num2==0: 
        break 
    M.append(num2) 
for i2 in range(x2): 
    x22=M[i2] 
sumlist=[] 
for i in range(x,x2): 
     
    sum=x11+x22 
    sumlist.append(sum) 
print(sumlist)
