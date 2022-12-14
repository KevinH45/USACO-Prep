def gcd(a, b):
    if b==0:
        return a
    return gcd(b, a%b)

def get_last_occ(n, nums):

    index = None
    for i in range(len(nums)):
        if nums[i] == n:
            index = i
    return index


t = int(input())
for _ in range(t):
    n = int(input())
    p_nums = tuple(map(int, input().split()))
    nums = list(set(p_nums))

    for i in range(len(nums)):
        nums[i] = (nums[i], get_last_occ(nums[i], p_nums))

    max_sum = -1
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            if gcd(nums[i][0], nums[j][0]) == 1:
                max_sum = max(max_sum, nums[i][1]+nums[j][1]+2)
    print(max_sum)


