#include <iostream>
#include <cstring>
using namespace std;
void wyrazy()
{
       char litera[50];
    int ile=0;
    cout<<"Podaj zdanie: ";
    cin.getline(litera,50);
    for(int i=0; litera[i] != '.';i++)
    {
        if(litera[i]==' ')
            ile++;
    }

    cout<<"Liczba wyrazow w zdaniu: "<<ile+1;
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
    char zdanie[100];
    string pali;
    bool jest=true;
    cout<<"Podaj zdanie: ";
    gets(zdanie);
    for(int i=0;zdanie[i] != '\0';i++)
    {
        if(zdanie[i]!=' ')
           pali= pali+zdanie[i];
        else
        {

            for(int j=0;j<pali.size();j++)
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

    return 0;
}
