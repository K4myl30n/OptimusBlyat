#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  pracownicy_orm.py

from peewee import *

baza = SqliteDatabase(':memory:')


class BaseModel(Model):
    class Meta:
        baza = baza_plik
        

class Premia(BaseModel):
    id = CharField(primary_key = True)
    premia = DecimalKey()
    
class Dzial(BaseModel): 
    id = CharField(primary_key = True)
    nazwa = CharField()
    siedziba = CharField()
    

class Pracownik(BaseModel):
    id = CharField(primary_key = True)
    nazwisko = CharField()
    imie = CharField()
    stanowisko = ForeignKeyField(Premia)
    data_zatr = DataField()
    placa = DecimalField()
    premia = DecimalField()
    id_dzial = ForeignKeyField(dzial)


baza_plik.connect()
baza_plik.create_tables([Premia, Dzial, Pracownik], True)


def main(args):
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
