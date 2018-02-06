/*
 * ul_main.cpp 
 */


#include <iostream>
#include "ul_ulamek.h"

using namespace std;

int main(int argc, char **argv)
{   
    Ulamek ul1(4,5);
    Ulamek ul2(1,7);
    cout << "1 ułamek: ";
    ul1.wypisz();
    cout << " 1 ułamek: ";
    ul2.wypisz();
    cout << ul1.get_l() << endl;
	
	return 0;
}

