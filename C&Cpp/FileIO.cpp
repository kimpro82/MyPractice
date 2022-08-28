#include <iostream>
#include <fstream>
#define endl '\n'

using namespace std;

int main()
{
    // Write file
    ofstream ofs;
    ofs.open("FileIO.txt", ios::out);           // ios::out : make a new empty file
    ofs << "My wife is crazy." << endl;
    ofs << "Really crazy." << endl;
    ofs.close();

    // Read file
    ifstream ifs;
    string line;
    ifs.open("FileIO.txt", ios::in);            // ios::in : read-only
    while(getline(ifs, line)) cout << line << endl;
    ifs.close();

    return 0;
}