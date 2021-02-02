#include <iostream>

using namespace std;

string PIN;

int main()
{
    cout << "PIN: ";
    cin >> PIN;

    if (PIN=="2017")
    {
        cout<< "Good PIN";
    }
    else
    {
        cout<< "Bad PIN";
    }
    return 0;
}
