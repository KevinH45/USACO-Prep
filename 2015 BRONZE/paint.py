# Kevin Hwang, 2022
# http://www.usaco.org/index.php?page=viewproblem2&cpid=567
import sys
sys.stdin = open("paint.in", "r")
sys.stdout = open("paint.out", "w")
a, b = map(int, input().split())
c, d = map(int, input().split())
#    0   1   2   3   4   5   6   7   8   9  10  11  12
#                                        c           d
#                    a               b
#
#        |       |
#                                    |      |
# 
# write code to find the overlap
# a or c is never involved in the maximum
# b or d is never the minimum
lower = max(a,c)
upper = min(b,d)
overlap = upper-lower
# total = d - c + b - a - overlap # not  quite correct : correct if there is an overlap
total = d - c + b - a - max(overlap,0)
# painted = 0
# for i in range(100):
#     if (a<=i and i<b) or (c<=i and i<d):
#         painted += 1
print(total)