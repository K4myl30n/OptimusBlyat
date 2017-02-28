/*
 * szyfr_cezara.cpp
 */


#include <iostream>

using namespace std;

void szyfruj(char tekst[], int klucz){
    int i = 0;
    klucz = klucz % 26;
    while (tekst[i] != '\0') {
        if((int)tekst[i] + klucz > 122)
        //(int)tekst[i]
        //(char)((int)tekst[i])
            tekst[i] = (char)((int)tekst[i] + klucz - 26);
        else
            tekst[i] = (char)((int)tekst[i] + klucz);
        i++;
    }
    cout << tekst;
}

int main(int argc, char **argv)
{   char tekst[100];
    int klucz = 3;
    cout << "Podaj tekst do zaszyfrowania ";
    //cin >> tekst;
    cin.getline(tekst, 100);
    cout << "Podaj klucz: ";
    cin >> klucz;
    szyfruj(tekst, klucz);

	return 0;
}

