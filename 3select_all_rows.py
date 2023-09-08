#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Anatoly Belyakov  <aabelyakov@mail.ru>
# Created: 06.03.2019
# Purpose: 
#############################################################################
from pydal import DAL, Field
#############################################################################
try:
    db = DAL('sqlite://test.db')#, folder='dbs')
    #------------------------------------------------------------------------
    db.define_table(
        'cars', 
        Field('name'), 
        Field('price')
    )
    #------------------------------------------------------------------------
    '''
    db.cars.insert(name='Audi', price=52642)
    db.cars.insert(name='Skoda', price=9000)
    db.cars.insert(name='Volvo', price=29000)
    db.cars.insert(name='Bentley', price=350000)
    db.cars.insert(name='Citroen', price=21000)
    db.cars.insert(name='Hummer', price=41400)
    db.cars.insert(name='Volkswagen', price=21600)
    '''
    #------------------------------------------------------------------------
    rows = db().select(db.cars.ALL)
    print(rows)
    #------------------------------------------------------------------------
    for row in rows:
        print("{} {} {}".format(row['id'], row['name'], row['price']))
    #endfor
    #------------------------------------------------------------------------
finally:
    if db:
        db.close()    
    #endif
#endtry
#############################################################################
"""
1 Audi 52642
2 Skoda 9000
3 Volvo 29000
4 Bentley 350000
5 Citroen 21000
6 Hummer 41400
7 Volkswagen 21600
8 Audi 52642
9 Skoda 9000
10 Volvo 29000
11 Bentley 350000
12 Citroen 21000
13 Hummer 41400
14 Volkswagen 21600
15 Audi 52642
16 Skoda 9000
17 Volvo 29000
18 Bentley 350000
19 Citroen 21000
20 Hummer 41400
21 Volkswagen 21600
"""
