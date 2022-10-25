def ascend_descend(length, minimum, maximum):
    
    if maximum < minimum or length==0:
        return ""
    
    if maximum == minimum:
        return (str(minimum)*length) [0:length]
    
    s = str(minimum)
    c = minimum
    interval = 1
    
    while len(s)<length:
        c += interval
        s += str(c)
        
        if c==minimum:
            interval = 1
        
        if c==maximum:
            interval = -1
            
    return s[0:length]