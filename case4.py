def first(*args):
    cem = 0
    for i in args:
        cem += i
    return cem

print(first(0,1,5,7,12,23,35,40,))

def second():
    massiv = list()
    for i in range(0,124):
        if (i % 2 == 0):
            massiv.append(i)
    return massiv

print(second())