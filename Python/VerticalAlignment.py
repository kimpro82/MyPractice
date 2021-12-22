# Korean letter's length is also measured as 1
abcd = "abcd"
ssjj = "삼성전자"

print(len(abcd))
print(len(ssjj))


# How to count Korean letter's length as 2
length = 0
for char in ssjj :
    if char >= '가' :
        length += 2
print(length)


# Vertical alignment
list = [abcd, ssjj]

# trial 1
for i in list :
    print(i, '\t', 100)

# trial 2
for i in list :
    length = 10
    for char in i :
        if char >= '가' :
            length -= 2
        else :
            length -= 1
    i += length * ' '
    print(i, 100, sep = '')