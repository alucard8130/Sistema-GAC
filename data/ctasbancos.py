#from model.ctasbancos import Cuentas
import conexion as con


# class CtasBancoData():
#     def consultar(self, info:Cuentas):
#         self.db = con.Conexion().conectarBd()
#         self.cursor= self.db.cursor()
#         query= self.cursor.execute("SELECT * FROM ctas_banco WHERE  num_cta='{}'".format(info._cta))
#         busqueda=query.fetchone()
#         if busqueda:
#             info_emp=Cuentas(info=busqueda[2])
#             self.cursor.close()
#             self.db.close()
#             return info_emp
#         else:
#             self.cursor.close()
#             self.db.close()
#             return None 
        
class CuentasData():
    def lista_ctas(self):
        self.db = con.Conexion().conectarBd()
        self.cursor= self.db.cursor()
        query= self.cursor.execute("SELECT * FROM ctas_banco order by num_cta")
        serch_info=query.fetchall()
        self.db.close()    
        return(serch_info)
                