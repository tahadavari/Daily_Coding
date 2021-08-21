# link : https://quera.ir/problemset/contest/82378/

masraf = int(input())
l_1500 = int(input()) + 60
if masraf > l_1500:
    print((l_1500*1500)+((masraf-l_1500)*3000))
else:
    print(masraf*1500)
