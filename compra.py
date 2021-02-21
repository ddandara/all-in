from perfil import*
from sopa import*

class Compra:
    def __init__(self):
        self._perfil=None
        self._sopa=None

    def comprar(self,perfil, sopa):
        self._perfil=perfil
        self._sopa=Sopa

    def confirm_compra(self):
        return self._perfil.name+" comprou "+self._produto._nome