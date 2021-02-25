#include <iostream>

using namespace std;
void wyswietl(){
    //n ilosc znakow ktore sie wyswietla
int n;
//znak ktory sie wyswietli
char znak;
    cout<<"Jaki znak wyswietlic: ";
    cin>>znak;
    cout<<"Podaj ile znakow wyswietlic poziomo i pionowo\n";
    cin >> n;
//petla wyswietla poziomo znaki
    for(int i = 0; i<n;i++){
        cout<<znak;
    }
    cout<<"\n\n\n";
//petla wyswietla pionowo znaki
    for(int i=0;i<n;i++){
        cout<<znak<<"\n";
    }
}
void rysuj(){
int wiersz,kolumna;
    char znak;
    cout<<"Podaj ilosc wierszy i kolumn: ";
    cin>>wiersz>>kolumna;
    cout<<"Podaj jaki znak uzyc: ";
    cin >> znak;

    for(int i = 0; i<wiersz;i++)
    {
        for(int j = 0; j<kolumna;j++){
            cout<<znak;
        }
        cout<<"\n";
    }
}
void trojkat(){

}
int main()
{
    int h;
    cin >> h;
    for(int i= 0;i<h;i++){
        for(int j =3; j>i; j--){
            cout<<"$";
            }
        for(int z =2;z<j;z++){
            cout<<"#";
        }

        cout<<endl;}

    return 0;
}
