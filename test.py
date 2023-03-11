orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 10)]
res = list(filter(lambda x: x[0] != x[1], orbits))
print(res)
def max(orb):
    maxInd = 0
    max = 0
    for i in range(len(orb)):
        x = orb[i][0]
        y = orb [i][1]
        if x * y > max:
            max = x * y
            maxInd = i
    return maxInd        
print(max(res))