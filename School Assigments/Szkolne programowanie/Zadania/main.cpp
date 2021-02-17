#include <iostream>

using namespace std;
void wprowadz(float tab[10])
{
    for(int i=0;i<10;i++){
        cout<<"Podaj "<<i+1<<" liczbe: ";
         cin>>tab[i];
    }
}
void wypisz(float tab[10])
{
    for(int i;i>=0;i--)
    {
        cout<<tab[i-1]<<endl;
    }
}
void wpisz(int tab[8])
{
    for(int i=0;i<8;i++){
        cout<<"Wpisz "<<i+1<<" liczbe: ";
        cin>>tab[i];
    }
}
void zero(int tab[8])
{
    bool zero ;
     for(int i=0;i<8;i++){
        if(tab[i] == 0)
        {
            cout<<"Zero znajduje sie na "<<i<<" miejscu";
            zero = true;
        }

    }
    if(zero == false) cout<<"Nie ma zera";
}

int main()
{
    /*float tablica[10];
    wprowadz(tablica);
    wypisz(tablica);*/
    int tabl[8];
    wpisz(tabl);
    zero(tabl);
    return 0;
}
