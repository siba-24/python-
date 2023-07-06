list=[] 
list1=[] 
while True: 
    num=int(input('add')) 
    list.append(num) 
    if num==0: 
        break 
    T=len(list) 
    for i in range(T): 
        x=list[i] 
        if x in list1: 
            continue 
        list1.append(x) 
print('tedad',x,'is:',list.count(x)) 
print(list1)
