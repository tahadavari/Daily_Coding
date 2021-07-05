nunmber =[]
i=0
nunmber.append(int(input()))
while not nunmber[i]==0:
    i+=1
    nunmber.append(int(input()))
while i>0:
    print(nunmber[i-1])
    i-=1

