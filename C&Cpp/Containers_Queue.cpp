// Containers : Queue (FIFO; First-In First-Out)

#include <iostream>
#include <queue>

using namespace std;

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