import math
num = int(input())
numCopy = num
for i in range(math.ceil((num-1)/4)):
    num -= 4
mabda = [1, 0] if num == -2 else [0, 0]
if num == -1:
    for i in range(math.ceil(numCopy/4)):
        mabda[0] += 1
        mabda[1] += 1

elif num == 0:
    for i in range(math.ceil(numCopy/4)):
        mabda[0] -= 1
        mabda[1] += 1


elif num == 1:
    for i in range(math.floor(numCopy/4)):
        mabda[0] -= 1
        mabda[1] -= 1

else:

    for i in range(math.floor(numCopy/4)):
        mabda[0] += 1
        mabda[1] -= 1

print(mabda[0], mabda[1])
