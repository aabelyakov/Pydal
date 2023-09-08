# from pydal import DAL, Field
from model import db

# Чистка таблицы sht
# db.sht.truncate()

# Вставка нового значения поля addr в текущей записи таблицы sht
# print(db.sht.insert(addr="A1"))

# Заполним поле addr в нескольких строках таблицы sht
# print(db.sht.bulk_insert([{'addr': 'S1'}, {'addr': 'S2'}, {'addr': 'S3'}]))

oRows = db(db.sht).select()
for oRow in oRows:
    print(oRow.id, oRow.addr, oRow.ready)

# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
print(oRows[1])
print(oRows[1].ready) # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

oRow = db(db.bus).select()[2]
print(oRow.port)
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

# Как удалить одну запись из БД
db(db.bus.id==4).delete()

db.commit()
