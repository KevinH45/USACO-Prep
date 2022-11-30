s = input()
global strings
strings = []

def perms(cur, s, used=[]):
    
    if len(cur)==len(s):
        global strings
        strings.append(cur)
        return
    
    subset = [(i,j) for i,j in enumerate(s) if i not in used]

    for i,j in subset:
        perms(cur+j, s, used+[i])

    return 

perms("", s)
print(len(set(strings)))

for i in sorted(list(set(strings))):
    print(i)