from model import db
from pydal import DAL, Field

print(db.tables)
# ['obj', 'bus', 'krp', 'pdr', 'lgh', 'sht']

# Перечень полей в таблице obj
print(db.obj.fields)
# ['id', 'snaim', 'naim', 'address', 'ready']

# Перечень полей в таблице bus
print(db.bus.fields)
# ['id', 'obj_id', 'snaim', 'naim', 'host', 'port', 'timeout', 'ready']

# Перечень полей в таблице sht
print(db.sht.fields)
# ['id', 'obj_id', 'bus_id', 'krp_id', 'pdr_id', 'lgh_id', 'addr', 'ready']
# ----------------------------------------------------------------------------
# Доступ к записи таблицы bus по заданному идентификатору
# print(db.bus[id])
print(db.bus[3])
# ----------------------------------------------------------------------------
# Чистка всех таблиц в цикле
for tbl in db.tables:
    eval(f"db.{tbl}.truncate()")

# Импорт данных из одного csv-файла all.csv во все таблицы
db.import_from_csv_file(
    open('databases/SQLite/csv/all.csv', 'r'),
    restore=True,
    encoding="utf-8",
)
# ----------------------------------------------------------------------------
for iBus in range(1, len(db(db.bus).select()) + 1):
    # Объединение трёх таблиц obj, bus и sht в дерево
    oRows = db(db.obj.id == db.bus.obj_id)(db.bus.id == db.sht.bus_id) \
        (db.sht.bus_id == iBus).select()
    print(oRows)
    for oRow in oRows:
        # print(oRow["sht"]["bus_id"])
        print(oRow.sht.bus_id)

# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
print(db.bus[3])

db.commit()

# В Н И М А Н И Е!!!!
# Первые два поля в каждой  распечатке из четырех - это идентификаторы шины
# (bus.id) и  объекта (bus.obj_id), то есть - путь к таблице sht от таблицы
# obj и bus.
"""
bus.id,bus.obj_id,bus.snaim,bus.naim,bus.host,bus.port,bus.timeout,bus.ready,sht.id,sht.obj_id,sht.bus_id,sht.krp_id,sht.pdr_id,sht.lgh_id,sht.addr,sht.ready,obj.id,obj.snaim,obj.naim,obj.address,obj.ready
1,1,qwork,Pack1,94.240.112.77,65000,10,True,1,1,1,3,8,1,09,True,1,NZiF,Отдельный счётчик,Корпус 35,True

bus.id,bus.obj_id,bus.snaim,bus.naim,bus.host,bus.port,bus.timeout,bus.ready,sht.id,sht.obj_id,sht.bus_id,sht.krp_id,sht.pdr_id,sht.lgh_id,sht.addr,sht.ready,obj.id,obj.snaim,obj.naim,obj.address,obj.ready
2,1,qrept,Pack2,94.240.112.77,65001,10,False,2,1,2,7,6,2,09,True,1,NZiF,Отдельный счётчик,Корпус 35,True

bus.id,bus.obj_id,bus.snaim,bus.naim,bus.host,bus.port,bus.timeout,bus.ready,sht.id,sht.obj_id,sht.bus_id,sht.krp_id,sht.pdr_id,sht.lgh_id,sht.addr,sht.ready,obj.id,obj.snaim,obj.naim,obj.address,obj.ready
3,2,AllMoxy,NoPackAll,213.177.97.70,4001,10,False,3,2,3,5,10,1,01,True,2,Moxy,Счётчики на стене,Стена у Южука,False
3,2,AllMoxy,NoPackAll,213.177.97.70,4001,10,False,4,2,3,7,18,2,02,True,2,Moxy,Счётчики на стене,Стена у Южука,False
3,2,AllMoxy,NoPackAll,213.177.97.70,4001,10,False,5,2,3,10,7,1,03,True,2,Moxy,Счётчики на стене,Стена у Южука,False
3,2,AllMoxy,NoPackAll,213.177.97.70,4001,10,False,6,2,3,9,9,1,04,True,2,Moxy,Счётчики на стене,Стена у Южука,False
3,2,AllMoxy,NoPackAll,213.177.97.70,4001,10,False,7,2,3,7,25,1,05,True,2,Moxy,Счётчики на стене,Стена у Южука,False
3,2,AllMoxy,NoPackAll,213.177.97.70,4001,10,False,8,2,3,10,24,2,06,True,2,Moxy,Счётчики на стене,Стена у Южука,False
3,2,AllMoxy,NoPackAll,213.177.97.70,4001,10,False,9,2,3,6,18,1,07,True,2,Moxy,Счётчики на стене,Стена у Южука,False
3,2,AllMoxy,NoPackAll,213.177.97.70,4001,10,False,10,2,3,11,12,1,08,True,2,Moxy,Счётчики на стене,Стена у Южука,False
3,2,AllMoxy,NoPackAll,213.177.97.70,4001,10,False,11,2,3,3,27,1,09,True,2,Moxy,Счётчики на стене,Стена у Южука,False
3,2,AllMoxy,NoPackAll,213.177.97.70,4001,10,False,12,2,3,7,26,1,0a,True,2,Moxy,Счётчики на стене,Стена у Южука,False
3,2,AllMoxy,NoPackAll,213.177.97.70,4001,10,False,13,2,3,6,8,1,0b,True,2,Moxy,Счётчики на стене,Стена у Южука,False
3,2,AllMoxy,NoPackAll,213.177.97.70,4001,10,False,14,2,3,11,16,3,0c,True,2,Moxy,Счётчики на стене,Стена у Южука,False
3,2,AllMoxy,NoPackAll,213.177.97.70,4001,10,False,15,2,3,1,22,1,0d,True,2,Moxy,Счётчики на стене,Стена у Южука,False
3,2,AllMoxy,NoPackAll,213.177.97.70,4001,10,False,16,2,3,7,19,1,0e,True,2,Moxy,Счётчики на стене,Стена у Южука,False
3,2,AllMoxy,NoPackAll,213.177.97.70,4001,10,False,17,2,3,3,15,3,0f,True,2,Moxy,Счётчики на стене,Стена у Южука,False
3,2,AllMoxy,NoPackAll,213.177.97.70,4001,10,False,18,2,3,3,16,1,10,True,2,Moxy,Счётчики на стене,Стена у Южука,False

bus.id,bus.obj_id,bus.snaim,bus.naim,bus.host,bus.port,bus.timeout,bus.ready,sht.id,sht.obj_id,sht.bus_id,sht.krp_id,sht.pdr_id,sht.lgh_id,sht.addr,sht.ready,obj.id,obj.snaim,obj.naim,obj.address,obj.ready
4,2,PwrMoxy,NoPackPwr,213.177.97.70,4001,10,False,19,2,4,7,24,1,01,False,2,Moxy,Счётчики на стене,Стена у Южука,False
4,2,PwrMoxy,NoPackPwr,213.177.97.70,4001,10,False,20,2,4,6,24,2,02,True,2,Moxy,Счётчики на стене,Стена у Южука,False
4,2,PwrMoxy,NoPackPwr,213.177.97.70,4001,10,False,21,2,4,8,16,1,03,True,2,Moxy,Счётчики на стене,Стена у Южука,False
4,2,PwrMoxy,NoPackPwr,213.177.97.70,4001,10,False,22,2,4,2,17,1,04,True,2,Moxy,Счётчики на стене,Стена у Южука,False
4,2,PwrMoxy,NoPackPwr,213.177.97.70,4001,10,False,23,2,4,5,1,1,05,True,2,Moxy,Счётчики на стене,Стена у Южука,False
4,2,PwrMoxy,NoPackPwr,213.177.97.70,4001,10,False,24,2,4,5,19,1,06,True,2,Moxy,Счётчики на стене,Стена у Южука,False
4,2,PwrMoxy,NoPackPwr,213.177.97.70,4001,10,False,25,2,4,10,8,2,07,True,2,Moxy,Счётчики на стене,Стена у Южука,False
4,2,PwrMoxy,NoPackPwr,213.177.97.70,4001,10,False,27,2,4,4,15,1,09,False,2,Moxy,Счётчики на стене,Стена у Южука,False
4,2,PwrMoxy,NoPackPwr,213.177.97.70,4001,10,False,28,2,4,2,19,1,0b,False,2,Moxy,Счётчики на стене,Стена у Южука,False
4,2,PwrMoxy,NoPackPwr,213.177.97.70,4001,10,False,29,2,4,8,8,1,0f,True,2,Moxy,Счётчики на стене,Стена у Южука,False
4,2,PwrMoxy,NoPackPwr,213.177.97.70,4001,10,False,30,2,4,11,13,3,10,True,2,Moxy,Счётчики на стене,Стена у Южука,False
"""