#include <iostream>
#include <math.h>
using namespace std;

float boka, bokb, bokc;
void sprawdz(float a, float b, float c){
    if((a+b > c) && (a+c > b) && (b+ c > a)){
        cout<<"Istnieje taki trojkat\n";
        double p = (a+b+c)/2;
        double pole = sqrt(p*(p-a)*(p-b)*(p-c));
        cout<<"Pole trojkata wynosi: "<<pole<<endl;
    }else{
    cout<<"Nie istnieje taki trojkat";}
}
int main()
{
    cout<<"Podaj trzy boki trojkata: \n";
    cin >> boka>>bokb>>bokc;
    sprawdz(boka,bokb,bokc);
    return 0;
}
