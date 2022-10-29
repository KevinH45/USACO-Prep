# Kevin Hwang, 2022
# http://www.usaco.org/index.php?page=viewproblem2&cpid=616

import sys

sys.stdin = open("cbarn.in", "r")
sys.stdout = open("cbarn.out", "w")

min_dist = float("inf")
N = int(input())
cows = []

for i in range(N):
    cows.append(int(input()))

for entry in range(N):
  total_dist = 0
  for room in range(N):
    dist = room - entry
    if dist < 0:
      dist = (N - entry) + room
    total_dist += dist * cows[room]
  min_dist = min(total_dist, min_dist)

print(min_dist)