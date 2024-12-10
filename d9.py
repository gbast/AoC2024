import sys

with open("d9.txt", "r") as file:
    line = file.readline().strip()  

inpiut_data = [int(char) for char in line]

print(f"len input=",len(inpiut_data))

l=len(inpiut_data)
id=0
expanded = []

for i in range (0,l):
    if i%2:
        for r in range(0,inpiut_data[i]):
            expanded.append('')
        
    else:
        for r in range(0,inpiut_data[i]):
            expanded.append(id)
        id+=1
#print(expanded)
le=len(expanded)

e2= expanded[:]
left, right = 0, len(expanded) - 1

while left < right:
    if expanded[left] == '':  
        # Swap 
        expanded[left], expanded[right] = expanded[right], expanded[left]
        right -= 1  # Move leftward
    else:
        left += 1  # Move  rightward if no swap is needed

result = sum((int(x) if x != '' else 0) * i for i, x in enumerate(expanded))


print("res=",result)       

ebl =dict()
fbl =dict()
#part2


cnt = 1
idx = 0
cv=e2[0]
for i,v in enumerate(e2[1:],start=1):
    if v==cv:
        cnt+=1
    else:
        if cv=='':
            ebl[i-cnt]=cnt
        else:
            fbl[i-cnt]=cnt
        cv=v
        idx=i
        cnt=1
#  handle the last sequence after the loop
if cv == '':
    ebl[idx] = cnt
else:
    fbl[idx] = cnt
''' only for progess bar
lf=len(fbl)  
print(f'lf=',lf)
lp=1
'''
for key in sorted(fbl.keys(), reverse=True):
    ''' only for progess bar
    sys.stdout.write("\r%d" % int((lp)*100/lf) )
    sys.stdout.flush()
    lp+=1'''
    count_needed = fbl[key]
    for start_idx in sorted(ebl.keys()):
        if start_idx >= key:
            break
        if ebl[start_idx] >= count_needed:  
            # Swap 
            for y in range(count_needed):
                e2[key + y], e2[start_idx + y] = e2[start_idx + y], e2[key + y]

            # Update ebl 
            if ebl[start_idx] > count_needed:
                ebl[start_idx + count_needed] = ebl[start_idx] - count_needed
            del ebl[start_idx]

         
            break
            


result2 = sum((int(x) if x != '' else 0) * i for i, x in enumerate(e2))


print("res2=",result2)   