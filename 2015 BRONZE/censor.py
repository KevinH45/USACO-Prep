# Kevin Hwang, 2022
# http://www.usaco.org/index.php?page=viewproblem2&cpid=526
import sys
sys.stdin = open("censor.in", "r")
sys.stdout = open("censor.out", "w")

# appending to the end of a list is O(1). inserting is O(n)
# we want to use a list of characters
# can we solve this problem by appending one character at a time
# "acocowwbc"
# X number of elements censoring
# 
# erasing from the end of list
# # O(1)
# buffer = [''] * 1000000
# index = 0
# index -= 10
# index += 1
# buffer[index] = newelement

s = input()
censor = list(input())

# executes L times
# N = len(s)/amount of characters > 10^6
# L depends on how many "cow" we can cram into S
# which is proportional to N. L is k*N
# O(N * L)  = O(N * k N) = O(N^2)
# O(N)
new_s = [''] * (10**6)
index = 0 # points to location of NEXT char
length_censor = len(censor)

# new_s[index-T:index]
for c in s:
    new_s[index] = c    
    index += 1
    p_removal = new_s[index-length_censor:index]
    if p_removal==censor:
        index -= length_censor

print(''.join(new_s[0:index]))
    
    