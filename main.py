"""Complete o projeto do bimestre anterior adicionando:

o tratamento de exceções que podem acontecer no seu programa.

utilize os comandos try, except e raise para tratar as possíveis exceções que podem ser lançadas pelo seu código

O uso de coleções de dados para gerenciar os itens da compra e a ordem dos pedidos.

utilize a coleção de dados apropriada para armazenar os objetos: Lista, fila, pilha, dicionário entre outras."""""

#Discente: Denise Dandara Gomes de Carvalho Severo.
#2º ano de Informática Matutino.
#Programação Orientada a Objetos

from delivery import*
from perfil import*
from sopa import*
from compra import*

perfil=Perfil()

sopa=Sopa()
sopa.mostrar_sopa()

comp=Compra(perfil,sopa)
#exibindo o verificar compra da nossa compra1
print(comp.ver_compra())
