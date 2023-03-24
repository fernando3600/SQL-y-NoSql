from crudMongo import _crudMongo
from crudSql import _crudSql

#definimos la tabla a trabajar 

tabla = "detalles"

# inicializamos las clases para saber con que tabla vamos a trabajar

crudM = _crudMongo(tabla)
crudS = _crudSql(tabla)

# obtenemos los datos de SqLite

dataSQL = crudS.getData()

# los guardamos en mongo DB

dataSaved = crudM.saveData(dataSQL)

# obtenemos todos los datos de mongo db

dataMongo = crudM.getData()

print(dataMongo)

print("se guardo correctamente !")