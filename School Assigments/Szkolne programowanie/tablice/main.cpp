#include <iostream>

using namespace std;

void wypelnij(int tab[10])
{
    for(int i=0; i<10;i++){
        cout<<"Wpisz "<<i+1<<" liczbe: ";
        cin>>tab[i];
    }
}
void wyswietl(int tab[10]){
for(int i=0;i<10;i++){
    cout<<tab[i]<<" ";
}
}
int main()
{
    int tablica[10];
    wypelnij(tablica);
    wyswietl(tablica);
    return 0;
}
