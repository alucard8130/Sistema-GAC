import conexion as con
from model.regcontrato import RegContrato


class RegContratoData():
    def registrar(self, info=RegContrato):
        self.db = con.Conexion().conectarBd()
        self.cursor= self.db.cursor()
        query =self.cursor.execute( "SELECT * FROM contratos WHERE num_contrato = '{}'".format(info._numContrato))
        result = query.fetchone()
        if result is None:    
            self.db = con.Conexion().conectarBd()
            self.cursor= self.db.cursor()
            query= self.cursor.execute("""INSERT INTO contratos values(null,'{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')
            """.format(info._numContrato, info._clienteFact, info._area, info._fechaInicio, info._fechaFin, info._cuota, info._dg, info._tipoContrato, info._statusContrato, info._statusVigencia, info._usuarioReg, info._fechaReg))
            self.db.commit()
            self.cursor.close()
            self.db.close()
            return True   
        else:
            return False
    
    def obtener_ultimo_contrato(self):
        self.db = con.Conexion().conectarBd()
        self.cursor= self.db.cursor()
        query= self.cursor.execute("SELECT * FROM contratos order by num_contrato desc limit 1")
        serch_info=query.fetchall()
        self.db.close()    
        return(serch_info)
    
    def obtener_contrato_x_fechaInio_fechaFinal(self, fechaInicio, fechaFin,cliente):
        self.db = con.Conexion().conectarBd()
        self.cursor= self.db.cursor()
        query= self.cursor.execute("SELECT area_comun FROM contratos WHERE fecha_inicio = '{}' AND fecha_fin = '{}' AND cliente = '{}'".format(fechaInicio, fechaFin, cliente))
        result=query.fetchone()
        self.db.close()    
        if result is None:
            return False
        else:
            return True
            
    def lista_contratos(self):
        self.db = con.Conexion().conectarBd()
        self.cursor= self.db.cursor()
        query= self.cursor.execute("SELECT * FROM contratos")
        serch_info=query.fetchall()
        self.db.close()    
        return(serch_info)
    
    
    
    def info_contratos(self,contrato):
        self.db = con.Conexion().conectarBd()
        self.cursor= self.db.cursor()
        query= self.cursor.execute("""SELECT cliente,area_comun,fecha_inicio,fecha_fin,cuota_mensual,deposito_garantia,status_activo,status_vencido FROM contratos WHERE num_contrato = '{}'""".format(contrato))
        serch_info=query.fetchall()
        self.db.close()    
        return(serch_info)
    
    
    