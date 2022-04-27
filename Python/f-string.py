sample = [
    ['이렇게', '하면'],
    ['줄이', '잘 맞을까'],
    ['모르겠네', '어디'],
    ['한 번', '볼까'],
]

# 1. Normal
print("# 1. Normal")
for el in sample :
    print(el[0], el[1])

# 2. Use f-string
sample[3][0] = '두 번'
print("\n# 2. Use f-string")
for el in sample :
    print(f"{el[0]:<10}", f"{el[1]:<10}")                   # Korean letters drive it to insanity

# 2.1 Use f-string : Handle Korean letters
sample[3][0] = '세 번'
print("\n# 2.1 Use f-string 2 : Handle Korean letters")
for r in sample :
    length = [10, 10]
    for c in range(2) :
        for char in r[c] :
            if char >= '가' :
                length[c] -= 1
    # print(length[0], length[1])                           # test : ok
    # print(f"{r[0]:<length[0]} {r[1]:<length[1]}")         # ValueError: Invalid format specifier; length[] → {length[]}
    print(f"{r[0]:<{length[0]}} {r[1]:<{length[1]}}")

# 2.2 Use f-string : Change alignment direction
sample[3][0] = '네 번'
print("\n2.2 Use f-string : Change alignment direction")
for r in sample :
    length = [10, 10]
    for c in range(2) :
        for char in r[c] :
            if char >= '가' :
                length[c] -= 1
    print(f"{r[0]:>{length[0]}} {r[1]:>{length[1]}}")

# 2.3 Use f-string : Code generalization & individual alignment control
sample[3][0] = '다섯 번'
print("\n2.3 Use f-string : Code generalization")
for r in sample :
    length = [10] * len(r)
    for c in range(len(r)) :
        for char in r[c] :
            if char >= '가' :
                length[c] -= 1
        if c == 1 :
            print(f"{r[c]:>{length[c]}}", end = '')
        else :
            print(f"{r[c]:<{length[c]}}", end = '')
    print()