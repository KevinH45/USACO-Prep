# Kevin Hwang, 2022
# http://www.usaco.org/index.php?page=viewproblem2&cpid=759

import sys

sys.stdin = open("billboard.in", "r")
sys.stdout = open("billboard.out", "w")

def findOverlap(r1,r2):
    a,b = r1
    c,d = r2
    overlap = min(b,d) - max(a,c)
    return max(overlap,0)
   
def findArea(p1,p2):
    x1,y1 = p1
    x2,y2 = p2
    return (y2-y1)*(x2-x1)

ax1, ay1, ax2, ay2 = map(int, input().split())
bx1, by1, bx2, by2 = map(int, input().split())
tx1, ty1, tx2, ty2 = map(int, input().split())

truckXRange = (tx1, tx2)
truckYRange = (ty1, ty2)
aOverlap = findOverlap(truckXRange, (ax1, ax2)) * findOverlap(truckYRange, (ay1,ay2))
bOverlap = findOverlap(truckXRange, (bx1, bx2)) * findOverlap(truckYRange, (by1,by2))
overlap = aOverlap + bOverlap
totalArea = findArea((ax1,ay1), (ax2, ay2)) + findArea((bx1,by1), (bx2, by2))
print(max(0, totalArea-overlap))
