N = int(input())
weights = sorted(list(map(int,input().split())))
groups = []
min_i = float("inf")
for i in range(len(weights)):

    for j in range(i+1, len(weights)):
        tmp = [y for x,y in enumerate(weights) if x not in (i,j)]
        cur_i = 0
        for z in range(len(tmp)):
            if z%2==0:
                subset = tmp[z:z+2]
                cur_i += abs(subset[0]-subset[1])
        min_i = min(cur_i, min_i)
print(min_i)