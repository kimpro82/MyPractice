#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

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