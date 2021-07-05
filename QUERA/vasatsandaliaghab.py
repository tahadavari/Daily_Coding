name = [0,0,0,0]
m = [0,0,0,0]
for i in range(4):
    name[i], m[i] =input().split()
if m.count("R") == 2:
    print(name[m.index("R")])
elif m.count("L") == 2:
    print(name[m.index("L")])
else:
    name.pop(m.index("U"))
    print(name[1])