#include <iostream>
#include "headers.h"

using namespace std;

float Zadania::zamien(int eu){
return eu*4.28;}
float Zadania::srednia(int a, int b, int c){
return (a+b+c)/3;}
float Zadania::jak_szybko(float t){
return t*1320;}
float Zadania::zamiana(float m){
return m*1.609;}
string Zadania::porownaj(int cgrecja, int cpolska){
	cgrecja = cgrecja*4.28;
	if(cgrecja< cpolska){
		return "Cena w Grecji jest mniejsza";
	}else if (cgrecja > cpolska){
		return "Cena w Grecji jest wieksza";
	}else if (cgrecja == cpolska){
		return "Ceny sa identyczne";
	}}
int Zadania::godzina(int n){
return (21 +n)%24;}
int Zadania::godz_ny(int g){
return (18+g)%24;}
