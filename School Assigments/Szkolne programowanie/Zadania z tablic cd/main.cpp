#include <iostream>
#include<cstring>
using namespace std;
void zamien()
{
     char napis[256];
    int spacja=0,kropka=0,a=0,z=0;
    cout<<"Podaj tekst: ";
    gets(napis);
    int d = strlen(napis);
    cout<<d;
    for(int i=0;i<d;i++)
    {
        if(napis[i]==' ')
        {
            spacja++;
        }
        if(napis[i]=='.')
        {
            kropka++;
        }
        if(napis[i]=='a')
        {
            a++;
        }
        if(napis[i]=='z')
        {
            z++;
        }
    }
    cout<<"Spacja: "<<spacja<<" Kropka: "<<kropka<<" A: "<<a<<" Z: "<<z;
}
void nazwisko()
{
    string imie, nazwisko;
    cout<<"Podaj imie i nazwisko: ";
    cin>>imie>>nazwisko;
    cout<<"Wpisz i jezeli napisac ma twoje imie\nWpisz n jezeli napisac ma twoje nazwisko\n";
    char znak;
    cin>>znak;
    switch(znak)
    {
    case 'i':
        cout<<"Twoje imie to: "<<imie;
        break;
    case 'n':
        cout<<"Twoje nazwisko to: "<<nazwisko;
        break;
    default:
        cout<<"Bledy znak!";
        break;
    }
}
void imie()
{
    string imie;
    cout<<"Podaj imie: ";
    cin>>imie;
    int d=imie.size();
    if(imie[d-1]=='a') cout<<"To imie jest zenskie";
    else cout<<"To imie jest meskie";
}
int main()
{
    imie();
    return 0;
}
