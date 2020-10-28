#include <iostream>
using namespace std;
int km[3] = {12,14,18};

float zamien(int eu){
    return eu*4.28;
}
string porownaj(int cgrecja, int cpolska){
	cgrecja = cgrecja*4.28;
	if(cgrecja< cpolska){
		return "Cena w Grecji jest mniejsza";
	}else if (cgrecja > cpolska){
		return "Cena w Grecji jest wieksza";
	}else if (cgrecja == cpolska){
		return "Ceny sa identyczne";
	}
}
float srednia(int a,int b,int c){
return (a+b+c)/3;}
float jak_szybko(float t){
return t*1320;}
float zamiana(float m){
    return m*1.609;
}
int godzina(int n){
return (21 + n)%24;
}
int godz_ny(int g){
return (18+g)%24;}
int skala(float v){
    return (v+10)/6;
}

int main() {
        /*
        cout<<zamien(126);

        cout<<porownaj(49,200);

        cout<<srednia(12,14,18);

        cout<<jak_szybko(2.5)<<endl;
        cout<<jak_szybko(3);

        cout<<zamiana(10)<<endl;
        cout<<zamiana(12);

        cout<<godzina(14)<<endl;
        cout<<godzina(20);
*/
        cout<<godz_ny(18)<<endl;
        cout<<godz_ny(2);
/*
        cout<<skala(5)<<endl;
        cout<<skala(52);

*/
		return 0;
}
