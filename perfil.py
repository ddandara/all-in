class Perfil:
    def __init__(self):
        self.name=input("++++++++++++++++++++  Primeiramente, qual o seu nome? ")
        self.login=input("Crie um nome de login: ")
        self.endereco=input("Insira o logradouro nº da casa e bairro: ")
        self.data_nasc=input("Insira sua data de nascimento: ")
        self.email=input("Digite um endereço de email válido: ")
        self.senha=input("Crie uma senha de no mínimo 8 caracteres, com ao menos uma letra e um número: ")
        
        
        """self.cpf=input("digite seu cpf:")
        if self.cpf==str:
          raise Exception("Apenas números são permitidos")"""

        while True:
          try:
              self.telefone=int(input("Nos informe seu número de telefone atual: "))
              break
          except ValueError:
              print("Apenas números inteiros são válidos! Tente novamente. Ex: 40028922")

        while True:
          try:
              self.cpf=int(input("Estamos quase finalizando, insira seu cpf: "))
              break

          except ValueError:
                print("O cpf deve conter apenas números inteiros. Exemplo: 05089923456")


    def consultperfil(self):
        return self.name

    def consultaNome(self):
        return self.name 

    