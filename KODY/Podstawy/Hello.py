#! /usr/bin/env python
# -*- coding: utf-8 -*-

ROK = 2017
ROKPY = 1991

def parzysta(b):
    ile = list(range(0, b+1, 2))
    return ile

def main(args):
    imie = input("Jak masz na imię? ")
    wiek = int(input("Ile masz lat? "))
    rokur = ROK - wiek
    print ("Czołem! ", imie)
    print ("No to jesteś z: ", ROK-wiek) 
    if ROKPY < rokur:
        print("Jestem starszy~PY")
    elif ROKPY > rokur:
        print ("Jestem młodszy~PY")
    elif ROKPY == rokur:
        print ("Rówieśnik~PY")
    
    b = int(input("podaj liczbę naturalną: "))
    print('Ilość parzystych:', parzysta(b))
    
    return 0
    
if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
