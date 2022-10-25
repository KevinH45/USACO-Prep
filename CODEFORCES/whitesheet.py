# Kevin Hwang, 2022
# https://codeforces.com/contest/1216/problem/C


def findOverlapRange(r1, r2):
    a,b = r1
    c,d = r2
    lower = max(a,c)
    upper = min(b,d)
    if upper-lower>0:
        return (lower,upper)
    return None


def findOverlap(r1, r2):
    a,b = r1
    c,d = r2
    return max(0,min(b,d)-max(a,c))

wx1, wy1, wx2, wy2 = map(int, input().split())
ax1, ay1, ax2, ay2 = map(int, input().split())
bx1, by1, bx2, by2 = map(int, input().split())

axRange, ayRange = findOverlapRange((wx1, wx2), (ax1, ax2)), findOverlapRange((wy1, wy2), (ay1, ay2))
aOverlap = findOverlap((wx1, wx2), (ax1, ax2)) * findOverlap((wy1, wy2), (ay1, ay2))

bxRange, byRange = findOverlapRange((wx1, wx2), (bx1, bx2)), findOverlapRange((wy1, wy2), (by1, by2))
bOverlap = findOverlap((wx1, wx2), (bx1, bx2)) * findOverlap((wy1, wy2), (by1, by2))
totalArea = (wy2-wy1) * (wx2-wx1)

if aOverlap == 0:
    if bOverlap == 0:
        print("YES")
    else:
        # Only b overlaps
        if (totalArea - bOverlap) > 0:
            print("YES")
        else:
            print("NO")
elif bOverlap == 0:
    # Only a overlaps
    if (totalArea - aOverlap) > 0:
        print("YES")
    else:
        print("NO")
else:
    blackOverlap = findOverlap(axRange, bxRange) * findOverlap(ayRange, byRange)
    totalOverlap = aOverlap + bOverlap - blackOverlap
    if (totalArea - totalOverlap)>0:
        print("YES")
    else:
        print("NO")