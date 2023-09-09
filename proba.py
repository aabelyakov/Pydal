#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Anatoly Belyakov  <aabelyakov@mail.ru>
# Created: 13.03.2019
'''
Purpose: Просмотр таблицы в виде формы:
Имя поля1: Значение поля1
Имя поля2: Значение поля2
Имя поля3: Значение поля3
Имя поля4: Значение поля4
Имя поля5: Значение поля5
'''
#############################################################################
# from pydal import DAL, Field
from model import db

#############################################################################
# Oбъект соединения c БД
print("db:", db)
# db: {
#     'obj': <Table obj (id, snaim, naim, address, ready)>, '_debug': False,
#     '_uri': 'sqlite://red.sqlite', '_decode_credentials': False,
#     '_uri_hash': '4252f9bce694ea69042ee20eb7202c16', '_adapter_args': None,
#     '_migrate': True,
#     '_adapter': <pydal.adapters.sqlite.SQLite object at 0x7f7edfeb9320>,
#     '_driver_args': None, '_db_codec': 'UTF-8',
#     '_drivers_available': {'psycopg2': <module 'psycopg2' from
#     '/usr/lib/python3/dist-packages/psycopg2/__init__.py'>,
#     'sqlite3': <module 'sqlite3.dbapi2' from
#     '/usr/lib/python3.5/sqlite3/dbapi2.py'>,
#     'imaplib': <module 'imaplib' from '/usr/lib/python3.5/imaplib.py'>},
#     '_request_tenant': 'request_tenant', '_tables': ['obj'],
#     '_pending_references': {}, '_do_connect': True, '_bigint_id': False,
#     '_ignore_field_case': True, '_fake_migrate': False, '_LAZY_TABLES': {},
#     '_fake_migrate_all': False, 'check_reserved': None,
#     '_referee_name': '%(table)s', '_attempts': 5, '_common_fields': [],
#     '_migrate_enabled': True, '_dbname': 'sqlite',
#     '_db_uid': '816c92dd7cd47d7664de79c55541bf80',
#     '_lazy_tables': False, '_migrated': [],
#     '_check_reserved': None, '_pool_size': 0,
#     '_folder': './databases/SQLite'
# }
# ------------------------------------------------------------------------------
# Объект универсального идентификатора ресурса (Uniform Resource Identifier)
print("db._uri:", db._uri)
# db._uri: sqlite://red.sqlite
# ------------------------------------------------------------------------------
# Предыдущий SQL-запрос
print("db._lastsql:", db._lastsql)
# db._lastsql: None

# ------------------------------------------------------------------------------
# Тип СУБД
print("db._dbname:", db._dbname)
# db._dbname: sqlite
# ------------------------------------------------------------------------------
# Перечень таблиц в базе данных
print("db.tables:", db.tables)
# db.tables: ['obj', 'bus', 'krp', 'pdr', 'lgh', 'sht']
# ------------------------------------------------------------------------------
# Перечень полей в таблице obj
print("db.obj.fields:", db.obj.fields)
# db.obj.fields: ['id', 'snaim', 'naim', 'address', 'ready']
#############################################################################
