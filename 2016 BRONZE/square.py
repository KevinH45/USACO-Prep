import sys
sys.stdin = open("square.in", "r")
sys.stdout = open("square.out", "w")

ax1, ay1, ax2, ay2 = map(int, input().split())
bx1, by1, bx2, by2 = map(int, input().split())

lCorner = (min(ax1,bx1), min(ay1, by1))
uCorner = (max(ax2, bx2), max(ay2, by2))
sideLength = max(uCorner[1] - lCorner[1], uCorner[0] - lCorner[0])
print(sideLength*sideLength)