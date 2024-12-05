def check(rep):
    x = len(rep)
    is_inc=all(rep[i]>rep[i-1] for i in range(1,x))
    is_dec=all(rep[i]<rep[i-1] for i in range(1,x))
    v=all(1<=abs(rep[i]-rep[i-1])<=3 for i in range(1,x))

    return ((is_inc or is_dec) and v)*1



with open("d2.txt", "r") as file:
    # Read all lines from the file
    lines = file.readlines()

lis=[list(map(int, line.split())) for line in lines]

print(f"count=",sum(check(rep) for rep in lis)) 

#add on part 2
cnt = 0
for rep in lis:
    if check(rep):
        cnt+=1
    else:
        for i in range(len(rep)):
            mrep = rep[:i]+rep[i+1:]
            if check(mrep):
                #print(f"o=",rep," m=",mrep)
                cnt+=1
                break
                
print(f"cntmodif=",cnt) 