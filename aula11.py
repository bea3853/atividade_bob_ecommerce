#DESAFIO
#EXPLICAR PORQUE UTILIZOU ESSA LÓGICA** 

# Enviar a lógica para esse e-mail: 
# Subir para o github**
# Enviar o link do repositório no e-mail:

# Titulo  -> Atividade Constantes Python

# beatriz.cristina@sp.senai.br

# DESENVOLVEDOR(A) DE BACK-END, E PRECISA DESENVOLVER AS 
# ESTRUTURAS BÁSICAS DO FUNCIONAMENTO DE UM E-COMMERCE
# CRIAR UM SISTEMA DE E-COMMERCE
# PRECISA TER UM FORMULÁRIO CADASTRO ok 
# O USUÁRIO PRECISA VER QUAIS PRODUTOS EXISTEM ok
# ESCOLHER O PRODUTO ok
# ESCOLHER A FORMA DE PAGAMENTO ok
# MENSAGEM DE DESPEDIDA ok


# FUNCTION -> LAMBDA FUNCÕES CLASSICAS TAMBÉM
# CONSTANTES
# NOME DO USÁRIO
# ID CODIGO PRODUTO
# CPF DO USUÁRIO


# sempre utilizar funções 



def cad(nome, cpf): 
    '''Funçaõ de cadastro irá cadastrar CPF E NOME '''
    print(f'''Dados do usuário:
    NOME -> {nome}
    CPF ->{cpf}
    ''')

def menu():
    print('''
    lapis -> id 0 
    caneta -> id 1
    borracha  -> id 2   
    
    ''')
  

def escolher_prod():
    lista_vazia = []
    lista = ['lapis', 'caneta', 'borracha' ]
    escolha =  int(input('Digite o ID'))
    lista_vazia.append(lista[escolha])
    print('Produtos', lista_vazia)
    mais = input('Deseja adicionar novos produtos, digite s, para não n:')
    while mais == 's':
        escolha2 =  int(input('Digite o ID do outro ptoduto'))
        lista_vazia.append(lista[escolha2])
        print('Produtos - ', lista_vazia)
        mais = input('Deseja adicionar novos produtos?digite s, para não n:') 
        
    else:
       print('Produtos:', lista_vazia) 


def pag():
    escolha =  input('Escolha o pagamento - 1 pix | 2 - CC ')
    if escolha  == '1':
       print('Pagamento realizado em PIX')
    elif escolha == '2':
        print('Pagamento realizado em CC')
    else: 
       print('Digite algo válido') 
       pag()

def despedida(nome):
    print('Obrigada pela preferência {} '.format(nome))



def ecommerce(): 
    NOME  =     input('Digite seu nome: ')
    CPF =   input('Digite seu CPF')
    cad(NOME, CPF)
    menu()
    escolher_prod()
    pag()
    despedida(NOME)




while True: 
    ecommerce()


