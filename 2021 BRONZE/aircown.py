def findIncrease(curr, des):
    maxSub = -1
    maxRange = ()
    curRange = [0,0]
    index = 0
    for i,j in zip(curr,des):
        if i<j:
            curRange[1] += 1
        else:
            if maxSub < curRange[1]-curRange[0]:
                maxRange = curRange
                maxSub = curRange[1]-curRange[0]
            curRange = [index+1, index+1]
        index += 1
    return maxRange,maxSub

def findDecrease(curr, des):
    maxSub = -1
    maxRange = ()
    curRange = [0,0]
    index = 0
    for i,j in zip(curr,des):
        if i>j:
            curRange[1] += 1
        else:
            if maxSub < curRange[1]-curRange[0]:
                maxRange = curRange
                maxSub = curRange[1]-curRange[0]
            curRange = [index+1, index+1]
        index += 1
    return maxRange,maxSub

def findRange(curr, des):
    increaseRange, increaseNum = findIncrease(curr,des)
    decreaseRange, decreaseNum = findDecrease(curr,des)

    if increaseNum > decreaseNum:
        return increaseRange, "increase"
    return decreaseRange, "decrease"

def findNextStep(curr, des):
    rnge, typ = findRange(curr, des)
    startB, endB = rnge
    if typ == "increase":
        minIncrease = min([])


            

n = int(input())
curr = list(map(int, input().split()))
des = list(map(int, input().split()))

print(findDecrease(curr, des))
print(findIncrease(curr, des))



