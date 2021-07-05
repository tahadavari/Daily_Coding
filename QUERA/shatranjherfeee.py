numbers = [int (x) for x in input().split()]
shatrang = [1,1,2,2,2,8]
for i in range(6):
    print(shatrang[i]-numbers[i],end=" ")
