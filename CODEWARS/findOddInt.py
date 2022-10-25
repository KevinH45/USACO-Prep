
def find_it(seq):
    freqMap = {}
    for i in seq:
        if i not in freqMap:
            freqMap[i] = 1
        else:
            freqMap[i] += 1
            
    for i,j in freqMap.items():
        if j%2!=0:
            return i
