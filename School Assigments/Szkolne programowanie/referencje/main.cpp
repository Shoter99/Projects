#include <iostream>

using namespace std;
void zamien(float&a, float &b)
{
    float pomoc;
    if(a < b)
    {
        pomoc = a;
        a = b;
        b = pomoc;
    }

}
void zamien3(float &a, float &b)
{
    float pomoc;
    if(a > b)
    {
        pomoc = a;
        a = b;
        b = pomoc;

}}
void wynik(float &a, float &b, float &c)
{
    zamien3(a,b);
    zamien3(a,c);
    zamien3(b,c);
}
int main()
{
    float a, b,c;
    cout<<"Wpisz a i b i c: ";
    cin>>a>>b>>c;
    cout<<a<<" "<<b<<" "<<c<<endl;
    wynik(a,b,c);
    cout<<a<<" "<<b<<" "<<c<<endl;
    return 0;
}
