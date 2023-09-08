#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Anatoly Belyakov  <aabelyakov@mail.ru>
# Created: 06.03.2019
# Purpose: 
#############################################################################
from pydal import DAL, Field
#############################################################################
try:
    db = DAL('sqlite://test.db')   #, folder='dbs')
    #------------------------------------------------------------------------
    db.define_table('cars', Field('name'), Field('price', 'integer'))
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
    rows = db(db.cars).select(limitby=(2, 5))
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
3 Volvo 29000
4 Bentley 350000
5 Citroen 21000
"""
    
    
        