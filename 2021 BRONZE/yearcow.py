cycle = ("Ox", "Tiger", "Rabbit", "Dragon", "Snake", "Horse", "Goat", "Monkey", "Rooster", "Dog", "Pig", "Rat")
global infoMap, yearMap
infoMap = {"Bessie": ("Ox", None, None)}
yearMap = {"Bessie": 0}

# Zodiac1 > Pointer zodiac
# Zodiac2 > CUR cow zodiac
def calc_rel_year(year, zodiac1, zodiac2, prev):
    if not prev:
        direct = cycle.index(zodiac2) - cycle.index(zodiac1)
        cycled = (len(cycle)-cycle.index(zodiac1)) + cycle.index(zodiac2)

        if direct <= 0:
            ans = cycled
        else:
            ans = direct
        return year + ans

    direct = cycle.index(zodiac1) - cycle.index(zodiac2)
    cycled = (len(cycle)-cycle.index(zodiac2)) + cycle.index(zodiac1)

    if direct <= 0:
        ans = cycled
    else:
        ans = direct
        
    return year - ans

def find_val(curCow):

    global infoMap, yearMap
    if curCow == "Bessie":
        return yearMap["Bessie"]
    else:
        
        if curCow not in yearMap:
            # Find info of the cow it points to
            year = find_val(infoMap[curCow][2])

            if infoMap[curCow][1] == "previous":
                rel_year = calc_rel_year(year, infoMap[infoMap[curCow][2]][0], infoMap[curCow][0], True)
            else:
                rel_year = calc_rel_year(year, infoMap[infoMap[curCow][2]][0], infoMap[curCow][0], False)
            
            yearMap[curCow] = rel_year

            return rel_year
        return yearMap[curCow]






n = int(input())
for i in range(n):
    inp = input().split()
    # ZODIAC, PREV/NEXT, POINTER_COW
    infoMap[inp[0]] = (inp[4], inp[3], inp[7])

print(abs(find_val("Elsie")))
