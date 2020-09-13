#include <iostream>
#include "pytanie.h"
#include <fstream>
#include <cstdlib>


using namespace std;

void Pytanie::wczytaj()
{
    fstream plik;
    plik.open("quiz.txt", ios::in);

    if(plik.good()== false)
    {
        cout<<"Nie udalo sie otworzyc pliku!";
        exit(0);
    }

    int nr_linii = (nr_pytania-1)*6+1;
    int akt_nr=1;
    string linia;

    while(getline(plik,linia))
    {
        if(akt_nr==nr_linii) tresc=linia;
        if(akt_nr==nr_linii+1) a=linia;
        if(akt_nr==nr_linii+2) b=linia;
        if(akt_nr==nr_linii+3) c=linia;
        if(akt_nr==nr_linii+4) d=linia;
        if(akt_nr==nr_linii+5) poprawna=linia;
        akt_nr++;
    }
    plik.close();

}
void Pytanie::zadaj()
{
    cout<<tresc+"\n a) "+a+"\n b) "+b+"\n c) "+c+"\n d) "+d+"\n";
    cout<<"-------------------";
    cout<<"\n Odpowiedz: ";
    cin>>odpowiedz;
}
void Pytanie::sprawdz()
{
    if (odpowiedz == poprawna){
        punkt = 1;
    }else punkt = 0;

}
