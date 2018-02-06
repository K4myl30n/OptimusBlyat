/*
 * wskazniki.cpp
 */


#include <iostream>

using namespace std;

int main(int argc, char **argv)
{
    int x = 11;
    cout << x << endl; //wartosc zmiennej
    cout << &x << endl; // adres zmiennej w pamieci
    cout << * &x << endl; // wartosc zmiennej pod adresem
	
    int *px;
    px = &x;
    cout << px << endl;
    cout << *px << endl;                                                                            
	return 0;
}

