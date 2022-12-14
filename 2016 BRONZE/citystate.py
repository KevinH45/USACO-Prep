import sys
sys.stdin = open("citystate.in", "r")
sys.stdout = open("citystate.out", "w")

n = int(input())
citystate = []

for i in range(n):
    inp = input().split()
    citystate.append((inp[0][0:2], inp[1]))

print(len(citystate)-len(set(citystate))//2+1)