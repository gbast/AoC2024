import re

def parsemul(inp):
    regex = r"mul\((\d{1,3}),(\d{1,3})\)"
    return re.finditer(regex, inp, re.MULTILINE)

# Open the file in read mode
with open("d3.txt", "r") as file:
    # Read all lines from the file
    lines = file.readlines()

# Strip whitespace characters like '\n' and print each line
input_s = ''.join(line.strip() for line in lines)

jinput=input_s.replace('\n','')


res=sum(int(m.group(1))*int(m.group(2)) for m in parsemul(jinput))
print(f"res=",res)

#aad part 2
regexp2m = r"^(.*?)don't\(\)|do\(\)(.*?)don't\(\)"
#for m in re.finditer(regexp2, input, re.MULTILINE):
 #   print(m.group(0))
j = "".join(m.group(0) for m in re.finditer(regexp2m, jinput, re.MULTILINE))
#print(f"J=",j)
res2=sum(int(m.group(1))*int(m.group(2)) for m in parsemul(j))
print(f"res2=",res2)
