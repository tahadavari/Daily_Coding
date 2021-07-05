number = map(int,input())


# number = int(numberS)
# while(number >= 10):
#     numberS = str(number)
#     number = 0
#     for num in numberS:
#         number += int(num)
# print(number)

while True:
    if number/10 >= 1:
        number=sum(number)

print(number)
