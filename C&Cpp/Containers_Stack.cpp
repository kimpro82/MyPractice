// Containers : Stack (LIFO; Last-In First-Out)

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