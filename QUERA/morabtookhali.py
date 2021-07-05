a, b = int(input()), int(input())
if a-b <= 0:
    print("Wrong order!")
elif ((a-b) % 2) !=0:
    print("Wrong difference!")
else:
    for i in range(int((a-b)/2)):
        print("* "*a)
    for i in range(b):
        print("* "*(int((a-b)/2))+" "*b+"* "*(int((a-b)/2)))
    for i in range(int((a-b)/2)):
        print("* "*a)
