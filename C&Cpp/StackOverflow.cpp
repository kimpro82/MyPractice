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

// Improvement point : find how to use a function for repetitive works → template & generic function!