#DESAFIO: Mini Sistema de Cadastro com Lista
# Objetivo:

#Criar um programa de cadastro de alunos que permita:
#1️ Adicionar alunos
#2️ Listar todos os alunos
#3️ Remover um aluno
#4️ Sair do programa

#Regras:

#Use listas para armazenar os nomes.

#Use um while para deixar o menu rodando até o usuário sair.

#Use if, elif, else para as opções.

#Trate erros (ex: se tentar remover um nome que não existe).
#DESAFIO SIMPLES E HARDCORE



class Cadastro:
    def __init__(self):
        self.lista = [
            {"nome": "edy"},
            {"nome": "jojo"},
            {"nome": "mia"},
            {"nome": "jeremias"},
            {"nome": "clebin"},
            {"nome": "duts"}
        ]

    def adicionar(self):
        nome = input('Adicionar nome: ').strip().title()

        if not nome.isalpha():
            print('apenas letras.')
            return

        for pessoa in self.lista:
            if pessoa["nome"].lower() == nome.lower():
                print('esse nome ja existe !')
                return

        self.lista.append({"nome": nome})
        print(f' {nome} foi adicionado com sucesso!')

    def listar(self):
        if not self.lista:
            print(' Nenhum nome cadastrado ainda.')
        else:
            print('\n lista de nomes ! ')
            for i, pessoa in enumerate(self.lista):
                print(f'{i}. {pessoa["nome"]}')
           

    def remover(self):
        nome = input('Remover nome: ').strip().title()

        for pessoa in self.lista:
            if pessoa["nome"].lower() == nome.lower():
                self.lista.remove(pessoa)
                print(f'{nome} foi removido com sucesso!')
                return
        print(' Nome não encontrado.')

    def menu(self):
        while True:
            print('''
  inicio
1 - Adicionar aluno
2 - Listar alunos
3 - Remover aluno
4 - Sair
''')
            opcao = input('Escolha uma opção: ').strip()

            if opcao == '1':
                self.adicionar()
            elif opcao == '2':
                self.listar()
            elif opcao == '3':
                self.remover()
            elif opcao == '4':
                print(' Encerrando o sistema...')
                break
            else:
                print(' Opção inválida! Tente novamente.')

sistema = Cadastro()
sistema.menu()