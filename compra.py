from perfil import*
from sopa import*

class Compra:
    def __init__(self,perfil, sopa):
        self._perfil=perfil
        self._sopa=sopa

    def ver_compra(self):
        return str(self._perfil.consultperfil()) + " comprou " + str(self._sopa.nome)