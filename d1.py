with open("d1.txt", "r") as file:
    # Read all lines from the file
    lines = file.readlines()

list1 = []
list2 = []

for line in lines:
    num1, num2 = map(int, line.split())
    list1.append(num1)
    list2.append(num2)

list1.sort(reverse=True)
list2.sort(reverse=True)
tot= sum(abs(list2[i]-list1[i]) for i in range(len(list1)))
print(f"tot=",tot)

##add for part 2
sim=sum(list2.count(x)*x for x in list1)
print(f"sim=",sim)