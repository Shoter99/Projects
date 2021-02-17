#include <iostream>

using namespace std;
void wyswietl(char &z)
{
    cout<<"Wybierz jedna z opcji \n + zeby dodac libczy \n - zeby odjac pierwsza liczbe od drugiej \n * zeby pomnozyc liczby \n / zeby podzielic pierwsza przez druga \n";
    cin>>z;
}
void oblicz(int a, int b, char z)
{
    switch(z){
case '+':
    cout<<a<<"+"<<b<<" = "<<a+b<<endl;
    break;
case '-':
    cout<<a<<"-"<<b<<" = "<<a-b<<endl;
    break;
case '*':
    cout<<a<<"*"<<b<<" = "<<a*b<<endl;
    break;
case '/':
    cout<<a<<"/"<<b<<" = "<<a/b<<endl;
    break;
}}
int main()
{
    string koniec;
    cout << "Witaj w kalkulatorze!" << endl;
    while (koniec != "tak"){
    char z;

    float a,b;
    cout<<"Podaj dwie liczby: ";
    cin>>a>>b;
    wyswietl(z);
    oblicz(a,b,z);
    cout<<"Koniec (nie/tak)\n";
    cin>>koniec;

    }
    return 0;
}
