import conexion as con

class ProveedoresData():       
    def lista_proveedores(self):
        self.db = con.Conexion().conectarBd()
        self.cursor= self.db.cursor()
        query= self.cursor.execute("SELECT * FROM proveedores order by nombre_razon")
        serch_info=query.fetchall()
        self.db.close()    
        return(serch_info)
    

     