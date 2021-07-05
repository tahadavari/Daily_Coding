day = int(input())
SZ = [int(x)for x in input().split()]
sood = 0
index = 1
test = 0
for j in range(day):
    for i in range(j,day):
        test = sum(SZ[j:i+1])
        sood = test if test>sood else sood
    

print(sood)
