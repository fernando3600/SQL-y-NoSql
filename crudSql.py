from connSqLite import openSqlLite

class _crudSql:

    def __init__(self, table):
        if(table == "clientes"): self.tabla = table
        if(table == "ventas"): self.tabla = table
        if(table == "sucursales"): self.tabla = table
        if(table == "detalles"): self.tabla = table
        if(table == "productos"): self.tabla = table

    def getData(self):
        cursor = openSqlLite()

        res = cursor.execute(f"SELECT * from {self.tabla}")

        res = res.fetchall()

        return res