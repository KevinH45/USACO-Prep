# we consider only 10? the positions that 10 goes in?

# -5 _ 5 _ 0 _ 20 _
# sufficient conditions , necessary conditions to fulfill the ultimate criteria
# trial position of the 10, trial scores
# is it necessary tghat all b's appear somewhere among trial scores?
# sufficient? (make a note of initial score)
# 10, 5, -10
# 15 | -5 (10)  5 [15]   0 [15]    20 [35]
# initial score: [15]
# 15, 10, 10, -10
# we know that 10 appears *somewhere*
#
# 
# -2000 _ -2000 _
# options = [3998000, 4000000, None] 
# x = 0
# -5, 0, 0, 20
# 
# F
# O(F)
# O(k)
# O(F*k)
# O(0.5*F*k)
# O(F*k)
# O(n)
# n =1000000
# 1000000 operations
# 10**7 : way above 10**7, forget about it
# way below: good
#
# O(F*k) , F 8e6, k 2**3, 
#


k, n = map(int, input().split())
marks = list(map(int, input().split()))
scores = tuple(map(int, input().split()))
set_scores = set(scores)
select_score = scores[0]

def calc_init(index):
    r_operation = sum([-i for i in marks[0:index]])
    return select_score + r_operation


def check_valid(init_score):

    cur = init_score
    gen_scores = set()
    for x in marks:
        cur += x
        gen_scores.add(cur)
    
    return set_scores.issubset(gen_scores)

seen_scores = set()
for i in range(1,k+1):
    init_score = calc_init(i)
    if check_valid(init_score):
        seen_scores.add(init_score)

print(len(seen_scores))



