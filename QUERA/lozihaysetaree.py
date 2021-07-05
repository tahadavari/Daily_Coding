import math
number = int(input())
space1=math.floor((number/2))
space2=number-1
for setare in range(1,number+1):
    if setare < math.ceil(number/2):
        # for setare in range(math.ceil(number/2)):
        print(" "*(space1-setare+1)+"*"*(2*(setare-1)+1)+" "*(space2-((setare-1)*2))+"*"*(2*(setare-1)+1))
    elif setare == math.ceil(number/2):
        print("*"*(number*2))
    else:
        print(" "*(setare-space1-1)+"*"*(2*((number+1-setare)-1)+1)+" "*(space2-(((number+1-setare)-1)*2))+"*"*(2*((number+1-setare)-1)+1))



