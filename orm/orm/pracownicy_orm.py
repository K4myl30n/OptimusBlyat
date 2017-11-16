#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  pracownicy_orm.py

from peewee import *
from dane import *

baza_plik = SqliteDatabase('baza.db')


class BaseModel(Model):
    class Meta:
        database = baza_plik


class Premia(BaseModel):
    id = CharField(primary_key = True)
    premia = DecimalField()
    
    def __str__(self):
        return self.id
    

class Dzial(BaseModel):
    id = IntegerField(primary_key = True)
    nazwa = CharField()
    siedziba = CharField()


class Pracownik(BaseModel):
    id = CharField(primary_key = True)
    nazwisko = CharField()
    imie = CharField()
    stanowisko = ForeignKeyField(Premia)
    data_zatr = DateField()
    placa = DecimalField(decimal_places=2)
    id_dzial = ForeignKeyField(Dzial)
    premia = DecimalField(decimal_places=2, default=0)
    
baza_plik.connect()  # połączenie z bazą
baza_plik.create_tables([Premia, Dzial, Pracownik], True)

def kw_c():
    #query = Pracownik.select()
    #select imie, nazwisko from pracownik;
    query = (Dzial
            .select(Dzial.siedziba, fn.Sum(Pracownik.placa).alias('place'))
            .join(Pracownik)
            .group_by(Dzial.siedziba)
            .order_by('place').asc())
            
    for obj in query:
        print(obj.siedziba, obj.place)

kw_d():
    query = Pracownik.select().join(Dzial)
    
    for obj in query:
        print(obj.id, )

#obiekt = Premia('Kierowca', premia=0.2)
#obiekt.save()

#~dane = [
    #~{'id': 'Kierowca', 'premia': '0.2'},
    #~{'id': 'Dyrektor', 'premia': '0.7'},
    #~{'id': 'Inżynier', 'premia': '0.4'},
#~]
#~for rekord in dane:
    #~Premia.create(id=dane['id'], premia=rekord['premia'])

#Premia.create(id='Kierowca', premia=0.2)
#Dzial.create(id=10, nazwa="Informatyka", siedziba="Warszawa")

premia = dane_z_pliku('premia.txt')
premia = wyczysc_dane(premia, 1)

#~print(premia)
#~print(Premia._meta.sorted_field_names)

premia = [dict(zip(Premia._meta.sorted_field_names, rekord))
for rekord in premia]

pracownicy = dane_z_pliku('pracownicy.txt')
pracownicy = wyczysc_dane(pracownicy, 5)
pracownicy = [dict(zip(Pracownik._meta.sorted_field_names, rekord))
for rekord in pracownicy]

dzial = dane_z_pliku('dział.txt')
dzial = [dict(zip(Dzial._meta.sorted_field_names, rekord))
for rekord in dzial]

print(premia)
print(pracownicy)
print(dzial)

with baza_plik.atomic():
    Premia.insert_many(premia).execute()
    Pracownik.insert_many(pracownicy).execute()
    Dzial.insert_many(dzial).execute()

baza_plik.commit()

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

def main(args):
    
    kw_c()
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
