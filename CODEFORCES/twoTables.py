# Kevin Hwang, 2022
# https://codeforces.com/problemset/problem/1555/B

N = int(input())

for i in range(N):
    boxWidth, boxLength = map(int, input().split())
    x1, y1, x2, y2 = map(int, input().split())
    newTableWidth, newTableLength = map(int, input().split())
    tableWidth, tableLength = x2-x1, y2-y1

    # If there is no overlap, then the result of these calculations are negative or 0 
    # We can just do max(0, calc) to find the minimum distance you need to move
    # |       |   |       |
    # |         |     |   |
    # 0 1 2 3 4 5 6 7 8 9 10
    # Minimum distance that you need if you are going to travel in the opposite direciton
    # if you place the new table to the ___ of the rectangle
    down_dist = max(0, newTableLength-y1)
    up_dist = max(0, y2 - (boxLength - newTableLength))
    left_dist = max(0, newTableWidth-x1)
    right_dist = max(0, x2 - (boxWidth - newTableWidth))

    # Check if within bounds
    # why does checking whether the individual translated points are in bounds not work:
    #if down_dist + y2 > boxLength:
    #    down_dist = float("inf")
    #if y1 - up_dist < 0:
    #    up_dist = float("inf")
    #if left_dist + x2 > boxWidth:
    #    left_dist = float("inf")
    #if x1 - down_dist < 0:
    #    right_dist = float("inf")
    if newTableLength + tableLength > boxLength:
        down_dist, up_dist = None, None
    if newTableWidth + tableWidth > boxWidth:
        left_dist, right_dist = None, None

    solutionSet = [i for i in (down_dist, up_dist, left_dist, right_dist) if i is not None]
    if not solutionSet:
        print(-1)
    else:
        print(min(solutionSet))
