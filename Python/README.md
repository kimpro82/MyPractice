# [My Python Practice]
- Square_Root.py (2020.01.01)
- Fibonacci_Series.py (2019.12.18)
- Player2.py (2019.12.15)
- Generate_List.py (2019.12.07)
- Password.py (2019.05.24)
- Player.py (2019.03.12) - maybe?
- Class_Test.py (2018.02.07)
- Nirvana.py (2017.05.15)


## Square_Root.py (2020.01.01)
an algorithm to find n's square root without math.sqrt()

```python
import random
import math
import matplotlib.pyplot as plt

n = 2 # should be larger than 1

random.seed(20200101)
squareroot = [random.uniform(1, n)]
lowerlimit, upperlimit = 1, n

k = 20 # run loop k times
for i in range(k) :

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

    squareroot.append(random.uniform(lowerlimit, upperlimit))

myplot = plt.plot(range(k+1), squareroot)
# myplot.hlines(math.sqrt(n), color="red", linestyle="--") # doesn't work
```
> 1 1.122733720559369 1.2605310072810834 -0.7394689927189166  
> 2 1.7599794873175498 3.0975277957785456 1.0975277957785456  
> 3 1.3090078515307688 1.7135015553691992 -0.28649844463080076  
> (중략)  
> 19 1.414220824726189 2.000020541089222 2.0541089222003706e-05  
> 20 1.4142176799584678 2.000011646307111 1.1646307111146115e-05  

![approximate to the exact square root](https://github.com/kimpro82/My_Practice/blob/master/images/Square_Root_20200101.png)

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
