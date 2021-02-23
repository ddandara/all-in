class Sopa:

    def __init__(self, nn=None, preco=None, sabor=None, acompanhamento=None):
        self.nome=input("Qual sopa da casa você deseja? ")
        self.nn = nn
        self.preco = preco
        self.sabor = sabor
        self.acompanhamento = acompanhamento

    
    def mostrar_sopa(self):
        if(self.nome=="Matryoshka"):
          print(soup1)

        elif(self.nome=="Hellevator"):
          print(soup2)

        elif(self.nome=="Chronosaurus"):
          print(soup3)
          
        elif(self.nome=="WOW"):
          print(soup4)

        else:
          print("teste")

    def mostrar_preco(self):
      if(self.nome=="Matryoshka"):
        print(soup1["preço"])

      elif(self.nome=="Hellevator"):
        print(soup2["preço"])

      elif(self.nome=="Chronosaurus"):
        print(soup3["preço"])
          
      elif(self.nome=="WOW"):
        print(soup4["preço"])


    def mostrar_sabor(self):
      if(self.nome=="Matryoshka"):
        print(soup1["sabor"])

      elif(self.nome=="Hellevator"):
        print(soup2["sabor"])

      elif(self.nome=="Chronosaurus"):
        print(soup3["sabor"])
          
      elif(self.nome=="WOW"):
        print(soup4["sabor"])

    def mostrar_acompanhamento(self):
      if(self.nome=="Matryoshka"):
        print(soup1["acampanhamento"])

      elif(self.nome=="Hellevator"):
        print(soup2["acompanhamento"])

      elif(self.nome=="Chronosaurus"):
        print(soup3["acampanhamento"])
          
      elif(self.nome=="WOW"):
        print(soup4["acompanhamento"])

    def mostrar_nn(self):
      if(self.nome=="Matryoshka"):
        print(soup1["nome"])

      elif(self.nome=="Hellevator"):
        print(soup2["nome"])

      elif(self.nome=="Chronosaurus"):
        print(soup3["nome"])
          
      elif(self.nome=="WOW"):
        print(soup4["nome"])


class Legumes(Sopa):
    def __init__(self, nome, preço, sabor, acompanhamento, tpnoodle, tpverdura):
        Sopa.__init__(self, nome, preço, sabor, acompanhamento)
        self.tpnoodle = tpnoodle
        self.tpverdura = tpverdura

    def mostrar_tpnoodle(self):
        print(self.tpnoodle)

    def mostrar_tpverdura(self):
        print(self.tpverdura)

    def verificar_disponibilidade(self):
        print(self.nome, "Esse prato está disponível")


class Carne(Sopa):
    def __init__(self, nome, preço, sabor, acompanhamento,tparroz, tpcarne):
        Sopa.__init__(self, nome, preço, sabor, acompanhamento)
        self.tparroz = tparroz
        self.tpcarne = tpcarne

    def mostrar_tparroz(self):
        print(self.tparroz)

    def mostrar_tpcarne(self):
        print(self.tpcarne)

    def verificar_disponibilidade(self):
        print(self.nome, "Esse prato está disponível")

#opc=input("Qual sopa da casa você deseja?")

soup1=dict()
soup1= {'nome':'Matryoshka', 'preço': 15, 'sabor': 'caldo de frango', 'acompanhamento': 'batata','tparroz': 'arroz branco', 'tpcarne': 'carne de frango'}

soup2=dict()
soup2 = {'nome':'Hellevator', 'preço': 17, 'sabor': 'carne picante', 'acompanhamento': 'Bruschetta', 'tparroz': 'arroz cateto', 'tpcarne':'carne bovina'}

soup3=dict()
soup3 = {'nome':'Chronosaurus', 'preço': 18, 'sabor': 'legumes ao molho de feijão', 'acompanhamento': 'bacon', 'tpnoodle': 'macarrão talharim', 'tpverdura':'ervilha'}

soup4=dict()
soup4 = {'nome':'WOW', 'preço': 16, 'sabor': 'Legumes variados', 'acompanhamento': 'bacon e croutons', 'tpnoodle':'macarrão parafuso', 'tpverdura':'repolho'}

"""if opc == soup1["nome"]:
  print(soup1) 

elif opc == soup2["nome"]: 
  print(soup2)

elif opc == soup3["nome"]: 
  print(soup3)

elif opc == soup4["nome"]: 
  print(soup4)"""
