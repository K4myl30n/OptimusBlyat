/*
 * lista.cpp 
 */


#include <iostream>
#include "lista.hpp"

Lista::Lista(){
    head = NULL; // lista jest pusta
    tail = NULL;
}

Lista::~Lista(){
    while(Usun()) {;}; // usuniecie 3wszystkich elementow listy
}

void Lista::Dodaj(int wartosc){
    ELEMENT *elo = new ELEMENT;
    elo->wartosc = wartosc;
    elo->next = NULL;
    if (head == NULL) { // lista była pusta
        head = elo;
        tail = elo;
    } else {
        tail->next = elo; //ustawienie wskaznika nastepny dotychczasowego
        tail = elo; // update wskaznika do ostatniego elementu
    }
}

void Lista::Wyswietl(){
    ELEMENT *elo = head;
    while(elo != NULL) {
        std::cout << elo->wartosc << " ";
        elo = elo->next;
    }
}

bool Lista::Usun(){
    if (head != NULL){
        if(head == tail) {
            delete head;
            head = NULL;
            tail = NULL;
        } else {
            ELEMENT *elo = head;
            while(elo->next != tail){
            elo = elo->next;
            }
            delete elo->next;
            elo->next = NULL;
            tail = elo;   
        }
        return true;
    }
    return false;
}

void Lista::Wstaw(int pozycja, int wartosc) {
    ;
}
