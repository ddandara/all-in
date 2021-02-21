class Perfil:
    def __init__(self):
        self.name=input("+++++++++++++++++++++++  Primeiramente, qual o seu nome?")
        self.login=input("Crie um nome de login: ")

        self.endereco=input("Insira o logradouro nº da casa e bairro: ")
        self.data_nasc=input("Insira sua data de nascimento: ")
        self.cpf=input("Estamos quase finalizando, insira seu cpf: ")
        self.email=input("Digite um endereço de email válido: ")
        self.senha=input("Crie uma senha de no mínimo 8 caracteres, com ao menos uma letra e um número: ")
        
    try:
        telefone=input("Nos informe seu número de telefone atual: ")
        telefone=int(telefone)
    except ValueError:
        print("Inteiro não valido! Tente novamente")

    
    def consultperfil(self):
        return self.name

    def consultaNome(self):
        return self.name 

    