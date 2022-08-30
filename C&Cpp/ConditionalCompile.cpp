#include <iostream>
#include <fstream>
#define endl '\n'

using namespace std;

int main()
{
    string txt = "I am your father.";

    #ifdef fileio
        ofstream ofs;
        string fileName = "ConditionalCompile.txt";
        ofs.open(fileName, ios::out);           // ios::out : make a new empty file
        ofs << txt << endl;
        ofs.close();
        cout << fileName << " has been generated." << endl;
    #else
        cout << txt << endl;
    #endif

    return 0;
}