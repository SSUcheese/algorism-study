color = ['black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'violet', 'grey', 'white']

col1= input()
col2 = input()
col3 = input()

temp1 = 0
temp2 = 0
temp3 = 0

for i in range(len(color)):
    if col1 == color[i]:
        temp1 = str(i)

for i in range(len(color)):
    if col2 == color[i]:
        temp2 = str(i)

for i in range(len(color)):
    if col3 == color[i]:
        temp3 = 10**i

print(int(temp1+temp2) * temp3)
