#include <iostream>

using namespace std;
float wynik;
string grupaA(float w){
    if(wynik >= 0 && wynik < 30){
        return "podstawowa";
    }else if(wynik >= 30 && wynik < 60){
    return "zaawansowana";}
    else { return "Wprowadzno zly wynik";}

}
string grupaB(float w){
    if(wynik >= 0 && wynik < 20){
        return "podstawowa";
    }else if(wynik >= 20 && wynik < 40){
    return "sredniozaawansowana";}
        else if(wynik >= 40 && wynik < 60){
    return "zaawansowana";}
    else { return "Wprowadzno zly wynik";}
}
int main()
{   cout<< "Wpisz wynik: ";
    cin >> wynik;
    cout <<"Twoja grupa to: "<< grupaA(wynik)<<endl;
    cout <<"Twoja grupa to: "<< grupaB(wynik);
    return 0;
}
