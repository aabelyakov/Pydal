#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Anatoly Belyakov  <aabelyakov@mail.ru>
# Created: 13.03.2019
# Purpose: 
#############################################################################
from pydal import DAL, Field
# import os

# Каталог для файлов (*.table) с метаданными
# Этот каталог должен существовать до момента создания БД
PATH = "./databases/SQLite"

# Строка соединения с БД
URI = "sqlite://upoweron.sqlite"

# Объект соединения с БД
db = DAL(
    # Строка соединения с БД
    URI,
    #------------------------------------------------------------------------
    # Этот каталог должен существовать до момента создания БД
    folder = PATH
)
#############################################################################
#
#               С П Р А В О Ч Н Ы Е   Т А Б Л И Ц Ы
#
#############################################################################
# Главная справочная таблица - ОБЪЕКТЫ
db.define_table( 
    "obj",  
    Field("snaim", "string", length=15, default="", unique=True),
    Field("naim", "string", length=512, default="", notnull=True),
    Field("address", "string", length=200, default=""),
    Field("ready", "boolean", default=False, notnull=True),
    format = "%(snaim)s",
    migrate='obj.table',
)
#----------------------------------------------------------------------------
# Метки полей таблицы для отображения в формах
db.obj.snaim.label = "СокрНаимОб"
db.obj.naim.label = "НаимОб"
db.obj.address.label = "АдрОб"
db.obj.ready.label = "Опросить"
#============================================================================
# Подчинённая справочная таблица - ШИНЫ 
db.define_table( 
    "bus",
    Field("obj_id", "reference obj"), 
    Field("snaim", "string", length=30, default="", unique=True),
    Field("naim", "string", length=256, default="", notnull=True),
    Field("host", "string", length=15, default="", notnull=True),
    Field("port", "string", length=7, default="", notnull=True),
    Field("timeout", "integer"),
    Field("ready", "boolean", default=False, notnull=True),
    format = "%(snaim)s",
    migrate='bus.table',
)    
#----------------------------------------------------------------------------
# Метки полей таблицы для отображения в формах
db.bus.obj_id.label = "Объект"
db.bus.snaim.label = "СокрНаимШины"
db.bus.naim.label = "НаимШины"
db.bus.host.label = "IpАдрTCPсервера"
db.bus.port.label = "ПортTCPсервера"
db.bus.timeout.label = "Тайм-аут"
db.bus.ready.label = "Опросить"
#============================================================================
# Подчинённая справочная таблица - КОРПУСА
db.define_table( 
    "krp",  
    Field("obj_id", "reference obj"),
    Field("snaim", "string", length=10, default="", unique=True),
    Field("naim", "string", length=256, default="", notnull=True),
    Field("lim", "decimal(10,2)", notnull=True),
    format = "%(snaim)s",
    migrate='krp.table',
)
#----------------------------------------------------------------------------
# Метки полей таблицы для отображения в формах
db.krp.obj_id.label = "Объект"
db.krp.snaim.label = "СокрНаимКорп"
db.krp.naim.label = "НаимКорпуса"
db.krp.lim.label = "Лимит"
#============================================================================
# Подчинённая справочная таблица - ПОДРАЗДЕЛЕНИЯ
db.define_table( 
    "pdr", 
    Field("obj_id", "reference obj"), 
    Field("snaim", "string", length=100, default="", unique=True),
    Field("naim", "string", length=256, default="", notnull=True),
    Field("lim", "decimal(10,2)", notnull=True),
    format = "%(snaim)s",
    migrate='pdr.table',
)
#----------------------------------------------------------------------------
# Метки полей таблицы для отображения в формах
db.pdr.obj_id.label = "Объект"
db.pdr.snaim.label = "СокрНаимПодразд"
db.pdr.naim.label = "НаимПодразд"
db.pdr.lim.label = "Лимит"
#============================================================================
# Cправочная таблица - НАЗНАЧЕНИЕ ЭНЕРГИИ
db.define_table(
    "lgh",
    Field("obj_id", "reference obj"), 
    Field("snaim", "string", length=30, default="", unique=True),
    Field("naim", "string", length=256, default="", notnull=True),
    Field("lim", "decimal(10,2)"), #, notnull=True),
    format = "%(snaim)s",
    migrate='lgh.table',
)
#----------------------------------------------------------------------------
# Метки полей таблицы для отображения в формах
db.lgh.obj_id.label = "Объект"
db.lgh.snaim.label = "СокрНаимНазнЭн"
db.lgh.naim.label = "НаимНазнЭнер"
db.lgh.lim.label = "Лимит"
#============================================================================
# Подчинённая справочная таблица - СЧЁТЧИКИ
db.define_table( 
    "sht",  
    Field("obj_id", "reference obj"), 
    Field("bus_id", 'reference bus'), 
    Field("krp_id", 'reference krp'), 
    Field("pdr_id", 'reference pdr'), 
    Field("lgh_id", 'reference lgh'), 
    Field("addr", "string", length=2, notnull=True),
    Field("ready", "boolean", default=False, notnull=True),
    format = "%(addr)s",
    migrate='sht.table',
)
#----------------------------------------------------------------------------
# Метки полей таблицы для отображения в формах
db.sht.obj_id.label = "Объект"
db.sht.bus_id.label = "Шина"
db.sht.krp_id.label = "Корпус"
db.sht.pdr_id.label = "Подразд"
db.sht.lgh_id.label = "Назнач"
db.sht.addr.label = "АдрСч"
db.sht.ready.label = "Опросить"
#############################################################################
