import sys
sys.stdin = open("triangles.in", "r")
sys.stdout = open("triangles.out", "w")

def check_valid(coord1, coord2, coord3):
    x1, y1 = coord1
    x2, y2 = coord2
    x3, y3 = coord3
    return (x1==x2 or x2==x3 or x1==x3) and (y1==y2 or y2==y3 or y1==y3) and not(coord1==coord2 or coord2==coord3 or coord1==coord3)

N = int(input())
posts = []
for i in range(N):
    posts.append(tuple(map(int,input().split())))
max_area = float("-inf")

for i in range(len(posts)):

    for j in range(i+1, len(posts)):

        for k in range(j+1, len(posts)):
            x1, y1 = posts[i]
            x2, y2 = posts[j]
            x3, y3 = posts[k]

            if check_valid(posts[i], posts[j], posts[k]):
                max_area = max(max_area,
                    ((max(x1,x2,x3)-min(x1,x2,x3))* 
                    (max(y1,y2,y3)-min(y1,y2,y3))))
print(max_area)
