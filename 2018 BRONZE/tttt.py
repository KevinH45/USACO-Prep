# Kevin Hwang, 2022
# http://www.usaco.org/index.php?page=viewproblem2&cpid=831
import sys
sys.stdin = open("tttt.in", "r")
sys.stdout = open("tttt.out", "w")

def get_options(table):
    options = []
    options.append(list(table[0]))
    options.append(list(table[1]))
    options.append(list(table[2]))
    options.append([x[0] for x in table])
    options.append([x[1] for x in table])
    options.append([x[2] for x in table])
    options.append([table[0][0], table[1][1], table[2][2]])
    options.append([table[2][0], table[1][1], table[0][2]])
    return options

line1 = input()
line2 = input()
line3 = input()

one_team = []
two_team = []

for option in get_options([line1,line2,line3]):
    cows = len(set(option))
    if cows==1:
        one_team.append(option[0])
    elif cows==2:
        two_team.append(''.join(set(option)))

print(len(set(one_team)))
print(len(set(two_team)))