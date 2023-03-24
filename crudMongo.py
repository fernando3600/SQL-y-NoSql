from connMongo import getDbMongo

class _crudMongo:
    def __init__(self, table):

        if(table == "clientes"): 
            self.tabla = getDbMongo().clientes
            self.tableName = "clientes"
        if(table == "ventas"): 
            self.tabla = getDbMongo().ventas
            self.tableName = "ventas"
        if(table == "sucursales"): 
            self.tabla = getDbMongo().sucursales
            self.tableName = "sucursales"
        if(table == "detalles"): 
            self.tabla = getDbMongo().detalles
            self.tableName = "detalles"
        if(table == "productos"): 
            self.tabla = getDbMongo().productos
            self.tableName = "productos"



        

    def getData(self):
        data = []
        dataUsers = self.tabla.find()

        for doc in dataUsers:
            data.append(doc)
        return data


    def saveData(self, data):
        allData = []

        # transformando la informacion 

        if data is not None:
            for doc in data:
                if self.tableName == "clientes":
                    allData.append({
                            "id": doc[0],
                            "nombre": doc[1],
                            "apellidps": doc[2],
                            "rfc": doc[3],
                            "email": doc[4],
                            "telefono": doc[5]
                        })
                if self.tableName == "sucursales":
                    allData.append({
                            "id": doc[0],
                            "nombre": doc[1],
                            "direccion": doc[2],
                            "latitud": doc[3],
                            "longitud": doc[4]
                        })
                if self.tableName == "productos":
                    allData.append({
                            "id": doc[0],
                            "nombre": doc[1],
                            "unidadMedida": doc[2],
                            "precioUnitario": doc[3],
                        })
                if self.tableName == "ventas":
                    allData.append({
                            "id": doc[0],
                            "sucursalId": doc[1],
                            "clientesId": doc[2],
                            "fecha": doc[3],
                        })
                if self.tableName == "detalles":
                    allData.append({
                            "id": doc[0],
                            "ventasId": doc[1],
                            "productosId": doc[2],
                            "cantidad": doc[3],
                        })

        # guardando los datos
        result = self.tabla.insert_many(allData)
        return result.inserted_ids


    


