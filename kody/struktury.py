#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  struktury.py
#


def osoba(imie, nazwisko, wiek):
    return{'imie': imie, 'nazwisko': nazwisko, 'wiek': wiek}


def pobierzDane(lista, n):
    for i in range(0, n):
        imie = input('podaj imię:')
        nazwisko = input('podaj nazwisko:')
        wiek = int(input('podaj wiek:'))
        lista.append(osoba(imie, nazwisko, wiek))
    return lista

def wyswietlDane(lista):
    for i in lista:
        print("Imię: {:20}".format(o['imie']))
        print("Nazwisko: {:20}".format(o['nazwisko']))
        print("Wiek: {:20}".format(o['wiek']))
    print()


def zapiszDane(lista):
    with open('osobyp.txt', 'w') as plik:
        for o in lista:
            plik.write(o['imie'] + "," + o['nazwisko'] + "," + str(o['wiek']) + "\n")

def zapiszDaneCsv(lista):
    import csv
    with open('osobyp.csv', 'w', newline='') as plik:
        tresc = csv.writer(plik, delimiter=';')
        for o in lista:
            tresc.writerow(o.values())

def czytajDane(nazwa):
    import csv
    with open(nazwa, newline='') as plik:
        tresc = csv.reader(plik, delimiter=';')
        for i in tresc:
            print(o)



def main(args):
    ##print(osoba1['imie'], osoba1['nazwisko'])
    ile = int(input('Ile osób wprowadzisz?'))
    lista = [] #pusta lista
    lista = pobierzDane(lista, ile)
    wyswietlDane(lista)
    zapiszDaneCsv(lista)
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
