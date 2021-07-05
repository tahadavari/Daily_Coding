Ns, t = input().split()
Ns = int(Ns)
result = ["Yes"]*Ns
for i in range(Ns):
    code=input()
    for c in code:
        if not (c in t):
            result[i]="No"
            break
for i in result:
    print(i)


    
