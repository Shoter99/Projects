#include <iostream>

using namespace std;
void ramka()
{
        int w, k;
    cout <<"Wpisz liczbe wierszy i kolumn: ";
    cin >> w >> k;
    for(int i = 0; i < k; i++)
    {
        cout<<"* ";
    }cout<<endl;
    for(int i =0; i < (w-2); i++){
        cout<<"*";
        for(int j=0; j<(2*k-3);j++){
            cout<<" ";
        }cout<<"*"<<endl;
    }
    for(int i =0; i< k; i++){
        cout<<"* ";
    }
}
void przekatna()
{

    int a;

cout<<"Podaj bok kwardratu: ";
cin>>a;
for(int i = 0; i<a;i++){

  for(int j = a+i;a<j;j--){
    cout<<"  ";
  }

cout<<"#"<<endl;
}
}
void odprzekatna(){

       int a;

cout<<"Podaj bok kwardratu: ";
cin>>a;
for(int i = a; i>0;i--){

  for(int j = a+i;a<j;j--){
    cout<<"  ";
  }

cout<<"#"<<endl;
}
}
void tabliczka(){
    cout<<"        ";
for(int i=1;i<10;i++){
    cout<<"j="<<i<<"    ";
}cout<<endl;
    for(int i=1;i<10;i++){
            cout<<"i = "<<i;
        for(int j=1;j<10;j++){
            cout.width(6);

            cout<<i*j<<" ";
        }
        cout<<endl;
    }
}
void silnia(){
long long silnia = 1;
int n;
cout<<"Podaj n: ";
cin>>n;
for(int i =1; i<=n;i++){
    silnia=silnia*i;

}
cout<<"Silnia: "<<silnia;
}
void potega(){
int x,n, i;
cout<<"Podaj x i n: ";
cin>>x>>n;
for(i =1;n>0;n--){
    i = i*x;
}
cout<<i<<endl;
}
int main()
{
    potega();
    return 0;
}
