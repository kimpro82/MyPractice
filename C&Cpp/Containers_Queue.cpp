// Containers : Queue (FIFO; First-In First-Out)

#include <iostream>
#include <stack>

using namespace std;

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

int main()
{
    // stack<int> stk {1, 2, 3, 4, 5};  // seems impossible to declare with initial elements
    stack<int> stk;
    print(stk);

    stk.push(1);
    print(stk);

    stk.push(2);
    print(stk);

    stk.pop();
    print(stk);

    stk.pop();
    print(stk);

    // Any other methods?

    return 0;
}