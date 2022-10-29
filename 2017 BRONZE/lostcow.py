import sys
sys.stdin = open("lostcow.in", "r")
sys.stdout = open("lostcow.out", "w")

def inRange(start, stop, n):
    return start <= n and stop >= n

x, y = map(int, input().split())
dist = 0
n_interval = 1
c_pos = x
# While cow not found
while (n_interval < 0 and not inRange(x, c_pos, y)) or (n_interval > 0 and not inRange(c_pos, x, y)) : 
    dist += abs(c_pos - (x+n_interval))
    c_pos = x+n_interval
    n_interval*=-2
dist -= abs(c_pos-y)
print(dist)