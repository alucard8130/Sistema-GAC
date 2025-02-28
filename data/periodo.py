
import conexion as con

#
class PeriodosCargaData():
    #
    def info_periodos_x_tipo_cartera(self,tipoCartera):
        self.db = con.Conexion().conectarBd()
        self.cursor= self.db.cursor()
        query= self.cursor.execute("SELECT periodo FROM reg_carga_cuotas WHERE tipo_cartera='{}'".format(tipoCartera))
        serch_info=query.fetchall()
        self.db.close()    
        return(serch_info)
        

                