from model.operaciones import Reg_Cartera, Reg_Factura
import conexion as con


class RegCarteraData():
    #funcion conecta a bd y registra un pago en base de datos cartera
    def _registrar(self, info=Reg_Cartera):
        self.db = con.Conexion().conectarBd()
        self.cursor= self.db.cursor()
        self.cursor.execute("""INSERT INTO cartera values(null,'{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')
        """.format(info._nl_o_a,info._cliente,info._tCartera,info._tCuota,info._tFactura,info._nFact,info._iAdeudo,info._iPago,info._iSaldo,info._feP_C,info._cta,
                   info._foPago,info._cheque,info._nContrato,info._sPago,info._usuario,info._feReg,info._comm))
        self.db.commit()
        if self.cursor.rowcount==1:
            return True
        else:
            return False
            
        
class RegFacturaData():
    #funcion conecta a bd y registra un pago en base de datos cobranza
    def _registrar(self, info=Reg_Factura):
        self.db = con.Conexion().conectarBd()
        self.cursor= self.db.cursor()
        self.cursor.execute("""INSERT INTO facturas values(null,'{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')
        """.format(info._num_factura,info._cliente,info._nl_o_a,info._fecha_factura,info._tipo_cuota,info._importe_factura,info._tipo_factura,info._tipo_cartera,
                   info._status_pago,info._usuario,info._fecha_reg))
        self.db.commit()        
        if self.cursor.rowcount==1:
            return True
        else:
            return False
        