from PyQt6.QtWidgets import QApplication, QMessageBox
from gui.main import PantallaPrincipal


#
class Gestor():
    def __init__(self):
        self.app=QApplication([])
        self.pp=PantallaPrincipal()
 
        self.app.exec()