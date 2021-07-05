def mostafa(x:int)->str:
    # c=0
    for i in range(x-30,x):
        # c+=1
        ii = sum(list(map(int,list(str(i)))))
        if ii+i==x:
            # print(c)
            return "Yes"
        
    return "No"


testcase=int(input())
result = []
while testcase>0:
    number=int (input())
    result.append(mostafa(number))
    testcase-=1

print(*result,sep="\n")