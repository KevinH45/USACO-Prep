# Kevin Hwang, 2022
# http://www.usaco.org/index.php?page=viewproblem2&cpid=664

import sys
sys.stdin = open("blocks.in", "r")
sys.stdout = open("blocks.out", "w")

# Would use default dict
def get_letter_or_zero(table, letter):

    if letter in table:
        return table[letter]
    else:
        return 0

blocks = []
table = {}
alphabet = "abcdefghijklmnopqrstuvwxyz"
N = int(input())

for block in range(N):
    blocks.append(input().split())

for block in blocks:

    letter_set = set(block[0]+block[1])
    for i in letter_set:
        i_needed = max(block[0].count(i), block[1].count(i))
        if i in table: 
            table[i] += i_needed
        else:
            table[i] = i_needed

for l in alphabet:
    print(get_letter_or_zero(table, l))


