#include <iostream>
#include <cstdlib>
using namespace std;
void srednia(){
    float a, b;
    cout<<"Podaj dwie liczby: ";
    cin >> a >> b;
    cout << (a+b)/2<<endl;
}
void modul(){
    float a;
    cout<<"Podaj wartosc: ";
    cin >> a;
    if (a < 0) cout<<"Wartosc bezwzgledana liczby wynosi: "<< -a<<endl;
    else cout<<"Wartosc bezwzgledana liczby wynosi: "<<a<<endl;

}
void rysuj()
{
    int a,b;
    cout<<"Podaj a i b: ";
    cin >> a >> b;
    for (int i =0; i<a;i++){
        for(int j = 0; j<b;j++){
            cout<<"*";
        }
        cout<<endl;
    }
}
void ilocz(){
int i, a, iloczyn, n;
cout<<"Ile liczb chcesz pomnozyc"<<endl;
cin >> n;
iloczyn = 1;
for (i=0;i<n;i++)
{
    cout<< "Podaj liczbe: \n";
    cin >>a;
    iloczyn*=a;
}
cout<<"Iloczyn tych liczb wynosi: "<<iloczyn;
}
void kolejno(){
float a, b ,c;
	cout << "Podaj trzy liczby" << endl;
	cin>>a>>b>>c;
	if (a<b)
		{if (c<a) cout <<c<<a<<b;
		else if (c<b) cout <<a<<c<<b;
		else cout <<a<<b<<c;}
	else if (c<b)
{cout<<c<<b<<a;}
		else if (c<a) cout<<b<<c<<a;
		else cout <<b<<a<<c;}


void sortuj(){
    float a, b, c;
    cout<<"Podaj 3 wartosci: ";
    cin >>a >>b>>c;
    if (a < b){
        if (a< c){
            if(b<c){
                cout<<"Kolejnosc to: "<<a<<" "<<b<<" "<<c<<endl;
                    }else{cout<<"Kolejnosc to: "<<a<<" "<<c<<" "<<b<<endl;}
                        }else{cout<<"Kolejnosc to: "<<c<<" "<<a<<" "<<b<<endl;}
    }else if (b<c){
        if (a<c){cout<<"Kolejnosc to: "<<b<<" "<<a<<" "<<c<<endl;
            }else{cout<<"Kolejnosc to: "<<b<<" "<<c<<" "<<a<<endl;}
                }else cout<<"Kolejnosc to: "<<c<<" "<<b<<" "<<a<<endl;
    }
int main()
{
    kolejno();
    return 0;
}
