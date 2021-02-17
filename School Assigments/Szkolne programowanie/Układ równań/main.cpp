#include <iostream>

using namespace std;
float x1,x2,y1,y2,w1,w2;
void wyswietl(float x1, float y1, float x2, float y2, float w1, float w2)
{
    if(y1< 0 && y2 > 0)
         cout<<x1<<"x "<<y1<<"y = "<<w1<<"\n"<<x2<<"x + "<<y2<<"y = "<<w2;
    else if(y1<0 && y2< 0)
         cout<<x1<<"x "<<y1<<"y = "<<w1<<"\n"<<x2<<"x "<<y2<<"y = "<<w2;
    else if(y1>0 && y2<0)
         cout<<x1<<"x + "<<y1<<"y = "<<w1<<"\n"<<x2<<"x "<<y2<<"y = "<<w2;
    else
        cout<<x1<<"x + "<<y1<<"y = "<<w1<<"\n"<<x2<<"x + "<<y2<<"y = "<<w2;

}
float wyznacznik(float x1, float y1, float x2, float y2)
{
    return (x1*y2)-(x2*y1);
}

float wynik(float wyznacznik_g, float wyznacznik)
{
    return wyznacznik/wyznacznik_g;
}
void rozwiazanie()
{
    if(wyznacznik(x1,x2,y1,y2)!= 0)
    {
        cout<<endl<<"X = "<<wynik(wyznacznik(x1,x2,y1,y2),wyznacznik(w1,y1,w2,y2));
        cout<<endl<<"Y = "<<wynik(wyznacznik(x1,x2,y1,y2),wyznacznik(x1,w1,x2,w2));
    }
    else if((wyznacznik(w1,y1,w2,y2) == 0) && (wyznacznik(x1,w1,x2,w2) == 0 )){
    cout<<"\nTozsamosciowe";}
    else{
        cout<<"\nSprzeczne!";}
}
int main()
{
    setlocale( LC_ALL, "" );

    cout<<"Podaj wartosc przed x w pierwszej linijce: ";
    cin>>x1;
    cout<<"Podaj wartosc przed y w pierwszej linijce: ";
    cin>>y1;
    cout<<"Podaj wynik w pierwszej linijce: ";
    cin>>w1;
    cout<<"Podaj wartosc przed x w drugiej linijce: ";
    cin>>x2;
    cout<<"Podaj wartosc przed y w drugiej linijce: ";
    cin>>y2;
    cout<<"Podaj wynik w drugiej linijce: ";
    cin>>w2;
    wyswietl(x1,y1,x2,y2,w1,w2);
    cout<<endl<<"Wyznacznik glowny: "<<wyznacznik(x1,x2,y1,y2);
    cout<<endl<<"Wyznacznik x: "<<wyznacznik(w1,y1,w2,y2);
    cout<<endl<<"Wyznacznik y: "<<wyznacznik(x1,w1,x2,w2);
    rozwiazanie();
    return 0;
}
