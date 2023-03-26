lst = [0,0,0,0,0]
c = 0
for i in range (len(lst)):
    if lst[i] == 0:
        lst[i] = 1
        c += 1
    else:
        continue
    
    for j in range (i+1, len(lst)):
        if lst[j] == 1:
            lst[j] = 0
        elif lst[j] == 0:
            lst[j] = 1

            
        
print(lst)
print(c)
