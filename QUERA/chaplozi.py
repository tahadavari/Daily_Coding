number = int(input())
for i in range(0, 2*number+1):
    print(i)
    if i <= number:
        print(" "*(number-i) + "*"*(2*i+1))
    else:
        print(" "*(i-number)+"*"*((2*number-1)+number-i+1))
    
