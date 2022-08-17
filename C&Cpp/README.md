# My C/C++ Practice

The final destination of programming


### \<List>

- [GCC Optimization Option Practice (2022.08.16)](#gcc-optimization-option-practice-20220816)
- [`printf()` format test (2022.04.25)](#printf-format-test-20220425)
- [Binary Search 1 (2022.04.19)](#binary-search-1-20220419)
- [Binary Search 0 (2022.02.11)](#binary-search-0-20220211)
- [Increment and Decrement Operators (2022.02.01)](#increment-and-decrement-operators-20220201)
- [Prevent Garbage Value (2022.01.21)](#prevent-garbage-value-20220121)
- [Containers : Deque, Stack and Queue (2021.10.14)](#containers--deque-stack-and-queue-20211014)
- [Template (2021.07.23)](#template-20210723)
- [Stack Overflow (2021.05.18)](#stack-overflow-20210518)
- [Hello World (2021.05.12)](#hello-world-20210512)


※ All codes include the following top lines. :
```c
// C
#include <stdio.h>
```
```cpp
// CPP
#include <iostream>

using namespace std;
```


## [GCC Optimization Option Practice (2022.08.16)](#list)

- Generate many assembly(`.s`) files with various optimization options in `GCC`
- But I've just realized that I'm not ready yet to read their assembly codes ……
- However, I've found at least that the generally known properties of the optimization options are not fixed absolutely.  
  (For example, `Os` is known as smaller code size but it sometimes returns rather larger one.)
- References :  
  · https://gcc.gnu.org/onlinedocs/gcc/Optimize-Options.html  
  · https://wiki.kldp.org/wiki.php/GccOptimizationOptions  
  · https://www.rapidtables.com/code/linux/gcc/gcc-o.html

#### `OptimizePractice.c`
```c
void operate(int i, int* p)
{
    if (i % 2 != 0) (*p)++;
}
```
```c
int main()
{
    int num = 0;
    int* p = &num;

    for (int i = 0; i < 10; i++) operate(i, p);

    printf("%d\n", num);

    return 0;
}
```
> 5

#### `OptimizePractice.bat` (Old)
```batch
gcc -O0 -S OptimizePractice.c -o OptimizePractice_O0.s
gcc -O1 -S OptimizePractice.c -o OptimizePractice_O1.s
gcc -O2 -S OptimizePractice.c -o OptimizePractice_O2.s
gcc -O3 -S OptimizePractice.c -o OptimizePractice_O3.s
gcc -Os -S OptimizePractice.c -o OptimizePractice_Os.s
gcc -Ofast -S OptimizePractice.c -o OptimizePractice_Ofast.s
```

#### `OptimizePractice.bat` (New)
```batch
@echo off

set name=OptimizePractice
set options=O0 O1 O2 O3 Os Ofast
@REM There should be no space on the both side of "="

for %%i in (%options%) do (
    @REM echo %%i
    gcc -%%i -S %name%.c -o %name%_%%i.s
)
```


## [`printf()` format test (2022.04.25)](#list)

- I wrote the below codes in [*GCJ 2022 Round 1B*](https://github.com/kimpro82/MyCodingContest/tree/master/Google/CodeJam/2022%20Round%201B#google-code-jam-2022---round-1b) - [*Controlled Inflation*](https://github.com/kimpro82/MyCodingContest/tree/master/Google/CodeJam/2022%20Round%201B#controlled-inflation-14pts-21pts), but there's some struggle with `printf()`'s format `%d` `%ld` `%lld`.  
  (All the variables are declared as *long long* type.)
```cpp
// test
// printf("min : %lld, max : %lld, dist : %lld, sum1 : %lld, sum2 : %lld\n", min, max, dist, sum1, sum2);
```
- I will never miss the criminal!

#### `printf.c` & `printf.cpp`
The codes except each of the headers are the same.
```c
int main()
{
    char text[] = "%d %ld %lld\n";
    printf(text, __SCHAR_MAX__, __SCHAR_MAX__, __SCHAR_MAX__);
    printf(text, __INT8_MAX__, __INT8_MAX__, __INT8_MAX__);
    printf(text, __SHRT_MAX__, __SHRT_MAX__, __SHRT_MAX__);
    printf(text, __INT16_MAX__, __INT16_MAX__, __INT16_MAX__);
    printf(text, __INT_MAX__, __INT_MAX__, __INT_MAX__);
    printf(text, __LONG_MAX__, __LONG_MAX__, __LONG_MAX__);
    printf(text, __INT32_MAX__, __INT32_MAX__, __INT32_MAX__);
    printf(text, __LONG_LONG_MAX__, __LONG_LONG_MAX__, __LONG_LONG_MAX__);
    printf(text, __INT64_MAX__, __INT64_MAX__, __INT64_MAX__);

    return 0;
}
```

#### Output
```
127 127 8458399796925825151
127 127 8458399796925825151
32767 32767 8458399796925857791
32767 32767 8458399796925857791
2147483647 2147483647 8458399799073308671
2147483647 2147483647 8458399799073308671
2147483647 2147483647 8458399799073308671
-1 2147483647 9223372036854775807
-1 2147483647 9223372036854775807
```

#### Implications
- `%d` and `%ld` don't make trouble with reading `char` or `short`, but `%lld` is something special.
- Make sure `int` == `long` == `int32` in the current standard environment
- **-1** seems interesting. `__LONG_LONG_MAX__`(== `__INT64_MAX__`) is `0 111 …… 1111`, but `%d` reads only partial digits from it.  
  And the partial number `1 111 …… 1111` indicates -1 as [2's complement](https://en.wikipedia.org/wiki/Two%27s_complement).


## [Binary Search 1 (2022.04.19)](#list)

- I tried this code with [Binary Search 0 (2022.02.11)](#binary-search-0-20220211) about the same time,  
  but couldn't find why the traversal results are wrong.
- There was a crazy mistake …… It stole my two months!

#### `BinarySearch.c`
```c
#include <stdio.h>
#include <stdlib.h>                             // malloc()
```
```c
typedef struct _tNode                           // It makes using struct easier to declare it with typedef
{
    int value;
    struct _tNode* left;                        // Node* left : why does it not work?
    struct _tNode* right;                       // should be declared as a pointer
} Node;
```
```c
Node* insert(Node* root, int value)             // The location of '*' doesn't matter
{
    if (root == NULL)
    {
        Node* root = malloc(sizeof(Node));      // malloc : instead of `new` in C++
        root->value = value;
        root->left = NULL;
        root->right = NULL;

        return root;
    }
    else
    {
        if (root->value > value) root->left = insert(root->left, value);
        else root->right = insert(root->right, value);
    }

    return root;
}

Node* delete(Node* root, int value) 
{
    if (root == NULL) return root;

    if (root->value > value) root->left = delete(root->left, value);
    else if (root->value < value) root->right = delete(root->right, value);
    else
    {
        // ing~~~
    }

    return root;
}
```
`delete()` is still imcomplete.
```c
void preOrder(Node* root)
{
    if (root == NULL) return;

    printf("%d ", root->value);
    preOrder(root->left);
    preOrder(root->right);
}

void inOrder(Node* root)
{
    if (root == NULL) return;

    inOrder(root->left);
    printf("%d ", root->value);
    inOrder(root->right);
}

void postOrder(Node* root)
{
    if (root == NULL) return;

    postOrder(root->left);
    postOrder(root->right);
    printf("%d ", root->value);
}
```
I wrote all the inside function names as `preOrder()` …… crazy~~~
```c
int main()
{
    Node* root = NULL;

    int arr[6] = {6, 3, 4, 7, 13, 10};
    int len = sizeof(arr) / sizeof(int);
    for (int i = 0; i < len; i++) root = insert(root, arr[i]);

    printf("Preorder traversal : ");
    preOrder(root);
    putchar('\n');

    printf("Inorder traversal : ");
    inOrder(root);
    putchar('\n');

    printf("Postorder traversal : ");
    postOrder(root);
    putchar('\n');

    return 0;
}
```

#### Output
```
Preorder traversal : 6 3 4 7 13 10
Inorder traversal : 3 4 6 7 10 13
Postorder traversal : 4 3 10 13 7 6
```


## [Binary Search 0 (2022.02.11)](#list)

- hope `binary_search()` in *C++* would be a free lunch ……  
  but it just returns only `true` or `false` depending on the element's presence.
- Of course, this function seems very **powerful** for sorted data.

#### `BinarySearch.cpp`
```cpp
#include <iostream>
#include <vector>
#include <algorithm>
```
```cpp
int main()
{
    vector<int> vec = {2, 4, 6, 8, 10, 12};                     // should be sorted
    vector<int> vec2 = {3, 6, 9, 12};

    for (auto v : vec2)
    {
        // binary_search() : a function to just return true or false if the value exists
        bool ans = binary_search(vec.begin(), vec.end(), v);
        cout << v << ' ' << ans << endl;
    }

    return 0;
}
```

#### Output
```
3 0
6 1
9 0
12 1
```


## [Increment and Decrement Operators (2022.02.01)](#list)

- Some extreme(?) experiments about `++` and `--` operators

#### `IncDecOperator.c`
```c
int main()
{
    int a = 1, b = 1, c = 1, d = 1, e = 1, f = 1;

    a++;
    --b;
    // no problem

    c = ++c;
    d = d++;
    // gcc - no problem
    // clang - warning: multiple unsequenced modifications to 'c' [-Wunsequenced]

    // e = ++e--;
    // ++e--;
    // f++--++;
    // f++++++;
    // gcc - error: lvalue required as increment operand
    // clang - error: expression is not assignable

    printf("Good-bye %d %d %d %d\n", a, b, c, d);

    return 0;
}
```

#### Output
```
Good-bye 2 0 2 1
```


## [Prevent Garbage Value (2022.01.21)](#list)

- The way to prevent variable declaration from garbage value

#### `PreventGarbageValue.cpp`
```cpp
int main()
{
    int garbage;
    int noGarbage{};

    cout << garbage << endl;
    cout << noGarbage << endl;

    return 0;
}
```

#### Output
```
2686816
0
```


## [Containers : Deque, Stack and Queue (2021.10.14)](#list)

- `STL` Practice : Container `Deque` and its adaptors `Stack` and `Queue`
- Especially `Deque` is something greater than `vector` and `list`
- `Prior Queue` that is also one of the container adaptor from Deque and consists of `heap` will be continued ……
- Reference ☞ [코딩 테스트를 위한 자료 구조와 알고리즘 with C++ (길벗, 2020)](https://github.com/gilbutITbook/080239)

#### `Containers_Deque.cpp`
```cpp
#include <deque>
```
```cpp
void print(deque<int> deq)
{
    for (auto it = deq.begin(); it != deq.end(); it++) cout << *it << ' ';
    cout << endl;
}
```
```cpp
int main()
{
    deque<int> deq {1, 2, 3, 4, 5};
    print(deq);

    deq.push_front(0);
    print(deq);

    deq.push_back(6);
    print(deq);

    deq.insert(deq.begin() + 2, 10);
    print(deq);

    deq.pop_back();
    print(deq);

    deq.pop_front();
    print(deq);

    deq.erase(deq.begin() + 1);
    print(deq);

    deq.erase(deq.begin() + 3, deq.end());
    print(deq);

    // emplace()?
    // emplace_front()?
    // emplace_back()?

    return 0;
}
```
> 1 2 3 4 5  
> 0 1 2 3 4 5  
> 0 1 2 3 4 5 6  
> 0 1 10 2 3 4 5 6  
> 0 1 10 2 3 4 5  
> 1 10 2 3 4 5  
> 1 2 3 4 5  
> 1 2 3  

#### `Containers_Stack.cpp`
```cpp
#include <stack>
```
```cpp
void print(stack<int> stk)
{
    if (stk.empty()) cout << "The stack is empty." << endl;
    else
    {
        while (!stk.empty())
        {
            cout << stk.top() << ' ';
            stk.pop();
        }
        cout << endl;
    }
}
```
```cpp
int main()
{
    stack<int> stk ({1, 2, 3});     // check the different way to declare with initial elements from deque and so on
    print(stk);

    stk.push(4);
    print(stk);

    stk.push(5);
    print(stk);

    stk.pop();
    stk.pop();
    print(stk);

    stk.pop();
    stk.pop();
    stk.pop();
    print(stk);

    // Any other methods?

    return 0;
}
```
> 3 2 1  
> 4 3 2 1  
> 5 4 3 2 1  
> 3 2 1  
> The stack is empty.

#### `Containers_Queue.cpp`
```cpp
#include <queue>
```
```cpp
void print(queue<int> q)
{
    if (q.empty()) cout << "The que is empty." << endl;
    else
    {
        while (!q.empty())
        {
            cout << q.front() << ' ';
            q.pop();
        }
        cout << endl;
    }
}
```
```cpp
int main()
{
    queue<int> q ({1, 2, 3});   // don't forget ()!
    print(q);

    q.push(4);
    print(q);

    q.push(5);
    print(q);

    q.pop();
    q.pop();
    print(q);

    q.pop();
    q.pop();
    q.pop();
    print(q);

    return 0;
}
```
> 1 2 3  
> 1 2 3 4  
> 1 2 3 4 5  
> 3 4 5  
> The que is empty.


## [Template (2021.07.23)](#list)

- Significantly advanced code using **template** from the previous `StackOverflow.cpp`
- I am so proud!

#### `Template.cpp`
```cpp
template <class T>
// void next (T a) cout << a++ << endl;       // can't write in a line without {}
void next (T a)
{
    if (typeid(a) == typeid((char) 'a') || typeid(a) == typeid((unsigned char) 'a'))
    {
        cout << typeid(a).name() << " : " << (int) a << " + 1 = " << (int) ++a << " (converted to ASCII value)" << endl;    
    } else
    {
        cout << typeid(a).name() << " : " << a << " + 1 = " << ++a << endl;
    }
    // there will be more alternatives like type_info and so on ……
}
```
```cpp
int main()
{
    next((char) CHAR_MAX);
    next((unsigned char) UCHAR_MAX);
    next((short) SHRT_MAX);
    next((unsigned short) USHRT_MAX);
    next((int) INT_MAX);
    next((unsigned int) UINT_MAX);
    next((bool) 1);                     // warning: use of an operand of type 'bool' in 'operator++' is deprecated

    return 0;
}
```

#### Output
> c : 127 + 1 = -128 (converted to ASCII value)  
> h : 255 + 1 = 0 (converted to ASCII value)  
> s : 32767 + 1 = -32768  
> t : 65535 + 1 = 0  
> i : 2147483647 + 1 = -2147483648  
> j : 4294967295 + 1 = 0  
> b : 1 + 1 = 1


## [Stack Overflow (2021.05.18)](#list)

- "Let's conquer the **stack overflow** problem!"
- …… a stupid conquerer who didn't know **template** and **generic function** said.
- Can he learn them or still stay in beginner's swamps? To be continued …… 

#### `StackOverflow.cpp`
```cpp
#include <iostream>

using namespace std;

int main()
{
    // char : -128 to 127 (-2^7 to 2^7 - 1)
    char chr1 = 126;
    char chr2 = chr1 + 1;
    char chr3 = chr2 + 1;
    cout << "char (" << sizeof(char) << ") : " << (short)chr1 << " + 1 = " << (short)chr2 << endl;          // 127
    cout << "char (" << sizeof(char) << ") : " << (short)chr2 << " + 1 = " << (short)chr3 << endl << endl;  // -128

    // unsigned char : 0 to 255 (0 to 2^8 - 1)
    unsigned char uChr1 = 254;
    unsigned char uChr2 = uChr1 + 1;
    unsigned char uChr3 = uChr2 + 1;
    cout << "unsigned char (" << sizeof(unsigned char) << ") : " << (short)uChr1 << " + 1 = " << (short)uChr2 << endl;          // 255
    cout << "unsigned char (" << sizeof(unsigned char) << ") : " << (short)uChr2 << " + 1 = " << (short)uChr3  << endl << endl; // 0

    // short : -32768 to 32767 (-2^15 to 2^15 - 1)
    short shrt1 = 32766;
    short shrt2 = shrt1 + 1;
    short shrt3 = shrt2 + 1;
    cout << "short (" << sizeof(short) << ") : " << shrt1 << " + 1 = " << shrt2 << endl;            // 32767
    cout << "short (" << sizeof(short) << ") : " << shrt2 << " + 1 = " << shrt3 << endl << endl;    // -32768

    // unsigned short : 0 to 65535 (0 to 2^16-1)
    unsigned short uShrt1 = 65534;
    unsigned short uShrt2 = uShrt1 + 1;
    unsigned short uShrt3 = uShrt2 + 1;
    cout << "unsigned short (" << sizeof(unsigned short) << ") : " << uShrt1 << " + 1 = " << uShrt2 << endl;            // 65535
    cout << "unsigned short (" << sizeof(unsigned short) << ") : " << uShrt2 << " + 1 = " << uShrt3 << endl << endl;    // 0

    // int : -214748368 to 214748367 (-2^31 to 2^31 - 1)
    int int1 = 2147483646;
    int int2 = int1 + 1;
    int int3 = int2 + 1;
    cout << "int (" << sizeof(int) << ") : " << int1 << " + 1 = " << int2 << endl;          // 2147483647
    cout << "int (" << sizeof(int) << ") : " << int2 << " + 1 = " << int3 << endl << endl;  // -2147483648
    
    // unsigned int : 0 to 4294967295 (0 to 2^32 -1)
    unsigned int uIint1 = 4294967294;
    unsigned int uIint2 = uIint1 + 1;
    unsigned int uIint3 = uIint2 + 1;
    cout << "unsigned int (" << sizeof(unsigned int) << ") : " << uIint1 << " + 1 = " << uIint2 << endl;            // 4294967295
    cout << "unsigned int (" << sizeof(unsigned int) << ") : " << uIint2 << " + 1 = " << uIint3 << endl << endl;    // 0

    // bool : 0 to 1
    bool bl1 = false;
    bool bl2 = bl1 + 1;
    bool bl3 = bl2 + 1;
    cout << "bool (" << sizeof(bool) << ") : " << bl1 << " + 1 = " << bl2 << endl;          // 1
    cout << "bool (" << sizeof(bool) << ") : " << bl2 << " + 1 = " << (bool)(bl3) << endl;  // 1

    return 0;
}
```

#### Output
> char (1) : 126 + 1 = 127  
> char (1) : 127 + 1 = -128  
>  
> unsigned char (1) : 254 + 1 = 255  
> unsigned char (1) : 255 + 1 = 0  
>  
> short (2) : 32766 + 1 = 32767  
> short (2) : 32767 + 1 = -32768  
>  
> unsigned short (2) : 65534 + 1 = 65535  
> unsigned short (2) : 65535 + 1 = 0  
>  
> int (4) : 2147483646 + 1 = 2147483647  
> int (4) : 2147483647 + 1 = -2147483648  
>  
> unsigned int (4) : 4294967294 + 1 = 4294967295  
> unsigned int (4) : 4294967295 + 1 = 0  
>  
> bool (1) : 0 + 1 = 1  
> bool (1) : 1 + 1 = 1


## [Hello World (2021.05.12)](#list)

- My first run of **`C`/`C++`** code in **Visual Studio Code**
- Environmental setting was harder than coding
- Find how to **complie** and **run** in cosole (rather easier than VS Code menu)
- `gcc` (for `C`) and `g++` (for `C++`) seem not so different to each other

#### `IamYourFather_c.c`
```c
#include <stdio.h>
#include <windows.h>    // for using system()

int main()
{
    printf("I am your father.\n");
    // system("pause");
    return 0;
}
```

##### Command Line
```
gcc --help
gcc -S IamYourFather_c.c
gcc IamYourFather_c.c -o IamYourFather_c.exe
```
```
.\IamYourFather_c
```
> I am your father.

#### `IamYourFather_cpp.cpp`
```cpp
#include <iostream>

using namespace std;

int main()
{
    cout << "I am your father." << endl;
    // system("pause");
    return 0;
}
```

##### Command Line
```
g++ --help
g++ -S IamYourFather_cpp.cpp
g++ IamYourFather_cpp.cpp -o IamYourFather_cpp.exe
```
```
.\IamYourFather_cpp
```
> I am your father.