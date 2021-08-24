# link : https://quera.ir/problemset/contest/26110/
# cc8

from math import sqrt
def two_point(l : tuple)->int:
    d = sqrt(((0-l[0])**2)+((0-l[1])**2))
    return d

def score(d : float)->int:
    shot_score = 0
    if d <= 10 :
        shot_score = 10
    elif 10 < d <= 30:
        shot_score = 9
    elif 30 < d <= 50:
        shot_score = 8
    elif 50 < d <= 70:
        shot_score = 7
    elif 70 < d <= 90:
        shot_score = 6
    elif 90 < d <= 110:
        shot_score = 5
    elif 110 < d <= 130:
        shot_score = 4
    elif 130 < d <= 150:
        shot_score = 3
    elif 150 < d <= 170:
        shot_score = 2
    elif 170 < d <= 190:
        shot_score = 1
    else : 
        shot_score = 0
    return shot_score



shot = int(input())
point = 0
for l in range(shot):
    location = tuple(map(int,input().split()))
    point += score(two_point(location))

print(point)