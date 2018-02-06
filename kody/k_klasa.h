#ifndef KLASA_H
#define KLASA_H


class Klasa {
private:
    char imie;
    char nazwisko;
public:
    int klasa;
    int * oceny = new int [20];
    float srednia;
    int ustaw_klase();
};
