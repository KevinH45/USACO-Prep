# Kevin Hwang, 2022
# http://www.usaco.org/index.php?page=viewproblem2&cpid=856
# O(1000*N)/O(N) solution

import sys

sys.stdin = open("blist.in", "r")
sys.stdout = open("blist.out", "w")

numCows = int(input())
reqList = []

for i in range(numCows):
	reqList.append(tuple(map(int, input().split())))

bucketsNeeded = float("-inf")
for i in range(1000):
	curBucketsNeeded = 0
	for j in reqList:
		lowerBound, upperBound = j[0], j[1]
		if lowerBound <= i and upperBound >= i:
			curBucketsNeeded += j[2]
	bucketsNeeded = max(bucketsNeeded, curBucketsNeeded)
print(bucketsNeeded)
		
