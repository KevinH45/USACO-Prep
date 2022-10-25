# Kevin Hwang, 2022
# http://www.usaco.org/index.php?page=viewproblem2&cpid=891

import sys

sys.stdin = open("shell.in", "r")
sys.stdout = open("shell.out", "w")

N = int(input())
game = [1,2,3]
score = [0,0,0]

for i in range(N):
    a, b, g = map(int, input().split())
    a -= 1
    b -= 1
    g -= 1
    game[a], game[b] = game[b], game[a]
    score[game[g]-1] += 1

print(max(score))
