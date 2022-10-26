# Kevin Hwang, 2022
# http://www.usaco.org/index.php?page=viewproblem2&cpid=917
# O(N) solution
import sys
sys.stdin = open("traffic.in", "r")
sys.stdout = open("traffic.out", "w")

N = int(input())
lower_n, upper_n = 0, float("inf")
roads = []

for i in range(N):
    type_road, mini, maxi = input().split()
    roads.append((type_road, int(mini), int(maxi)))


for t in roads:
    type_road, mini, maxi = t
    
    if type_road == "on":
        lower_n += mini # lower_n > 0, does have an effect
        upper_n += maxi

    elif type_road == "off":
        lower_n = max(0, lower_n-maxi)
        # somewhere that mini > upper_n? 
        upper_n -= mini
    else:
        lower_n = max(mini, lower_n)
        upper_n = min(maxi, upper_n)

lower_p, upper_p = 0, float("inf")
for t in roads[::-1]:
    type_road, mini, maxi = t
    
    if type_road == "off":
        lower_p += mini # lower_n > 0, does have an effect
        upper_p += maxi

    elif type_road == "on":
        lower_p = max(0, lower_p-maxi)
        # somewhere that mini > upper_n? 
        upper_p -= mini
    else:
        lower_p = max(mini, lower_p)
        upper_p = min(maxi, upper_p)

print(lower_p, upper_p)
print(lower_n, upper_n)
