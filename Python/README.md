# [My Python Practice](../README.md#my-python-practice)

I'm sorry `C++` …… I betrayed you.


### \<List>

- [`hello_world("print")` (2024.05.23)](#hello_worldprint-20240523)
- [`re.sub()` (2023.02.12)](#resub-20230212)
- [Vertical Alignment 2 with *f-string* (2022.04.27)](#vertical-alignment-2-with-f-string-20220427)
- [Arguements Parsing (2022.03.24)](#arguements-parsing-20220324)
- [Vertical Alignment with Korean Letters (2021.12.21)](#vertical-alignment-with-korean-letters-20211221)
- [Iterator (2021.06.17)](#iterator-20210617)
- [`if` ~ `while` ~ `true` (2021.05.04)](#if--while--true-20210504)
- [`re.split()` (2021.04.29)](#resplit-20210429)
- [`__name__ == '__main__'` (2021.04.26)](#__name__--__main__-20210426)
- [Turtle (2021.03.24)](#turtle-20210324)
- [`map()` (2021.02.16)](#map-20210216)
- [Words Mix (2021.01.13)](#words-mix-20210113)
- [Count Words (2020.11.10)](#count-words-20201110)
- [Operator Precedence (2020.06.28)](#operator-precedence-20200628)
- [`print()` (2020.03.31)](#print-20200331)
- [Fibonacci Series (2019.12.18)](#fibonacci-series-20191218)
- [Generate List (2019.12.07)](#generate-list-20191207)
- [`with` ~ `open()` (2019.07.21)](#with--open-20190721)
- [Password (2019.05.24)](#password-20190524)
- [Class (2018.02.07)](#class-20180207)
- [`while` (2017.05.15)](#while-20170515)


## [`hello_world("print")` (2024.05.23)](#list)

- Just for fun ☞ [related meme](https://www.reddit.com/r/ProgrammerHumor/comments/13u2mfm/_/)   
  - Other language version ☞ [Bash](/Shell/README.md#hello_worldecho-20240523) [TypeScript]()
- Code and Result
  <details>
    <summary>Code : HelloWorldPrint.py</summary>

  ```py
  import sys
  ```
  ```py
  def hello_world(func_name):
      """
      Dynamically call the given function using its name.
      The name of the current executing function is passed as an argument.

      Caution:
          Using eval() can pose security risks!

      Args:
          func_name (str): Name of the function to be called

      Returns:
          None
      """
      current_func_name = sys._getframe().f_code.co_name
      func = eval(func_name)
      func(current_func_name)
  ```
  ```py
  if __name__ == "__main__":
      hello_world("print")
  ```
  </details>
  <details open="">
    <summary>Result</summary>

  ```py
  hello_world
  ```
  </details>

## [`re.sub()` (2023.02.12)](#list)

- Get domain from e-mail address by `re.sub()`
- A partial practice for [Coursera](https://www.coursera.org/) > [Using Databases with Python (University of Michigan)](https://www.coursera.org/learn/python-databases) > [Week 2 > Assignment 2](https://www.coursera.org/learn/python-databases/gradedLti/WOD7V/counting-email-in-a-database)

  <details open="">
    <summary>Codes : ReSub.py</summary>

  ```py
  import re

  email = "404@not.found"
  domain = re.sub(r"[\w\.-_*]+@", "", email)

  print(domain)
  ```
  The regex `[\w\.-_*]+@` is not the only answer, anyway it seems to work well.
  ```
  not.found
  ```
  </details>


## [Vertical Alignment 2 with *f-string* (2022.04.27)](#list)

- I dreamed of making a new open source library to do it for a while, but *f-string* is too strong …… This devil has broken my dear dream!
- Reference ☞ https://docs.python.org/3/reference/lexical_analysis.html#formatted-string-literals

  ```python
  sample = [
      ['이렇게', '하면'],
      ['줄이', '잘 맞을까'],
      ['모르겠네', '어디'],
      ['한 번', '볼까'],
  ]
  ```

  <details>
    <summary>1. Normal Approach</summary>

  ```python
  # 1. Normal Approach
  print("# 1. Normal Approach")
  for el in sample :
      print(el[0], el[1])
  ```
  ```
  # 1. Normal Approach
  이렇게 하면
  줄이 잘 맞을까
  모르겠네 어디
  한 번 볼까
  ```
  </details>

  <details>
    <summary>2. Use f-string</summary>

  ```python
  # 2. Use f-string
  sample[3][0] = '두 번'
  print("\n# 2. Use f-string")
  for el in sample :
      print(f"{el[0]:<10}", f"{el[1]:<10}")                   # Korean letters drive it to insanity
  ```
  ```
  # 2. Use f-string
  이렇게        하면
  줄이         잘 맞을까
  모르겠네       어디
  두 번        볼까
  ```
  </details>

  <details>
    <summary>2.1 Use f-string : Handle Korean letters</summary>

  ```python
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
  ```
  ```
  # 2.1 Use f-string 2 : Handle Korean letters
  이렇게     하면
  줄이       잘 맞을까
  모르겠네   어디
  세 번      볼까
  ```
  </details>

  <details>
    <summary>2.2 Use f-string : Change alignment direction</summary>

  ```python
  sample[3][0] = '네 번'
  print("\n2.2 Use f-string : Change alignment direction")
  for r in sample :
      length = [10, 10]
      for c in range(2) :
          for char in r[c] :
              if char >= '가' :
                  length[c] -= 1
      print(f"{r[0]:>{length[0]}} {r[1]:>{length[1]}}")
  ```
  ```
  2.2 Use f-string : Change alignment direction
      이렇게       하면
        줄이  잘 맞을까
    모르겠네       어디
      네 번       볼까
  ```
  </details>

  <details>
    <summary>2.3 Use f-string : Code generalization & individual alignment control</summary>

  ```python
  sample[3][0] = '다섯 번'
  print("\n2.3 Use f-string : Code generalization & individual alignment control")
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
  ```
  ```
  2.3 Use f-string : Code generalization & individual alignment control
  이렇게          하면
  줄이       잘 맞을까
  모르겠네        어디
  다섯 번         볼까
  ```
  </details>


## [Arguements Parsing (2022.03.24)](#list)

- A practice to parse arguments from command line to `.py` script file
- Reference ☞ https://en.wikipedia.org/wiki/Command-line_argument_parsing

  <details>
    <summary>Codes : ArguementParsing.py</summary>

  ```python
  import sys
  ```
  ```python
  def ArguementParsing() :
      if len(sys.argv) > 1 :                          # not > 0; sys.argv[0] is the script file name
          for arg in sys.argv :
              print(arg)
      else :
          print("No arguments has been received.")
  ```
  ```python
  # test
  def test() :
      for arg in list(sys.argv) :
          print(arg)
  ```
  ```python
  if __name__ == "__main__" :
      ArguementParsing()
      # test()                                        # 0(path) 1 2 3
  ```
  </details>

  <details>
    <summary>Codes : ArguementParsing.bat</summary>

  ```bat
  python ArguementParsing.py
  python ArguementParsing.py a b c
  ```
  </details>

  <details open="">
    <summary>Output</summary>
  
  ```
  > python ArguementParsing.py
  No arguments has been received.

  > python ArguementParsing.py a b c
  ArguementParsing.py
  a
  b
  c
  ```
  </details>


## [Vertical Alignment with Korean Letters (2021.12.21)](#list)

- A solution for the problem to **align text vertically** with both of English and Korean letters

  <details>
    <summary>Codes : VerticalAlignment.py</summary>

  ```python
  # Korean letter's length is also measured as 1
  abcd = "abcd"
  ssjj = "삼성전자"

  print(len(abcd))
  print(len(ssjj))
  ```
  ```
  4  
  4
  ```

  ```python
  # How to count Korean letter's length as 2
  length = 0
  for char in ssjj :
      if char >= '가' :
          length += 2
  print(length)
  ```
  ```
  8
  ```

  ```python
  # Vertical alignment
  list = ["abcd", "삼성전자"]

  # trial 1
  for i in list :
      print(i, '\t', 100)
  ```
  ```
  abcd     100
  삼성전자         100
  ```

  ```python
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
  ```
  </details>

  ```
  abcd      100
  삼성전자  100
  ```
  Thses are arranged vertically well in the console output. Please believe me ……


## [Iterator (2021.06.17)](#list)

- Originally started from a stupid question : Can a `method` call other method in the same class?
- I've just realized it was really obvious (Why does `the constructor` exist?)
- This code is a strange station, that two methods call each other with `iterator`

  <details>
    <summary>Codes : Iterator.py</summary>

  ```python
  turn = 0

  class Bros :

      def __init__(self) :
          global turn
          turn += 1
          print("<Conversation " + str(turn) + ">")
          self.conversation = iter(["Hey bro", "Wassup"])
          self.n = 0

      def bros1(self) :
          print(self.bros1.__name__ + " : " + next(self.conversation))
          if (self.n < 1) :
              self.n += 1
              self.bros2()
          else :
              print()

      def bros2(self) :
          print(self.bros2.__name__ + " : " + next(self.conversation))
          if (self.n < 1) :
              self.n += 1
              self.bros1()
          else :
              print()
  ```
  ```python
  if __name__ == "__main__" :

      Bros1 = Bros()
      Bros1.bros1()

      Bros2 = Bros()
      Bros2.bros2()
  ```
  </details>

  <details open="">
    <summary>Output</summary>

  > <Conversation 1>  
  > bros1 : Hey bro  
  > bros2 : Wassup

  > <Conversation 2>  
  > bros2 : Hey bro  
  > bros1 : Wassup
  </details>


## [`if` ~ `while` ~ `true` (2021.05.04)](#list)

- A practice of using `if` and `while`
- All the strings and numbers *except* `0` and `False` are regarded as `True`

  <details>
    <summary>Codes : IfWhileTrue.py</summary>

  ```python
  if True :
      print(True)

  if False :
      print(False)

  if 'abc' :
      print('abc')

  a = 1
  if a :
      print(a)

  b = 0
  if b :
      print(b)

  c = -1
  if c :
      print(c)
  ```
  > True  
  > abc  
  > 1  
  > -1

  ```python
  while True :
      print(True)
      break

  while False :
      print(False)
      break

  while '123' :
      print('123')
      break
  ```
  > True  
  > 123
  </details>


## [`re.split()` (2021.04.29)](#list)

- Seperating a `string` by plural delimiters
- Using regular expression (`re`)

  ```Python
  txt = 'one two/three.four'

  # 1. string.split()
  print(txt.split())                  # default : ' '
  print(txt.split('/'))
  # print(txt.split(' ').split('/'))    # Error

  # 2. Regular Expression
  import re
  print(re.split("[ /.]", txt))       # Enter delimiters directly
  print(re.split("\W", txt))          # \W = a-zA-Z0-9
  ```
  > ['one', 'two/three.four']  
  > ['one two', 'three.four']  
  > ['one', 'two', 'three', 'four']  
  > ['one', 'two', 'three', 'four']


## [`__name__ == '__main__'` (2021.04.26)](#list)

- A practice of importing and running `module` in Python
- Using `__name__` and `__main__`

  #### ModuleSample.py
  ```python
  if __name__ == '__main__' :
      print("Don't call me yet.")

  def call() :
      print("Call me now.")
  ```
  > Don't call me yet.

  #### ModuleRun.py
  ```python
  import ModuleSample

  ModuleSample.call()
  ```
  > Call me now.


## [Turtle (2021.03.24)](#list)

- A practice of python module `turtle`
- Very easy!

  ![Turtle Practice](Images/Turtle.gif)

  <details>
    <summary>Codes : Turtle.py</summary>

  ```python
  import turtle
  import time

  turtle.setup(width = 300, height = 300)
  turtle.title("My turtle practice")

  turtle.hideturtle()         # hide turtle : make the moving speed faster


  turtle.home()               # set the position (0, 0)
  turtle.position()

  turtle.penup()              # penup() = pu() = up() : move without drawing
  turtle.setpos(0, 125)

  turtle.pendown()            # pendown() = pd() = down() : move with drawing
  turtle.right(180)
  turtle.circle(125)          # 1st circle

  turtle.penup()
  turtle.setpos(0, 100)

  turtle.pendown()
  time.sleep(0.3)
  turtle.circle(100)          # 2nd circle

  turtle.delay(20)

  time.sleep(0.5)
  turtle.circle(100, steps=3) # 1st triangle

  turtle.penup()
  turtle.setpos(0, -100)
  turtle.right(180)

  turtle.pendown()
  turtle.circle(100, steps=3) # 2nd triangle

  turtle.penup()
  turtle.setpos(0, 100)
  turtle.right(180)

  turtle.delay(30)

  turtle.pendown()
  turtle.circle(100, steps=6) # hexagon


  turtle.mainloop()           # avoid the screen closing
  ```
  </details>


## [`map()` (2021.02.16)](#list)

- To find how `map()` runs
  - I guessed the result of running `map()` would be something to contain hidden elements.
  - But actually it is a `generator type object`, so has not futural list data before I request by `list()`.
- References
  - StackOverflow ☞ https://stackoverflow.com/questions/66225592/
  - https://realpython.com/python-map-function/#getting-started-with-pythons-map

  <details>
    <summary>Codes : Map.py</summary>

  ```python
  def details(txt) :
      print("elements :", txt)
      print("type :", type(txt))
      try :
          print("elements' type :", type(txt[0]), "\n")
      except :
          print("elements' type : an error occurs.\n")

  txt = "1 2 3 4 5"
  details(txt)

  txtsplit = txt.split()
  details(txtsplit)

  txtmap = map(int, txt.split())
  details(txtmap) # an error occurs

  txtlist = list(txtmap)
  details(txtlist)
  ```
  </details>

  <details>
    <summary>Results</summary>

  ```python
  elements : 1 2 3 4 5
  type : <class 'str'>
  elements' type : <class 'str'>

  elements : ['1', '2', '3', '4', '5']
  type : <class 'list'>
  elements' type : <class 'str'>

  elements : <map object at 0x7fefcdfe8dc0>
  type : <class 'map'>
  elements' type : an error occurs.

  elements : [1, 2, 3, 4, 5]
  type : <class 'list'>
  elements' type : <class 'int'>
  ```
  </details>


## [Words Mix (2021.01.13)](#list)

- Read a _csv_ file into a _dictionary_
- Import `csv`
- Seems that _dictionary type_ is not so suitable to generate random paragraphs

  #### `WordMix.py`

  <details>
    <summary>0. Check If Words.csv Exists</summary>

  ```python
  import os
  ```
  ```python
  path = "C:\\Users\\……\\Python\\Words.csv"
  # \\ : escape character of \
  os.path.isfile(path)
  ```
  > True
  </details>

  <details>
    <summary>1. Read Words.csv simply</summary>

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
  </details>

  <details>
    <summary>1-1. Read Words.csv as dictionary type</summary>

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
  </details>

  <details>
    <summary>1-2. Get rid of '\ufeff' from the head of data</summary>

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
  </details>


## [Count Words (2020.11.10)](#list)

- Count words without duplication from .txt file
- import `re` for using `regular expression`

  <details>
    <summary>Codes : CountWords.py</summary>

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
  </details>


## [Operator Precedence (2020.06.28)](#list)

- Answer for my friend *YW Jang*'s question
- Reference ☞ https://www.programiz.com/python-programming/precedence-associativity

  <details>
    <summary>Codes : OperatorPrecedence.py</summary>

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
  </details>


## [`print()` (2020.03.31)](#list)

- Simple practice with `print()`

  <details>
    <summary>Codes : Print.py</summary>

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
  </details>


## [Fibonacci Series (2019.12.18)](#list)

- Simply Generating `Fibonacci Series` by Python

  #### `FibonacciSeries.py`

  ```python
  a = [1, 1]
  n = 2

  while n<10 : # length = 10
      a.append(a[n-2] + a[n-1])
      n += 1

  print(a)
  ```
  > [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]  


## [Generate List (2019.12.07)](#list)

- Generate lists by various ways

  #### `GenerateList.py`

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


## [`with` ~ `open()` (2019.07.21)](#list)

- Read binary file
- Convert decimal number ↔ hexadecimal number

  <details>
    <summary>Codes : WithOpen.py</summary>

  ```python
  # get current working directory
  import os

  os.getcwd()
  print(os.getcwd())

  # check if the file exists
  os.path.isfile("path")
  ```
  > True

  ```python
  import binascii

  # with statement
  with open('path','rb') as f: # rb : read & binary
      string = f.read()
      print(string[0:10])
      print(binascii.b2a_hex(string[0:10]))
  ```
  > b'1990.02.19'  
  > b'313939302e30322e3139'

  ```python
  # with statement X
  f = open('path','rb')
  data = f.read()
  print(data[0:10])
  print(binascii.b2a_hex(data[0:10]))
  f.close()
  ```
  > b'1990.02.19'  
  > b'313939302e30322e3139'

  ```python
  # decimal → hexadecimal
  hex(30000)
  hex(3000000)
  hex(100)
  ```
  > '0x7530'  
  > '0x2dc6c0'  
  > '0x64'

  ```python
  # hexadecimal → decimal
  int('7530', 16)
  int('2dc6c0', 16)
  int('64', 16)
  ```
  > 30000  
  > 3000000  
  > 100
  </details>


## [Password (2019.05.24)](#list)

- Input the correct passworld within 5 trials or die
- Practice `if`~`else`, `break`/`continue`, `time.sleep()` and so on

  #### `Password.py`

  <details>
    <summary>Codes : Password.py</summary>

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
  </details>


## [Class (2018.02.07)](#list)

- Simple Python `class` practice

  #### `Class.py`

  ```python
  class MyFirstClass :
      
      def Family(self, name, role):
          print(name, "is a(an)", role, "in my family")

  Do = MyFirstClass()

  Do.Family("Kim", "Husband")
  Do.Family("Shin", "Wife")
  Do.Family("Kim", "Future Baby")
  ```

  ![Python_Class_Test](Images/Class.PNG)

  I found that a simple `class` in Python doesn't need stuffs like `__main__`, `__init__` and so on.  
What the `__hell__`?


## [`while` (2017.05.15)](#list)

- Simple Python practice

  #### `While.py`

  ```python
  death_entropy = 100
  my_entropy = 1

  while(my_entropy < death_entropy) :
      print(my_entropy)
      my_entropy += 1
  print('Nirvana')
  ```
  ```
  1
  2
  3
  ……
  100
  Nirvana
  ```