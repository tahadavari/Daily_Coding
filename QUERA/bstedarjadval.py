# link : https://quera.ir/problemset/contest/106797/
# cc4

from math import sqrt


def is_prime(number):
    prime_flag = 0

    if(number > 1):
        for i in range(2, int(sqrt(number)) + 1):
            if (number % i == 0):
                prime_flag = 1
                break
        if (prime_flag == 0):
            return True
        else:
            return False
    else:
        return False


def location(now: tuple, matrix: list, n, m, k):
    number = matrix[now[0]-1][now[1]-1]
  

    if k == 0:
        return now

    elif is_prime(number):
      
        now = (n-now[0]+1, m-now[1]+1)
       

    else:
        divide_4 = number % 4

        if divide_4 == 0:
            x = now[1]+1
            if x > m:
                now = (now[0], 1) 
            else:
                now = (now[0], x)

        elif divide_4 == 1:
            y = now[0]+1
            if y > n:
                now = (1, now[1]) 
            else:
                now = (y, now[1])

        elif divide_4 == 2:
            x = now[1]-1
            if x < 1:
                now = (now[0], m)
            else:
                now = (now[0], x)

        elif divide_4 == 3:
            y = now[0]-1
            if y < 1:
                now = (n, now[1])
            else:
                now = (y, now[1])

    return location(now, matrix, n, m, k-1)


n, m, k = map(int, input().split())

matrix = [0 for i in range(n)]

for i in range(n):
    row = list(map(int, input().split()))
    matrix[i] = row

x = location((1, 1), matrix, n, m, k)

print(x[0], x[1])
