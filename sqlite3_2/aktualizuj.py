#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  baza_sql.py

import sqlite3

def wyniki(dane):
    for rekord in dane:
        print(tuple(rekord))

def kw_a(cur):
    parametr = input('Podaj klase→ ')
    print('Podpunkt a)')
    cur.execute("""
       SELECT Imie, Nazwisko, Klasa
       FROM tbUczniowie, tbKlasy
       WHERE KlasaID = IDKlasy
       AND Klasa = ?
    """, (parametr,)) 
    
    wyniki(cur.fetchall())

def kw_b(cur):
    print('Podpunkt b)')
    cur.execute("""
       SELECT Imie, Nazwisko, MAX(EgzHum)
       FROM tbUczniowie
    """) 
    
    wyniki(cur.fetchall())    

def kw_c(cur):
    print('Podpunkt c)')
    cur.execute("""
       SELECT Klasa, AVG(EgzMat)
       FROM tbUczniowie, tbKlasy
       WHERE tbUczniowie.KlasaID = tbKlasy.IDKlasy
       AND Klasa = '1A'
    """)  
    
    wyniki(cur.fetchall())  
    
def kw_d(cur):
    print('Podpunkt d)')
    cur.execute("""
       SELECT Ocena
       FROM tbUczniowie, tbOceny
       WHERE tbUczniowie.IDUcznia = tbOceny.UczenID
       AND Imie = 'Dorota'
       AND Nazwisko = 'Nowak'
    """)  
    
    wyniki(cur.fetchall())      
    
def kw_e(cur):
    print('Podpunkt e)')
    cur.execute("""
       SELECT AVG(Ocena)
       FROM tbOceny, tbPrzedmioty
       WHERE tbOceny.PrzedmiotID = tbPrzedmioty.IDPrzedmiotu
       AND tbPrzedmioty.Przedmiot = 'fizyka'
       AND Datad > '2012-10-01'
       AND Datad < '2012-10-31'
    """)  
    
    wyniki(cur.fetchall())

def dodaj(cur):
    cur.execute("""
        INSERT INTO tbKlasy
        VALUES (?, ?, ?, ?)
    """, [None, '1B', 2017, 2020])

def aktualizuj(cur):
    cur.execute("""
        UPDATE tbKlasy
        SET klasa = ?
        WHERE klasa = ? and roknaboru = ?
    """, ['1D', '1B', 2017])

def main(args):
    con = sqlite3.connect('szkola.db')
    cur = con.cursor()  # utworzenie kursora
    con.row_factory = sqlite3.Row
    
    con.commit()
    #dodaj(cur)
    aktualizuj(cur)
    wyniki(cur.execute('SELECT * FROM tbKlasy'))
    
    
    #kw_a(cur)
    #kw_b(cur)
    #kw_c(cur)
    #kw_d(cur)
    #kw_e(cur)
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
