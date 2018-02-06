/*
 * struktury.cxx
 * 
 */


#include <iostream>
#include <iomanip>
#include <fstream>

using namespace std;

struct osoba {
    char imie[20];
    char nazwisko[20];
    int wiek;
};

void pobierzDane(osoba t[], int n) {
    for(int i = 0; i <n; i++){
    cin.ignore(1);
    cout << "Podaj imię : " ;
    cin.getline(t[i].imie, 20);
    cout << "Podaj nazwisko : ";
    cin.getline(t[i].nazwisko, 20);
    cout << "Podaj wiek : ";
    cin >> t[i].wiek;
    }
}

void wyswietlDane(osoba t[], int n) {
    for(int i = 0; i < n; i++){
    cout << setw(10) << left << "Imię:" << setw(20)  << setfill('_') << right << t[i].imie << endl;
    cout << setw(10) << left << "Nazwisko:" << setw(20)  << setfill('_') << right << t[i].nazwisko << endl;
    cout << setw(10) << left << "Wiek:" << setw(20) << setfill('_') << right << t[i].wiek << endl;
    
    }
}

void zapiszOsoby(osoba t[], int n) {
    ofstream plik("osoby.txt", ios::app);
        if (!plik.is_open()) {
            cout << "Błąd otwarcia pliku";
        } else {
            for(int i = 0; i < n; i++) {
                cout << t[i].imie << "," << t[i].nazwisko << "," << t[i].wiek << endl;
                plik << t[i].imie << "," << t[i].nazwisko << "," << t[i].wiek << endl;
        }
    }
}
osoba pobierzInf(osoba u) {
    cout << "Podaj imię : " ;
    cin.getline(u.imie, 20);
    cout << "Podaj nazwisko : ";
    cin.getline(u.nazwisko, 20);
    cout << "Podaj wiek : ";
    cin >> u.wiek;
    return u;
}

void wyswietlInf(osoba u) {
    cout << setw(10) << left << "Imię:" << setw(20)  << setfill('_') << right << u.imie << endl;
    cout << setw(10) << left << "Nazwisko:" << setw(20)  << setfill('_') << right << u.nazwisko << endl;
    cout << setw(10) << left << "Wiek:" << setw(20) << setfill('_') << right << u.wiek << endl;
}

void czytajDane(osoba t[]) {
    ifstream plik("osoby.txt");
    string linia;
    
    if (plik.is_open()) { //udane otwarcie pliku
        int i = 0;
        while(getline(plik, linia)) {
            cout << linia << endl;
        }
    } else {
        cout << "Błąd otwarcia pliku";
    }
}

int main(int argc, char **argv)
{
	int ile;
    cout << "Ile osób chcesz wprowadzić: "; cin >> ile;
    //osoba uczen;
    osoba uczniowie[ile];
    //uczen = pobierzInf(uczen);
    pobierzDane(uczniowie, ile);
    //wyswietlInf(uczen);
    wyswietlDane(uczniowie, ile);
    zapiszDane(uczniowie, ile)
    
    osoba dane[ile];
    czytajDane(dane);
    
	return 0;
}

