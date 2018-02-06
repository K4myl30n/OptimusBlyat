/*
 * wskazniki.cpp
 */


#include <iostream>
#include <iomanip>
#include <cstdlib>


using namespace std;

void drukuj(float *t, int ile) {
        for(int i = 0; i < ile; i++) {
            cout << *(t + i) << endl;
        }
        
}

void wprowadz(float *t, int ile) {
        for(int i=0; i< ile; i++) {
            cout << "podaj liczbę> ";
            //cin >> t[i];
            cout << "Adres elementu> " << (t + i) << endl;
            cin >> *(t + i);
            
        }
}

float tab1W() {
    cout << "Ile podasz liczb? ";
    int ile;
    cin >> ile;
    
    cout << sizeof(ile) << endl;
    
    try {
        
        float *ptab = NULL;
        ptab = new float[ile];
        wprowadz(ptab, ile);
        drukuj(ptab, ile);
    } catch(bad_alloc) {
        cout << "Za mało pamięci";
        return 1;
    }
    
    return 0;
}

void wypelnij2W(int **tab,int w,int k) {
    srand(time(NULL));
    for(int i =1; i < w; i++) {
        for(int j = 1; j < k; j++) {
            tab[i][j] = i*j;
            cout << setw(4) << tab[i][j];
        }
    }
}

float tab2W() {
    int w, k, i;
    cout << "podaj liczbe wierszy i kolumn? ";
    cin >> w >> k;
    int **tab;

    try {
        tab = new int*[w];
    } catch(bad_alloc) {
        cout << "Za mało pamięci";
        return 1;
    }
    for(i =0; i < w; i++) {
        try {
            tab[i] = new int[k];
        } catch(bad_alloc) {
            cout << "Za mało pamięci" ;
            return 1;
        }
    }
    
    wypelnij2W(tab, w, k);
    
    return 0;
}

int main(int argc, char **argv)
{
   //tab1W();         
   tab2W();                                                 
	return 0;
}

