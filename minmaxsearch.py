import random

lvs = 2

def min_search(lv):
    if lv ==0:
        val =random.uniform(-1,1)
        print(val)
        return val
    else:
        return min(max_search(lv-1), max_search(lv-1))

def max_search(lv):
    print(lv)
    if lv==0:
        val = random.uniform(-1, 1)
        print(val)
        return val
    else:
        return max(min_search(lv-1), min_search(lv-1))

print(min_search(3))