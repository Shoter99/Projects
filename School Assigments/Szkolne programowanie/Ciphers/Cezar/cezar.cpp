#include <iostream>
#include <string>
using namespace std;

int silnia(int x)
{
    if (x == 0 || x == 1)
        return 1;
    return x * silnia(x - 1);
}

int main()
{
    double number;
    string end;
    while (true)
    {
        cout << "Podaj liczbę z której program ma obliczyc silnie: ";
        cin >> number;
        cout << silnia(number) << "\n";
        cout << "Czy chcesz zakończyć program? (tak/nie)";
        cin >> end;
        if (end == "tak")
            break;
    }
    return 0;
}