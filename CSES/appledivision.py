n = int(input())
apples = list(map(int, input().split()))

def search(apples, sum1=0, sum2=0, index=0):

    if index >= len(apples):
        return abs(sum1-sum2)
    
    c1 = search(apples, sum1+apples[index], sum2, index+1)
    c2 = search(apples, sum1, sum2+apples[index], index+1)

    return min(c1,c2)

print(search(apples))
