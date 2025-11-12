
import json

arquivo_estudantes = "estudantes.json"
arquivo_disciplinas = "disciplinas.json"
arquivo_professores = "professores.json"

def menuprincipal():
    print('=-' * 35)
    print(f'Bem vindo(a) {login} ao seu CRUD - ambiente de gestão de dados acadêmicos')
    print('=-' * 35)
    return int(input('Sobre o que deseja gerenciar?\n 1 - estudantes\n 2 - disciplinas\n 3 - professores\n 4 - sair\n'))

def inclusao_cadastro(nome_arquivo, eh_pessoa):
    if eh_pessoa == "sim":
        while True:
            nome_cadastro = str(input('Digite o nome que você deseja incluir: '))
            cpf_cadastro = str(input('Digite o CPF: '))
            try:
                codigo_cadastro = int(input('Digite o nº de matrícula ou o código: '))
                break
            except ValueError:
                print('Opção inválida, digite apenas números.')
                continue
        cadastro = {
            'nome': nome_cadastro,
            'cpf': cpf_cadastro,
            'codigo': codigo_cadastro
        }
    else:
        while True:
            nome_cadastro = str(input('Digite o nome que você deseja incluir: '))
            try:
                codigo_cadastro = int(input('Digite o código: '))
                break
            except ValueError:
                print('Opção inválida, digite apenas números.')
                continue

        cadastro = {
            'nome': nome_cadastro,
            'codigo': codigo_cadastro
        }
    lista = ler_arquivo(nome_arquivo)
    lista.append(cadastro)
    print(f'Cadastro de: {nome_cadastro} incluído com sucesso\n')
    salvar_arquivo(lista, nome_arquivo)

def listagem_cadastro(nome_arquivo):
    lista = ler_arquivo(nome_arquivo)
    print(f'Lista atualizada de cadastros: \n{lista}\n')

def edicao_cadastro(nome_arquivo, eh_pessoa):
    lista = ler_arquivo(nome_arquivo)
    for i, cadastro in enumerate(lista):
        print('***' * 10)
        print(f'{i} - {cadastro}')
        print('***' * 10)
    if eh_pessoa == "sim":
        while True:
            indice_cadastro = int(input('Digite o número correspondente do cadastro que deseja editar: '))
            nome = input('Novo nome: ')
            cpf = input('Novo CPF: ')
            try:
                matricula = int(input('Nova matrícula ou código: '))
                break
            except ValueError:
                print('Opção inválida, digite apenas números.')
                continue
        lista[indice_cadastro].update({
            'nome': nome,
            'cpf': cpf,
            'matricula': matricula
        })
    else:
        indice_cadastro = int(input('Digite o número correspondente do cadastro que deseja editar: '))
        nome = input('Novo nome: ')
        codigo = int(input('Novo código: '))
        lista[indice_cadastro].update({
            'nome': nome,
            'codigo': codigo})

    print(f'Cadastro: {indice_cadastro} atualizado com sucesso\n')
    salvar_arquivo(lista, nome_arquivo)

def excluir_cadastro(nome_arquivo):
    lista = ler_arquivo(nome_arquivo)
    for i, cadastro in enumerate(lista):
        print('***' * 10)
        print(f'{i} - {cadastro}')
        print('***' * 10)
    indice_cadastro = int(input('Digite o número correspondente do estudante que deseja excluir: '))
    print(f'Estudante {indice_cadastro} excluído com sucesso\n')
    lista.pop(indice_cadastro)  # aqui voce exclui o estudante da lista
    salvar_arquivo(lista, nome_arquivo)

def menu_edicoes_pessoas(nome_arquivo):
    while True:
        escolha = int(input(
            'O que deseja fazer?\n 1 - incluir\n 2 - listar\n 3 - editar\n 4 - excluir\n 5 - sair\n 6 - Voltar ao menu principal'))
        print('###' * 10)
        if escolha == 1:
            inclusao_cadastro(nome_arquivo, "sim")
        elif escolha == 2:
            listagem_cadastro(nome_arquivo)
        elif escolha == 3:
            edicao_cadastro(nome_arquivo)
        elif escolha == 4:
            excluir_cadastro(nome_arquivo)
        elif escolha == 5:
            print('Você saiu do sistema.')
            exit()  # função que sai do sistema
        elif escolha == 6:
            break  # encerra o segundo loop de while true e volta pro loop anterior
def menu_edicao_disciplinas(nome_arquivo):
    while True:
        escolha = int(input(
            'O que deseja fazer?\n 1 - incluir\n 2 - listar\n 3 - editar\n 4 - excluir\n 5 - sair\n 6 - Voltar ao menu principal'))
        print('###' * 10)
        if escolha == 1:
            inclusao_cadastro(nome_arquivo, "nao")
        elif escolha == 2:
            listagem_cadastro(nome_arquivo)
        elif escolha == 3:
            edicao_cadastro(nome_arquivo, "nao")
        elif escolha == 4:
            excluir_cadastro(nome_arquivo)
        elif escolha == 5:
            print('Você saiu do sistema.')
            exit()  # função que sai do sistema
        elif escolha == 6:
            break  # encerra o segundo loop de while true e volta pro loop anterior

def menuoperacoes():
    while True:
        menu = menuprincipal()
        if menu == 4:
            print('Você saiu do sistema')
            break  # aqui voce sai do ambiente, encerrando o loop
        if menu == 1:
            print(f'Você escolheu estudantes.')
            menu_edicoes_pessoas(arquivo_estudantes)
        elif menu == 2:
            print(f'Você escolheu disciplinas.')
            menu_edicao_disciplinas(arquivo_disciplinas)
        elif menu == 3:
            print(f'Você escolheu professores.')
            menu_edicoes_pessoas(arquivo_professores)
        else:
            print('Opção INVÁLIDA! Digite novamente.')

def salvar_arquivo(lista, nome_arquivo):
    with open(nome_arquivo, 'w', encoding='utf-8') as arquivo_aberto:
        json.dump(lista, arquivo_aberto, ensure_ascii=False)

def ler_arquivo(nome_arquivo):
    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo_aberto:
            lista = json.load(arquivo_aberto)
        return lista
    except:
        return []


login = input('login: ')
senha = input('senha: ')

menuoperacoes()