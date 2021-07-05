def ShowFibNth(n, m):
    print(m+n-m)
    if m-n==0:
        return 
    ShowFibNth(m-n,n)

ShowFibNth(int(input()), int(input()))

