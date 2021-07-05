n, m = input().split()
n, m = int(n), int(m)

matrix = [list(map(int, input().split())) for i in range(n)]
count=0
for i in range(1, n-1):
    for j in range(1, m-1):
        if((matrix[i][j] > matrix[i][j-1] and matrix[i][j] > matrix[i][j+1] and
            matrix[i][j] < matrix[i-1][j] and matrix[i][j] < matrix[i+1][j]) or (matrix[i][j] < matrix[i][j-1] and matrix[i][j] < matrix[i][j+1] and
                                                                                 matrix[i][j] > matrix[i-1][j] and matrix[i][j] > matrix[i+1][j])):
            count+=1
print(count)