#include <iostream>
#include <cstring>
using namespace std;
void wyrazy()
{
    char litera[50];
    int ile=0;
    cout<<"Podaj zdanie: ";
    cin.getline(litera,50);
    for(int i=0; litera[i] != '\0';i++)
    {
        if(litera[i]==' ' || litera[i]=='.')
            ile++;
    }

    cout<<"Liczba wyrazow w zdaniu: "<<ile;
}
void palidrom()
{
     char zdanie[100];
    string pali;
    bool jest=true;
    cout<<"Podaj zdanie: ";
    gets(zdanie);
    for(int i=0;zdanie[i] != '\0';i++) //Przejscie przez wszyskie znaki wpisane z kalwaitury
    {
        if(zdanie[i]!=' ')//podzial tekstu na wyrazy
           pali= pali+zdanie[i];
        else
        {

            for(int j=0;j<pali.size();j++)//sprwadzenie czy wyraz to palidrom
            {
                if(pali[j] != pali[pali.size()-j-1])
                {
                 jest=false;
                 break;
                }
            }
            if(jest==true)
            {
                cout<<pali<<" ";
                pali = "";
            }
            else
            {jest=true;
             pali="";
            }


        }
    }

}
void oddzielnie()
{
    char zdanie[300];
    cout<<"Podaj zdanie: ";
    cin.getline(zdanie, 300);
    for(int i=0;zdanie[i] != '.';i++)
    {
        if(zdanie[i]!=' ')
            cout<<zdanie[i];
        else
            cout<<endl;
    }
}
int main()
{
    wyrazy();
    return 0;
}
