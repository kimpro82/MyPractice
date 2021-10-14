// Containers : Deque (Double-Ended Queue) - more than vector and list

#include <iostream>
#include <deque>

using namespace std;

void print(deque<int> deq)
{
    for (auto it = deq.begin(); it != deq.end(); it++) cout << *it << ' ';
    cout << endl;
}

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

    return 0;
}