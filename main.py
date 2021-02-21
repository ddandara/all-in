#Faça a implementação do seu diagrama de classes completo na linguagem python.
#Faça a simulação de um pedido utilizando o programa. Utilize um menu para a navegação.
#Utilize o comando input para pedir dados do usuário durante o programa.


#Discente: Denise Dandara Gomes de Carvalho Severo.
#2º ano de Informática Matutino.
#Programação Orientada a Objetos

from delivery import*
from perfil import*
from sopa import*
from compra import*

perfil=Perfil()
comp=Compra()
sopa=Sopa()

comp.comprar(perfil,sopa)
#exibindo o verificar compra da nossa compra1
print(comp.ver_compra())
