#ifndef LISTA_HPP
#define LISTA_HPP

struct ELEMENT {
    int wartosc;
    ELEMENT * next;

};

class Lista {
    private:
        ELEMENT *head;
        ELEMENT *tail;
    public:
    Lista();
    ~Lista();
    void Dodaj(int);
    void Wyswietl();
    bool Usun();
};

#endif
