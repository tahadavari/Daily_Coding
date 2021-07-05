day = ["shanbe","1shanbe","2shanbe","3shanbe","4shanbe","5shanbe","jome"]
for i in range(3):
    Nday=int(input())
    days=[str (x) for x in input().split()]
    for name in days:
        if name in day:
            day.remove(name)
    days.clear()
print(len(day))

