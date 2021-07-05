x1, y1, x2, y2 = input().split()
x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
status = "Try again"
if x1 == x2:
    status = "Vertical"
elif y1 == y2:
    status = "Horizontal"
print(status)
