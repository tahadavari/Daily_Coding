Nesm = int(input())
Chois_name = ""
lenname = 0
for i in range(Nesm):
    name = input()
    if len(set(name)) > lenname:
        lenname = len(set(name))
        Chois_name = name
    elif len(set(name)) == lenname:
        if len(name)-len(set(name))==0:
            lenname = len(set(name))
            Chois_name = name
print(lenname)
