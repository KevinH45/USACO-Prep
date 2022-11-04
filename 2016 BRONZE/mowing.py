# Kevin Hwang, 2022
# http://www.usaco.org/index.php?page=viewproblem2&cpid=593
import sys
sys.stdin = open("mowing.in", "r")
sys.stdout = open("mowing.out", "w")

def stringify(entry):
    return f"{entry[0]},{entry[1]}"
    
N = int(input())
directions = []

for i in range(N):
    directions.append(input().split())
    directions[-1][1] = int(directions[-1][1])

t = float("inf")
cur_t = 0
cells = {"0,0":0}
cur = [0,0]

for j in directions:

    direction = j[0]
    unit = j[1]

    for i in range(unit):
        cur_t += 1
        if direction == "N": cur[1] += 1
        elif direction == "W": cur[0] -= 1
        elif direction == "E": cur[0] += 1
        elif direction == "S": cur[1] -= 1
        
        key_cur = stringify(cur)
        if key_cur in cells:
            t = min(t, cur_t-cells[key_cur])
        cells[key_cur] = cur_t

if t == float("inf"):
    print(-1)
else:
    print(t)