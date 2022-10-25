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

def findOverlapRange(r1, r2):
    a,b = r1
    c,d = r2
    lower = max(a,c)
    upper = min(b,d)
    if upper-lower>0:
        return (lower,upper)
    return None

def fullyCovers(r1, r2):
    # Does r1 fully cover an axis of r2?
    if not (r1 and r2):
        return False
    a,b = r1
    c,d = r2
    return (a<=c and b>=d)

def inRange(r1, r2):
    a,b = r1
    c,d = r2
    return (a>c and b<d)

ax1, ay1, ax2, ay2 = map(int, input().split())
bx1, by1, bx2, by2 = map(int, input().split())

overlap = findOverlap((bx1,bx2), (ax1, ax2)) * findOverlap((by1,by2), (ay1,ay2))
totalArea = (ax2-ax1) * (ay2-ay1)

xOverlapRange = findOverlapRange((bx1,bx2), (ax1, ax2))
yOverlapRange = findOverlapRange((by1,by2), (ay1,ay2))

if fullyCovers(xOverlapRange, (ax1,ax2)) and not inRange(yOverlapRange, (ay1, ay2)):
    print(totalArea-overlap)
elif fullyCovers(yOverlapRange, (ay1, ay2)) and not inRange(xOverlapRange, (ax1, ax2)):
    print(totalArea-overlap)
else:
    print(totalArea)

