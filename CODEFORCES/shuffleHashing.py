# Kevin Hwang, 2022
# https://codeforces.com/contest/1278/problem/A
from collections import Counter
 
def equal(p, subset):
    return Counter(p) == Counter(subset)
    
t = int(input())
# O(N^2)
# Where N is length of P
# Where M is length of H
# M is typically k * N , k < 1
# O(N kN)
# O(N^2)
for i in range(t):
    p = input()
    h = input()
 
    if len(h) < len(p):
        print("NO")
    else:
        found = False
        left = 0
        right = len(p)
 
        while right<=len(h):
            subset = h[left:right]
            if equal(p, subset):
                found = True
                break
            right+=1
            left +=1
 
        if found:
            print("YES")
        else:
            print("NO")