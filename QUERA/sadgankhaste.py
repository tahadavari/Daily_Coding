def reverse_number(num):
    result = num % 10
    num //= 10
    while num>0:
        result = (num % 10)+(result*10)
        num //= 10

    return result


x, y = int(input()), int(input())
if x == y:
    print(f"{x} = {y}")
else:
    print(reverse_number(min(reverse_number(x), reverse_number(y))),
          "<", reverse_number(max(reverse_number(x), reverse_number(y))))
