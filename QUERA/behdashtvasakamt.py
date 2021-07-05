nomre,day=int(input()),int(input())
if day==0:
    print(20)
elif day == 7:
    print(nomre)
else:
    print(0) if (nomre-day)<=0 else print(nomre - day)
