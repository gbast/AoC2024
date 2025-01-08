import numpy as np

def rep(lista):
    return [[1 if e == '#' else 0 for e in s] for s in lista]



with open("d25.txt", "r") as file:

    input_text = file.read()
    
lock_keys = input_text.strip().split("\n\n")

cnt= len(lock_keys)
print(cnt)

locks = []
keys = []
for v in lock_keys:
    #input_data = [line.strip() for line in v.split("\n")]
    input_data=[list(x) for x in v.splitlines()]
    if input_data[0][0] == '#' and input_data[6][0] == '.':
        input_data.pop()
        input_data.pop(0)
        locks.append(rep(input_data))
    elif input_data[0][0] == '.' and input_data[6][0] == '#':
        input_data.pop()
        input_data.pop(0)
        keys.append(rep(input_data))


print(len(locks))
print("---------------------")


print(len(keys))
cnt_no = 0

for lock in locks: 
    sl = [sum(c) for c in zip(*lock)]

    for key in keys:
        ov = 0
        sk=[sum(c) for c in zip(*key)]
       
        for i in range(len(sk)):
           
            ov += 1 if sk[i]+sl[i]>5 else 0

        cnt_no += 1 if ov==0 else 0    
print(cnt_no)
                    