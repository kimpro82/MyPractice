#include <iostream>

using namespace std;

#define endl '\n'

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
