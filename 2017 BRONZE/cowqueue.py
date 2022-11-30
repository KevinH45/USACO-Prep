# Kevin Hwang, 2022
# http://www.usaco.org/index.php?page=viewproblem2&cpid=713
import sys
sys.stdin = open("cowqueue.in", "r")
sys.stdout = open("cowqueue.out", "w")

N = int(input())
cows = []

for i in range(N):
    cows.append(tuple(map(int, input().split())))
cows = sorted(cows,reverse=True)
t = 0
while cows:
    arrive, need = cows.pop() 
    if t > arrive:
        t += need
    elif t <= arrive:
        t = arrive + need
print(t)
