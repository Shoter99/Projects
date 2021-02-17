#include <iostream>
#include<cmath>
using namespace std;

string koniec;

void dane(float &a, float &b, float &c)
{
    cout<<"Podaj a,b,c: ";
    cin>>a>>b>>c;
}
float delta(float &a, float &b, float &c)
{
    return ((b*b)+(-4*a*c));
}
void zerowe(float &a, float &b, float &c)
{
    int x1,x2;
    int x1L,x2L,mianownik;
    x1L = (-b-sqrt(delta(a,b,c)));
    x2L = (-b+sqrt(delta(a,b,c)));
    mianownik = 2*a;
    cout<<"Pierwiastek z delty wynosi: "<<sqrt(delta(a,b,c))<<endl<<endl;
    cout<<"Pierwsze miejsce zerowe: \nlicznik: "<<x1L<<"\nmianownik: "<<mianownik<<endl<<"\nDrugie miejsce zerowe: \nlicznik: "<<x2L<<"\nmianownik: "<<mianownik<<endl<<endl;
    x1 = ((-b-sqrt(delta(a,b,c)))/(2*a));
    x2 = ((-b+sqrt(delta(a,b,c)))/(2*a));
    cout<<"Pierwsze miejsce zerowe wynosi: "<<x1<<"\ndrugie miejsce zerowe wynosi: "<<x2<<endl;
}

int main()
{
    while(koniec!= "koniec"){
    float a,b,c;
    dane(a,b,c);
    cout<<"Delta wynosi: "<<delta(a,b,c)<<endl;
    zerowe(a,b,c);
    cin>>koniec;
    }
    return 0;
}
