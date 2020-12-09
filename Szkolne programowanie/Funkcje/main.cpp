#include <iostream>

using namespace std;
int a, b;


void wyswietl(){
cout<<"Bok kwadratu wynosi: "<<a;}
float pole(){
return a*a;}
float pole_prostokata(){
return a*b;}

int main()
{

    cout<<"Podaj a i b: ";
    cin>>a>>b;
    wyswietl();
    cout<<"\nPole kwadratu wynosi: "<<pole()<<"\nPole prostokata wynosi: "<<pole_prostokata();
    return 0;
}
