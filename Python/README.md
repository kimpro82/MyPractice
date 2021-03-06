# [My Python Practice]
- WordsMix.py (2021.01.13)
- Count_Words.py (2020.11.10)
- Operator_Precedence_Test.py (2020.06.28)
- Print.py (2020.03.31)
- Suffle_List.py (2020.03.30)
- Random_Seed_Influence.py (2020.01.05)
- Square_Root.py (2020.01.01) (adjusted 2020.01.04)
- Fibonacci_Series.py (2019.12.18)
- Player2.py (2019.12.15)
- Generate_List.py (2019.12.07)
- Password.py (2019.05.24)
- Player.py (2019.03.12) - maybe?
- Class_Test.py (2018.02.07)
- Nirvana.py (2017.05.15)


## WordsMix.py (2021.01.13)
- Read a _csv_ file into a _dictionary_
- Import `csv`
- Seems that _dictionary type_ is not so suitable to generate random paragraphs

#### 0. Check If Words.csv Exists
```python
import os
```
```python
path = "C:\\Users\\……\\Python\\Words.csv"
# \\ : escape character of \
os.path.isfile(path)
```
> True

#### 1. Read Words.csv simply 
```python
import csv
```
```python
with open(path,'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)

    for c in reader:
        for k, v in c.items():
            print(v, end= ' ')
        print("\n")
```
> 멍청하게 떡볶이 먹고 배탈 나는 똥개  
> 어리석게 꼭지에서 주식 사는 너구리  
> 정신 못 차리고 반바지에 긴 양말 신은 코흘리개  
> 한심하게 노래방 가서 고해 부르는 개미햝기  
> 아무 생각없이 담뱃불 붙이다 앞머리 불 붙은 이등병

#### 1-1. Read Words.csv as dictionary type
```python
with open(path,'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)

    for row in reader:
        print(row)
```
> {'\ufeff수식어1': '멍청하게', '수식어2': '떡볶이 먹고 배탈 나는', '명사': '똥개'}  
> {'\ufeff수식어1': '어리석게', '수식어2': '꼭지에서 주식 사는', '명사': '너구리'}  
> {'\ufeff수식어1': '정신 못 차리고', '수식어2': '반바지에 긴 양말 신은', '명사': '코흘리개'}  
> {'\ufeff수식어1': '한심하게', '수식어2': '노래방 가서 고해 부르는', '명사': '개미햝기'}  
> {'\ufeff수식어1': '아무 생각없이', '수식어2': '담뱃불 붙이다 앞머리 불 붙은', '명사': '이등병'}

#### 1-2. Get rid of '\ufeff' from the head of data
```python
with open(path,'r', encoding='utf-8-sig') as f:
    reader = csv.DictReader(f)

    for row in reader:
        print(row)
```
> {'수식어1': '멍청하게', '수식어2': '떡볶이 먹고 배탈 나는', '명사': '똥개'}  
> {'수식어1': '어리석게', '수식어2': '꼭지에서 주식 사는', '명사': '너구리'}  
> {'수식어1': '정신 못 차리고', '수식어2': '반바지에 긴 양말 신은', '명사': '코흘리개'}  
> {'수식어1': '한심하게', '수식어2': '노래방 가서 고해 부르는', '명사': '개미햝기'}  
> {'수식어1': '아무 생각없이', '수식어2': '담뱃불 붙이다 앞머리 불 붙은', '명사': '이등병'}


## Count_Words.py (2020.11.10)
- Count words without duplication from .txt file
- import `re` for using `regular expression`

```python
import os
import re
```

```python
# Check if the target file exists
path = "C:\\...\\Python\\subtitle - 1.1.txt"
os.path.isfile(path)
```
> True

```python
# Call words' list with duplication
document_raw = open(path, 'r')
document_lower = document_raw.read().lower()
words_duplication = re.findall(r'\b[a-z]{3,15}\b', document_lower)
# Regular expression to avoid meaningless or wrong words
```

```python
# Remove duplication from the list
words = set(words_duplication)
print(len(words))
```
> 455

## Operator_Precedence_Test.py (2020.06.28)
answer for my friend YW Jang's question

```python
print("F" == "M")
```
> False

```python
print(bool("m"))
```
> True

`==` runs prior to `or` in Python

```python
print("F" == "M" or "m")
print(("F" == "M") or "m") # the same with the above line
```
> True

☞ reference : https://www.programiz.com/python-programming/precedence-associativity


## Print.py (2020.03.31)
simple practice with `print()`

```python
#1. Print normally
print("위")
print("아래")
```
> 위  
> 아래

```python
#2. Write on the same line
print("왼쪽", end='')
print("에 붙여서 계속")
```
> 왼쪽에 붙여서 계속

```python
#3. Change lines within one function
print("줄을\n막\n바꿔")
```
> 줄을  
> 막  
> 바꿔


## Suffle_List.py (2020.03.30)
- find how to get random lists without overlapping values
- use `random` `random.randint` `random.sample`

```python
import random
```

#### Trial 1 : Use `random.randint()`
```python
sufflelist1 = []

for i in range(0,20) :
    random.seed(330 + i)
    sufflelist1.append(random.randint(1, 20))

print(sufflelist1) # There are overlapping values.
```
> [20, 11, 8, 18, 8, 5, 1, 7, 4, 5, 13, 19, 4, 7, 13, 10, 18, 12, 11, 14]

#### Trial 2 : Use `random.sample()`
```python
random.seed(330)
sufflelist2 = random.sample(range(1, 21), 20)

print(sufflelist2) # random.sample() offers values without overlapping.
```
> [20, 3, 2, 13, 1, 6, 10, 9, 15, 11, 14, 4, 18, 8, 16, 17, 7, 19, 12, 5]

#### Trial 3 : Use `while` Statement
```python
sufflelist3 = []
loopnum = 0

while len(sufflelist3) < 20 :
    random.seed(330 + loopnum)
    r = random.randint(1,20)
    if r not in sufflelist3 : sufflelist3.append(r)
    loopnum += 1

print(sufflelist3)
# It seems similar with Trial 1's sequence but there's no overlapping values.
```
> [20, 11, 8, 18, 5, 1, 7, 4, 13, 19, 10, 12, 14, 6, 2, 3, 17, 16, 15, 9]  
```python
print(loopnum) # It shows how many times overlapping numbers are rejected.
```
> 87


## Random_Seed_Influence.py (2020.01.05)
make sure the range of `random.seed()`'s influence  
☞ `random.seed()` affects just one time!

```python
import random
```

```python
# case 1
print(random.random())
print(random.random())
print(random.random())
```
> 0.48515227527760874  
> 0.48808537244754757  
> 0.9509662749522355

```python
# case 2
random.seed(105)
print(random.random())
print(random.random())
print(random.random())
```
> **0.8780993490764925**  
> 0.3491186468357038  
> 0.7907236599059974

```python
# case 2-1
random.seed(105); print(random.random())
random.seed(105); print(random.random())
random.seed(105); print(random.random())
```
> **0.8780993490764925**  
> **0.8780993490764925**  
> **0.8780993490764925**

```python
# case 3
random.seed(105)
for i in range(0,3) :
    print(random.random())
```
> **0.8780993490764925**  
> 0.3491186468357038  
> 0.7907236599059974

```python
# case 3-1
for i in range(0,3) :
    random.seed(105); print(random.random())
```
> **0.8780993490764925**  
> **0.8780993490764925**  
> **0.8780993490764925**


## Square_Root.py (2020.01.01)
an algorithm to find n's square root without `math.sqrt()`  
- adjusted 2020.01.04 : rearrange methods' order in `for` Loop for improving intuitive understanding

```python
import random
import math
import matplotlib.pyplot as plt

n = 2 # should be larger than 1
k = 20 # run loop k times

squareroot = []
lowerlimit, upperlimit = 1, n

for i in range(k) :

    random.seed(20200104) # can be removed
    squareroot.append(random.uniform(lowerlimit, upperlimit))
    square = squareroot[i] ** 2
    print(i+1, squareroot[i], square, square-n)

    if square == n :
        break;
    elif square < n :
        # print("smaller")
        lowerlimit = max(squareroot[i], lowerlimit)
    else :
        # print("larger")
        upperlimit = min(squareroot[i], upperlimit)

myplot = plt.plot(range(k), squareroot)
# myplot.hlines(math.sqrt(n), color="red", linestyle="--") # doesn't work
```
> 1 1.224709461308563 1.4999132646187106 -0.5000867353812894  
> 2 1.3989245806155413 1.956989982250368 -0.04301001774963198  
> 3 1.5339919143112415 2.3531311931722674 0.3531311931722674  
> (중략)  
> 19 1.4141854421168503 1.9999204646952313 -7.953530476867421e-05  
> 20 1.4141980335178153 1.9999560780056558 -4.3921994344220394e-05 

![approximate to the exact square root](https://github.com/kimpro82/My_Practice/blob/master/images/Square_Root_20200104.png)

```python
# practice
random.random()
random.randrange(1,n) # output only integer
random.uniform(1,n) # output float
list(range(10))
```
> 0.2508550895840985  
> 1  
> 1.2710268293926659  
> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]  


## Fibonacci_Series.py (2019.12.18)
Simply Generating `Fibonacci Series` by Python

```python
a = [1, 1]
n = 2

while n<10 : # length = 10
    a.append(a[n-2] + a[n-1])
    n += 1

print(a)
```
> [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]  


## Player2 (2019.12.15)
Updates : correct use of `__init__`, add validation of variables and use `return` in each method

```python
# generating a player who has location (a,b) and its trace data
class player :

    def __init__(self, name='', location=[0,0]) :
        self.name = name
        # add validation
        self.location = location
            if not (type(self.location)==list and len(self.location)==2) :
                raise ValueError("The location's shape is not [x, y].")
        self.trace = [self.location]
    
    # methods for moving
    def right(self, num=1) :
        self.location = [self.location[0] + num, self.location[1]]
        self.trace.append(self.location)
        return self.location
        # Is there any other way to avoid repeat this common line?
    
    def left(self, num=1) :
        self.location = [self.location[0] - num, self.location[1]]
        self.trace.append(self.location)
        return self.location
    
    def up(self, num=1) :
        self.location = [self.location[0], self.location[1] + num]
        self.trace.append(self.location)
        return self.location
    
    def down(self, num=1) :
        self.location = [self.location[0], self.location[1] - num]
        self.trace.append(self.location)
        return self.location
        
    # Should 'self' be really abused so much like the above?
```

```python
# generating an instance
p1 = player('John', [0,0])
```

```python
p2 = player('John', 1)
```
> ValueError: The location's shape is not [x, y].

```python
# Results
print(p1.right())
print(p1.up(3))
print(p1.left(2))
print(p1.trace)
```
> [1, 0]  
> [1, 3]  
> [-1, 3]  
> [[0, 0], [1, 0], [1, 3], [-1, 3]]  

```python
# practice
type([0,0])
type([0,0])==list
len([0,0])
```
> list  
> True  
> 2  

```python
not True
not(True)
not True and False
not(True and False)
```
> False  
> False  
> False  
> True  

## Generate_List.py (2019.12.07)
generate lists by various ways

```python
list1 = [[0,0], [0,0], [0,0], [0,0]]
list2 = [[0,0]] * 4
list3 = [0,0] * 4

print(list1, "\n", list2, "\n", list3)
list1 == list2
```

> [[0, 0], [0, 0], [0, 0], [0, 0]]  
> [[0, 0], [0, 0], [0, 0], [0, 0]]  
> [0, 0, 0, 0, 0, 0, 0, 0]  
> True  


## Password.py (2019.05.24)
input the correct passworld within 5 trials or die  
practice if~else, break/continue, time.sleep() and so on

```python
import time # for using time.sleep()

chance = 0
pw_original = "mymy" # password. a word that calls a pass. you nahm sayin?

while chance < 5 :
    pw_input = input("Input your password : ")

    # right
    if pw_original == pw_input :
        print("You entered the correct password")
        break
    
    # wrong
    else:
        chance += 1
        print("You entered the wrong passwords", chance, "times.")
        if chance == 5 :
            print("You bad guys will be delayed as a penalty.")
            time.sleep(3)
        else :
            continue

# Of course, saving the original password in this file is somewhat stupid.
# But, yes I am.
```


## Player (2019.03.12) - maybe?
A class that traces a player's coordinate

```python
# generating a player who has locatiion (a,b) and its trace data
 
 
class player :
    
    name = ''
    # can be named at each instance
    location = [0,0]
    # can be set as a random position (future task)
    trace = [[0,0]]
    # accumulationg as a list of location (a,b)s' trace
    
    def init(self, name, location, trace) : # Why doesn't __init__ work?
    # alternative : def init(self, name='', location=[0,0], trace=[])
        self.name = name
        self.location = location
        self.trace = trace
    
    # methods for moving
    def right(self, num=1) :
        self.location = [self.location[0] + num, self.location[1]]
        self.trace.append(self.location)
        print(self.location)
        # Is there any other way to avoid repeat this common line?
    
    def left(self, num=1) :
        self.location = [self.location[0] - num, self.location[1]]
        self.trace.append(self.location)
        print(self.location)
    
    def up(self, num=1) :
        self.location = [self.location[0], self.location[1] + num]
        self.trace.append(self.location)
        print(self.location)
    
    def down(self, num=1) :
        self.location = [self.location[0], self.location[1] - num]
        self.trace.append(self.location)
        print(self.location)
        
        # Should 'self' be really abused so much like the above?
```

```python
# generating an instance
p1 = player() 

# Results
p1.right()
p1.up(3)
p1.left(2)
print(p1.trace)
```
> [1, 0]  
[1, 3]  
[-1, 3]  
[[0, 0], [1, 0], [1, 3], [-1, 3]]  


## Class_Test.py (2018.02.07)
a simple Python `class` practice

```python
class MyFirstClass :
    
    def Family(self, name, role):
        print(name, "is a(an)", role, "in my family")

Do = MyFirstClass()

Do.Family("Kim", "Husband")
Do.Family("Shin", "Wife")
Do.Family("Kim", "Future Baby")
```

![Python_Class_Test](https://github.com/kimpro82/My_Practice/blob/master/images/2018-02-07%20Python_Class_Test.PNG)

I found that a simple `class` in Python doesn't need stuffs like `__main__`, `__init__` and so on.
What the `__hell__`?


## Nirvana.py (2017.05.15)
a simple Python practice

```python
death_entropy = 100
my_entropy = 1

while(my_entropy < death_entropy) :
    print(my_entropy)
    my_entropy += 1
print('Nirvana')
```
