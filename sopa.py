from carrinho import *
from compra import *

class Sopa:

    def __init__(self, nn, preco, sabor, acompanhamento, qnt):
        self.nome = input("Qual sopa da casa você deseja? ")
        self.nn = nn
        self.preco = preco
        self.sabor = sabor
        self.acompanhamento = acompanhamento
        self.qnt = qnt


    def mostrar_preco(self):
        print(self.preco)

    def mostrar_sabor(self):
        print(self.sabor)

    def mostrar_acompanhamento(self):
        print(self.acompanhamento)

    def mostrar_qnt(self):
        print(self.qnt)

    def mostrar_nn(self):
        print(self.nn, "->Esse foi o prato escolhido")
        


    def mostrar_sopa(self):
        if(nome=="Matryoshka"):
          print(self.soup1)

        elif(nome=="Hellevator"):
          print(self.soup2)

        elif(nome=="Chronosaurus"):
          print(self.soup3)

        elif(nome=="WOW"):
          print(self.soup4)

        else: 
          print("Sopa não disponível")

class Legumes(Sopa):
    def __init__(self, nn, preco, sabor, acompanhamento, qnt, tpnoodle, tpverdura):
        Sopa.__init__(self, nn, preco, sabor, acompanhamento, qnt)
        self.tpnoodle = tpnoodle
        self.tpverdura = tpverdura

    def mostrar_tpnoodle(self):
        print(self.tpnoodle)

    def mostrar_tpverdura(self):
        print(self.tpverdura)

    def verificar_disponibilidade(self):
        print(self.nome, "Esse prato está disponível")


class Carne(Sopa):
    def __init__(self, nn, preco, sabor, acompanhamento, qnt, tparroz, tpcarne):
        Sopa.__init__(self, nn, preco, sabor, acompanhamento, qnt)
        self.tparroz = tparroz
        self.tpcarne = tpcarne

    def mostrar_tparroz(self):
        print(self.tparroz)

    def mostrar_tpcarne(self):
        print(self.tpcarne)

    def verificar_disponibilidade(self):
        print(self.nome, "Esse prato está disponível")



Matryoshka("Carne", 15, "sabor: caldo de frango", "acompanhamento: batata", 1, "arroz branco",
              "carne de frango")


Chronosaurus("Legumes", 18, "sabor: legumes ao molho de feijão", "acompanhamento: bacon", 1,
                "macarrão talharim", "ervilha")

WOW("Legumes", 16, "sabor: Legumes variados", "acompanhamento: bacon e croutons", 1, "macarrão parafuso",
                "repolho")

Hellevator("Carne", 15, "sabor: carne picante", "acompanhamento: Bruschetta", 1, "arroz cateto", "carne bovina")