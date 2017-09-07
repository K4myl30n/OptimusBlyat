#include <iostream>

using namespace std;

#define ROK 2017
int parzysta(int b){
    int i;
    for (i=0; i<=b; i+=2)
        cout << i << " ";
    return i / 2;
    }


int main(int argc, char **argv) {   
    
    //~const int rok = 2017;
    //string imie;
    const int rokcpp = 1983;
    char imie[20]; 
    int a = 0;
    
    cout << "Podaj imie: ";
    cin >> imie;
    cout << "Witaj " << imie << endl;
    cout << "Ile masz lat? ";
    cin >> a ;
    cout << "Urodziłeś się w: " << ROK - a << endl;
    
    if ((ROK-a)>rokcpp)
        cout <<"Jestem starszy~C++"<< endl;
	else if ((ROK-a)<rokcpp)
        cout << "Jestem młodszy~C++" << endl;
    else
        cout <<"Jesteśmy w tym samym wieku" ;
    
    cout << endl;
    
    
    int b;
    cout << "Podaj liczbę: ";
    cin >> b;
    cout << "Ilość parzystych"<< parzysta(b);
    return 0;
}










