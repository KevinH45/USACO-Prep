import sys
sys.stdin = open("traffic.in", "r")
sys.stdout = open("traffic.out", "w")

N = int(input())

lower_n, upper_n = float('-inf'), float("inf")
lower_prev, upper_prev = None, None
altered = False

prevRamps = []

for i in range(N):
    type_road, mini, maxi = input().split()
    mini, maxi = int(mini), int(maxi)

    if type_road == "on":

        if lower_n == float("-inf"):
            prevRamps.append((-mini, -maxi))
            continue   
        if not altered:
            lower_prev, upper_prev = lower_n, upper_n
            altered = True
        lower_n += mini
        upper_n += maxi

    elif type_road == "off":

        if lower_n == float("-inf"):
            prevRamps.append((maxi, mini))
            continue     
        if not altered:
            lower_prev, upper_prev = lower_n, upper_n
            altered = True
        lower_n -= maxi
        upper_n -= mini
    else:
        lower_n = max(mini, lower_n)
        upper_n = min(maxi, upper_n)


for i in prevRamps[::-1]:
    lower_prev += i[0]
    upper_prev += i[1]

if not altered:
    lower_prev, upper_prev = lower_n, upper_n

print(lower_prev, upper_prev)
print(lower_n, upper_n)
