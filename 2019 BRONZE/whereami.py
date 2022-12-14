import sys
sys.stdin = open("whereami.in", "r")
sys.stdout = open("whereami.out", "w")

n = int(input())
s = input()

def is_unique(left, right, s):
    seen = set()
    while right <= n:

        sub = s[left:right]

        if sub in seen:
            return False
        
        seen.add(sub)
        left += 1
        right += 1
    return True

min_possible = None
for i in range(0, n):

    left = 0
    right = i
    if is_unique(left, right, s):
        min_possible = i
        break

print(min_possible)
