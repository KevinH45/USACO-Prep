# Kevin Hwang, 2022
# http://www.usaco.org/index.php?page=viewproblem2&cpid=639
import sys
sys.stdin = open("diamond.in", "r")
sys.stdout = open("diamond.out", "w")
N, K = map(int, input().split())
sizes = []
for i in range(N):
    sizes.append(int(input()))
sizes = sorted(sizes)
cur_w = []
max_length = float("-inf")

for i in sizes:
    if not cur_w:
        cur_w.append(i)
        max_length = max(max_length, 1)
    else:
        cur_w.append(i)
        if cur_w[-1]-cur_w[0] > K:
            cur_w = [x for x in cur_w if cur_w[-1]-x <= K]
        else:
            max_length = max(max_length, len(cur_w)) 
print(max_length)
