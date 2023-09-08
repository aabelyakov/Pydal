#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Anatoly Belyakov  <aabelyakov@mail.ru>
# Created: 06.03.2019
# Purpose: 
#############################################################################
from pydal import DAL, Field
#############################################################################
try:
    db = DAL('sqlite://test.db') #, folder='dbs')
    #------------------------------------------------------------------------
    db.define_table(
        'cars', 
        Field('name'), 
        Field('price', 'integer')
    )
    #------------------------------------------------------------------------
    """
    db.cars.insert(name='Audi', price=52642)
    db.cars.insert(name='Skoda', price=9000)
    db.cars.insert(name='Volvo', price=29000)
    db.cars.insert(name='Bentley', price=350000)
    db.cars.insert(name='Citroen', price=21000)
    db.cars.insert(name='Hummer', price=41400)
    db.cars.insert(name='Volkswagen', price=21600)
    """
    #------------------------------------------------------------------------
    rows = db(db.cars).select()
    print(rows.as_json())
    #------------------------------------------------------------------------
finally:
    if db:
        #cars.drop()
        db.close()        
    #endif
#endtry
#############################################################################
"""
[{"id": 1, "name": "Audi", "price": 52642}, 
{"id": 2, "name": "Skoda", "price": 9000}, 
{"id": 3, "name": "Volvo", "price": 29000}, 
{"id": 4, "name": "Bentley", "price": 350000}, 
{"id": 5, "name": "Citroen", "price": 21000}, 
{"id": 6, "name": "Hummer", "price": 41400}, 
{"id": 7, "name": "Volkswagen", "price": 21600}]
"""