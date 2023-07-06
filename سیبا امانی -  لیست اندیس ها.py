N=int(input('tedad')) 
list=[] 
for i in range(N): 
    num=int(input('number')) 
    list.append(num) 
andis=[] 
m=int(input('add vared shode karbar')) 
for i in range(len(list)): 
    if list[i] ==m: 
        andis.append(i) 
print(andis)
