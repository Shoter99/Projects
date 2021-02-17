#include <iostream>

using namespace std;
float modul(float a)
{
    if(a < 0){
        return -a;
    }else return a;
}
float odleglosc(float a, float b)
{
    return a+b;
}
void liniowe(float a, float b)
{
    if( a != 0)
    cout<< -b/a;
    else if (b!=0)
        cout<<"Rownanie sperzeczne";
    else cout<<"Nieskonczenie wiele rozwiazan";
}
int main()
{
    float a, b;
    cout<<"Podaj dwie liczby: ";
    cin>>a>>b;

    cout<<odleglosc(modul(a),modul(b))<<endl;
    liniowe(a,b);
    return 0;
}
