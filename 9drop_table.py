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
    cars = db.define_table(
        'cars', 
        Field('name'), 
        Field('price', 'integer')
    )
    cars.drop()
finally:
    if db:
        db.close() 
    #endif
#endtry
#############################################################################
