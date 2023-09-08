#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Anatoly Belyakov  <aabelyakov@mail.ru>
# Created: 05.03.2019
# Purpose: 
#############################################################################
from pydal import DAL, Field
#############################################################################
db = DAL('sqlite://test.db')#, folder='dbs')

try:
    db.define_table(
        'cars', 
        Field('name'), 
        Field('price', type='integer')
    )
    db.cars.insert(name='Audi', price=52642)
    db.cars.insert(name='Skoda', price=9000)
    db.cars.insert(name='Volvo', price=29000)
    db.cars.insert(name='Bentley', price=350000)
    db.cars.insert(name='Citroen', price=21000)
    db.cars.insert(name='Hummer', price=41400)
    db.cars.insert(name='Volkswagen', price=21600)
finally:
    if db:
        db.close()
    #endif
#endtry
#############################################################################
