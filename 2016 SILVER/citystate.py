import sys
sys.stdin = open("citystate.in", "r")
sys.stdout = open("citystate.out", "w")

n = int(input())
citystate = []

for i in range(n):
    inp = input().split()
    citystate.append((inp[0][0:2], inp[1]))

state_map = {}

for i in citystate:

    if i[1] == i[0]:
        continue
    if i[1] in state_map:
        state_map[i[1]].append(i[0])
    else:
        state_map[i[1]] = [i[0]]

matches = 0
for city in citystate:

    n_city = city[0]
    n_state = city[1]

    if city[0] not in state_map:
        continue

    for j in state_map[n_city]:
        if n_state == j and n_city!=j:
            matches += 1

print(matches//2)


# MIAMI FL > MI FL
# FLINT MI > FL MI
# FLOOR MI > FL MI
# (MI, FL) > FLINT MI
# (MI, FL) > FLOOR MI
