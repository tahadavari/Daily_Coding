z1,z2,z3=input().split()
z1,z2,z3=float(z1),float(z2),float(z3)
status="No"
if z1>0 and z2>0 and z3>0:
    status = "Yes" if z1+z2+z3==180 else "No"
print(status)


