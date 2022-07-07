from sys import stdin
l1 = list(map(int, stdin.readline().split()))
l2 = list(map(int, stdin.readline().split()))

[x1, y1, x2, y2] = l1
[x3, y3, x4, y4] = l2

[mx1, my1, mx2, my2] = [min(l1[0], l1[2]), min(l1[1], l1[3]), max(l1[0], l1[2]), max(l1[1], l1[3])]
[mx3, my3, mx4, my4] = [min(l2[0], l2[2]), min(l2[1], l2[3]), max(l2[0], l2[2]), max(l2[1], l2[3])]


def ccw(x1, y1, x2, y2, x3, y3):
    return (x2-x1)*(y3-y1) - (y2-y1)*(x3-x1)

ccw123 = ccw(x1, y1, x2, y2, x3, y3)
ccw124 = ccw(x1, y1, x2, y2, x4, y4)
ccw341 = ccw(x3, y3, x4, y4, x1, y1)
ccw342 = ccw(x3, y3, x4, y4, x2, y2)

if ccw123*ccw124 == 0 and ccw341*ccw342 == 0:
    if mx1 <= mx4 and mx3 <= mx2 and my1 <= my4 and my3 <= my2: print(1)
    else: print(0)
else:
    if ccw123*ccw124 <= 0 and ccw341*ccw342 <= 0:print(1)
    else: print (0)