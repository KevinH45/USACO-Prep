import sys
from collections import defaultdict
sys.stdin = open("circlecross.in", "r")
sys.stdout = open("circlecross.out", "w")


def in_range(n, lower, upper):
    return lower <= n and upper>= n
    
def c_length(a,b,c,d):
    if in_range(a, c, d) and in_range(b, c, d):
        return 0
    elif in_range(c, a, b) and in_range(d, a, b ):
        return 0
    return max(min(b,d)-max(a,c),0)

s = input()

c_map = defaultdict(lambda: [])
for i in range(len(s)):
    c_map[s[i]].append(i)
c_arr = []
for i,j in c_map.items():
    c_arr.append(j)

count = 0
for i in range(len(c_arr)):
    for j in range(i+1, len(c_arr)):
        if c_length(c_arr[i][0], c_arr[i][1], c_arr[j][0], c_arr[j][1]) > 0:
            count +=1

print(count)
