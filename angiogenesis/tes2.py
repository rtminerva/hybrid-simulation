a = [32, 37, 28, 30, 37, 25, 27, 24, 35, 55, 23, 31, 55, 21, 40, 18, 50, 35, 41, 49, 37, 19, 40, 41, 31]
m = max(a)
idr = [i for i, j in enumerate(a) if j == m]
print idr

idx = [i for i, j in enumerate(a) if j == m]
print idx
while len(idx) < tipss:
    for i in idx:
        b[i] = 0
    m = max(b)
    print m
    j = 0
    while len(idx) < tipss:
        if b[j] == m:
            idx.append(j)
        j += 1
idx.sort()
print idx