def digital_root(n):
    if len(str(n))==1:
        return n
    else:
        n = [int(x) for x in str(n)]
        return digital_root(sum(n))

# 17 > 8
# 256 > 13 > 4
# O(n) O(log n) O(n log n) O(n^2)
# individual steps: O(n)
# the greater N (number od digits), in step 1
# N: number of digits in step 1
# M: number od digits after doing step 1
#
# the greater N, the greater M
# whats the relationship between N and M.
# it depends. it's not just N, but specific digits.
# some kind of average. all the digits are 5 to try to get at this average
# M = k * N  (k < 1)
# M = N ^ k  (k < 1)
# M = N - k
# a that has N digits
# b is the number that has M digits
# b = 5N
# M = log10(b)
# N = log(a)
# 10 has 2 digits, 100 has 3 digits, 1000 has 4 digits
# log10(x) : this is number of digits in x (or proportional to it)

# log2(x) = K * log10(x)
# log(x)
# log(N) steps to reach one digit
# O (N log N) : N not the same as the parameter to digits_root(n) as you've written it above
# N is number of digits in n
