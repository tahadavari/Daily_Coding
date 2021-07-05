a,b,l=input().split()
a,b,l,time=int(a),int(b),int(l),0
for i in range(1,l+1):
    if i%2==0:
        time+=b
    else:
        time+=a
print(time)
