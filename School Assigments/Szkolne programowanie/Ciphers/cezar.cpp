#include <iostream>
using namespace std;

string ToLower(string keyword){
	string kw;
	for(int i = 0; i<keyword.length(); i++){
		if(int(keyword[i])>=65 || int(keyword[i])<=90){
			kw += tolower(keyword[i]);
		}
	}
	return kw;
}

string Encode(string keyword, int key){
	string encoded;
	for(int i = 0; i< keyword.length();i++){
    if(int(keyword[i]) == 32) encoded+=" "; 
		else {
      encoded +=(char(int(keyword[i])+key));
      if(int(encoded[i]) > 122) encoded[i] = char(int(encoded[i]-26));
      }
	}
	return encoded;
}
string Decode(string keyword, int key){
	string decoded;
	for(int i = 0; i< keyword.length();i++){
    if(int(keyword[i]) == 32) decoded+=" "; 
		else {
      decoded +=(char(int(keyword[i])-key));
      if(int(decoded[i]) < 97) decoded[i] = char(int(decoded[i]+26));
    }
	}
	return decoded;
}
string keyword;
int key;
string type;
int main()
{
    cout << "Input text to encode/decode: ";
    getline(cin, keyword);
    cout<<"Input key: ";
    cin>>key;
    cout<<"To decode type 1\nTo encode type 2\n";
    cin>>type;
    if(type == "1")
      cout<<Decode(ToLower(keyword), key);
    else if(type=="2")
      cout<<Encode(ToLower(keyword), key);
    else 
      cout<<"Wrong Number!";
    return 0;
}