N=[] 
M=[] 
while True: 
    num=int(input('add')) 
    N.append(num) 
    z=len(N) 
    if num==0: 
        break 
avg=sum(N)/len(N) 
for i in range(z): 
    if N[i]>avg: 
        M.append(N[i]) 
 
  
         
print(avg) 
print(M)
