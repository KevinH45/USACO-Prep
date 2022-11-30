import sys
sys.stdin = open("angry.in", "r")
sys.stdout = open("angry.out", "w")

n = int(input())
bales = []
for i in range(n):
    bales.append(int(input()))
bales = sorted(bales)

def goRight(index):
    lastIndex = index
    radius = 1

    while True:
        lastPos = bales[lastIndex]
        saveIndex = lastIndex

        while lastIndex < n and bales[lastIndex] <= (lastPos + radius): # lastIndex == lastPos + radius
            lastIndex += 1

        lastIndex -= 1
        radius += 1

        if saveIndex == lastIndex:
            return lastIndex - index + 1
        if lastIndex+1 == n:
            return lastIndex - index +1
        
def goLeft(index):
    lastIndex = index
    radius = 1

    while True:
        lastPos = bales[lastIndex]
        saveIndex = lastIndex

        while lastIndex >= 0 and bales[lastIndex] >= (lastPos - radius):
            lastIndex -= 1
        lastIndex += 1
        radius += 1
        if saveIndex == lastIndex:
            return index - lastIndex + 1
        if lastIndex-1 < 0:
            return index + 1

max_expl = float("-inf")
# print(bales)
for i in range(len(bales)):

    # print(f"######{i}######")
    # print(goRight(i))
    # print(goLeft(i))
    # print(goRight(i)+goLeft(i))
    
    max_expl = max(max_expl, goRight(i)+goLeft(i)-1)

print(max_expl)


