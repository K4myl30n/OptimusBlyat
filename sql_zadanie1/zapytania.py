#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  baza_sql.py

import sqlite3

def wyniki(dane):
    for rekord in dane:
        print(tuple(rekord))

def kw_c(cur):
    cur.execute("""
        SELECT siedziba, SUM(placa) AS pensje
        FROM dzial, pracownicy
        WHERE dzial.id = pracownicy.id_dzial
        GROUP BY siedziba
        ORDER BY pensje ASC        
    """) #ASC - Sortowanie rosnące 
    
    wyniki(cur.fetchall())
    
def kw_d(cur):
    parametr = input('Podaj nazwe działu→ ')
    parametr2 = input('Kobiety czy mężczyźni→ ')
    
    cur.execute("""
        SELECT dzial.id, dzial.nazwa, nazwisko, imie 
        FROM dzial, pracownicy
        WHERE dzial.id = pracownicy.id_dzial
        AND dzial.nazwa = ?
        AND imie NOT LIKE '%a'
        
    """, (parametr,))
    
    wyniki(cur.fetchall())
        
def kw_e(cur):
    cur.execute("""
        SELECT nazwisko, stanowisko, placa * premia.premia AS pensja
        FROM premia, pracownicy
        WHERE premia.id = pracownicy.stanowisko
        ORDER BY pensja ASC
    """) 
    
    wyniki(cur.fetchall())       

def kw_f(cur):
    cur.execute("""
      SELECT AVG(placa)
      FROM pracownicy
      WHERE imie LIKE '%a'
    """) #NOT LIKE dla mężczyzn
    # zamiast WHERE działa GROUP BY w tym przypadku
    
    wyniki(cur.fetchall())  
    
def kw_g(cur):
    cur.execute("""
      SELECT  imie, nazwisko,
      CAST((JulianDay() - JulianDay(data_zatr)) / 365 AS Integer) AS okres 
      FROM pracownicy
      ORDER BY okres DESC
      LIMIT 100, 5
    """) #DESC segreguje malejąco
    #LIMIT X ogranicza nam TOP X
    wyniki(cur.fetchall())

def kw_h(cur):
    parametr = input('Podaj numer działu→ ')
    cur.execute("""
      SELECT  imie, nazwisko, stanowisko, dzial.id
      FROM dzial, pracownicy
      WHERE dzial.id = pracownicy.id_dzial
      AND dzial.id = ?
    """, (parametr,)) 
    wyniki(cur.fetchall())
    
def main(args):
    con = sqlite3.connect('pracownicy.sqlite3')
    cur = con.cursor()  # utworzenie kursora
    #kw_c(cur)
    #kw_d(cur)
    #kw_e(cur)
    #kw_f(cur)
    #kw_g(cur)
    kw_h(cur)
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
