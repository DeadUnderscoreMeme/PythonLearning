a = [0]
i=0
for i in range(i,100):
    print(i)
    a.append(i)

total = 0
j = 0

for i in a:
    for j in range(1,i+1):
        total += j
    print("Sum upto {} : {}".format(i,total))
    total = 0

