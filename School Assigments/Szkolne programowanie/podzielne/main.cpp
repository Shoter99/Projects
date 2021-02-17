#include <iostream>
#include<string>
//wczytaj n liczb z klawiatury
//podaj podzielne przez trzy

using namespace std;

int main() {
int n, x;
x = 0;
cout <<"Podaj n: ";
cin >>n;
string wynik;
for(int i = 1; i <= n; i++)
{
    cout<<"Wpisz "<<i<<" liczb: ";
    int liczba;
    cin>>liczba;
//reszta z dzielenia przez 3 musi równac sie zero
    if(liczba%3==0)
    {
        wynik = wynik.append(to_string(liczba));
        x += 1;
    }
}
cout<<"Liczy ktore sa podzielne przez trzy: "<<wynik;
cout<<"\nJest ich: "<<x;
return 0;
}

