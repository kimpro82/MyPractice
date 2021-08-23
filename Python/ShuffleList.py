import random


# Trial 1 : Use random.randint()

sufflelist1 = []

for i in range(0,20) :
    random.seed(330 + i)
    sufflelist1.append(random.randint(1, 20))

print(sufflelist1) # There are overlapping values.


# Trial 2 : Use random.sample()

random.seed(330)
sufflelist2 = random.sample(range(1, 21), 20)

print(sufflelist2) # random.sample() offers values without overlapping.


# Trial 3 : Use while Statement

sufflelist3 = []
loopnum = 0

while len(sufflelist3) < 20 :
    random.seed(330 + loopnum)
    r = random.randint(1,20)
    if r not in sufflelist3 : sufflelist3.append(r)
    loopnum += 1

print(sufflelist3)
# It seems similar with Trial 1's sequence but there's no overlapping values.

print(loopnum) # It shows how many times overlapping numbers are rejected.