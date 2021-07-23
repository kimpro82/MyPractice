#include <iostream>

using namespace std;

#define endl '\n'

template <class T>
// void next (T a) cout << a++ << endl;       // can't write in a line without {}
void next (T a)
{
    cout << a << " + 1 = " << ++a << endl;
}

int main()
{
    next((char) 127);
    next((short) 32767);
    next((unsigned short) 65535);
    next((int) 214748367);
    next((unsigned int) 4294967295);
    next((bool) 1);                     // warning: use of an operand of type 'bool' in 'operator++' is deprecated

    // char : -128 to 127 (-2^7 to 2^7 - 1)
    char chr1 = 126;
    char chr2 = chr1 + 1;
    char chr3 = chr2 + 1;
    cout << "char (" << sizeof(char) << ") : " << (short)chr1 << " + 1 = " << (short)chr2 << endl;          // 127
    cout << "char (" << sizeof(char) << ") : " << (short)chr2 << " + 1 = " << (short)chr3 << endl << endl;  // -128

    // unsigned char : 0 to 255 (0 to 2^8 - 1)
    // short : -32768 to 32767 (-2^15 to 2^15 - 1)
    // unsigned short : 0 to 65535 (0 to 2^16-1)
    // int : -214748368 to 214748367 (-2^31 to 2^31 - 1)   
    // unsigned int : 0 to 4294967295 (0 to 2^32 -1)
    // bool : 0 to 1

    return 0;
}
