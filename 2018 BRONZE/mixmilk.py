import sys
sys.stdin = open("mixmilk.in", "r")
sys.stdout = open("mixmilk.out", "w")

c1, m1 = map(int, input().split())
c2, m2 = map(int, input().split())
c3, m3 = map(int, input().split())

c = [c1, c2, c3]
milk = [m1, m2, m3]
count = 0

for i in range(100):

    interval = 1
    if count==0:
        bin, bout = 0, 1
    elif count==1:
        bin, bout = 1, 2
    else:
        bin, bout = 2, 0
        interval = -2

    if milk[bin]+milk[bout] <= c[bout]:
        milk[bin], milk[bout] = 0, milk[bin]+milk[bout]
    else:
        overfill = (milk[bout] + milk[bin]) - c[bout]
        milk[bin], milk[bout] = overfill, c[bout]
    
    count += interval

for i in milk: print(i)
    