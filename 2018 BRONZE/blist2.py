# Kevin Hwang, 2022
# http://www.usaco.org/index.php?page=viewproblem2&cpid=856
#
# 3
# 4 10 1
# 8 13 3
# 2 6 2
#
# 2: needs 2
# 4 a cow needs 1 bucket
# 6: gives back 2: need -2
# 8 : needs 3
# 10 a cow gives back 1 buckt
# 13: gives back 3

import sys
sys.stdin = open("blist.in", "r")
sys.stdout = open("blist.out", "w")

req_list = []
# list of tuples (time,buckets needed)
evt_list = []
n = int(input())
for i in range(n):
    start, end, buckets = map(int, input().split())
    evt_list.append((start, buckets))
    evt_list.append((end, -buckets))
# sorting a list of strings, of tuples the same length, tuples different lengths
# "foo" < "goo"
# "foo" < "food"
# (1, 3) < (2, 3)
# (1, 2) < (1, 3)
# (1, 3) < (1, 3, 5)
evt_list = sorted(evt_list)
maxBuckets = float("-inf")
acc = 0
for i in evt_list:
    acc += i[1]
    maxBuckets = max(acc, maxBuckets)
print(maxBuckets)


