N = int(input())
weights = sorted(list(map(int,input().split())))
groups = []
min_i = float("inf")
for i in range(len(weights)):

    for j in range(i+1, len(weights)):
        cur_i = 0
        z = 0
        while z < len(weights):
            if z==i or z==j:
                z+=1
                continue
            p_z = z
            z+=1
            while z==i or z==j:
                z+=1

            if z>=len(weights):
                break
            cur_i += abs(weights[p_z]-weights[z])
            z+=1
        min_i = min(cur_i, min_i)
print(min_i)