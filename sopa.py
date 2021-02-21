class Sopa:

    def __init__(self, nn, preco, sabor, acompanhamento):
        self.nome=input("Qual sopa da casa você deseja?")
        self.nn = nn
        self.preco = preco
        self.sabor = sabor
        self.acompanhamento = acompanhamento


    def mostrar_sopa(self):
        if(nome=="Matryoshka"):
          print(soup1.items())

    def mostrar_sopa2(self):
        if(nome=="Hellevator"):
          print(soup2.items())

    def mostrar_sopa3(self):
        if(nome=="Chronosaurus"):
          print(soup3.items())
          
    def mostrar_sopa4(self):
        if(nome=="WOW"):
          print(soup4.items())

    def mostrar_preco(self):
        print(self.preco)

    def mostrar_sabor(self):
        print(self.sabor)

    def mostrar_acompanhamento(self):
        print(self.acompanhamento)

    def mostrar_nn(self):
        print(self.nn, "->Esse foi o prato escolhido")


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


soup1=dict()
soup1= {'nome':'Matryoshka', 'preço': 15, 'sabor': 'caldo de frango', 'acompanhamento': 'batata','tparroz': 'arroz branco', 'tpcarne': 'carne de frango'}

soup2=dict()
soup2 = {'nome':'Hellevator', 'preço': 17, 'sabor': 'carne picante', 'acompanhamento': 'Bruschetta', 'tparroz': 'arroz cateto', 'tpcarne':'carne bovina'}

soup3=dict()
soup3 = {'nome':'Chronosaurus', 'preço': 18, 'sabor': 'legumes ao molho de feijão', 'acompanhamento': 'bacon', 'tpnoodle': 'macarrão talharim', 'tpverdura':'ervilha'}

soup4=dict()
soup4 = {'nome':'WOW', 'preço': 16, 'sabor': 'Legumes variados', 'acompanhamento': 'bacon e croutons', 'tpnoodle':'macarrão parafuso', 'tpverdura':'repolho'}

