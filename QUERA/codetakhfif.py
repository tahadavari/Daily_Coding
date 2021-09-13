num,valid = input().split()

valid = set(valid)
for i in range(int(num)):
    test = set(input())
    if valid == test:
        print('Yes')
    else :
        print('No')