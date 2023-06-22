import mysql.connector

def conectar_banco():
    conexao = mysql.connector.connect(
        host='localhost',
        user='root',
        password='123456',
        database='cadastro',
    )
    return conexao

def criar_registro(conexao):
    cursor = conexao.cursor()
    nome = input("Digite o nome para adicionar ao banco de dados: ")
    comando = f'INSERT INTO ESTADO(Nome) VALUES("{nome}")'
    cursor.execute(comando)
    conexao.commit()
    print("Registro criado com sucesso!")

def exibir_registros(conexao):
    cursor = conexao.cursor()
    comando = 'SELECT * FROM ESTADO'
    cursor.execute(comando)
    resultados = cursor.fetchall()
    for resultado in resultados:
        print(resultado)

def atualizar_registro(conexao):
    cursor = conexao.cursor()
    id_estado = input("Digite o ID do estado a ser atualizado: ")
    nome = input("Digite o novo nome: ")
    comando = f'UPDATE ESTADO SET Nome="{nome}" WHERE IDEstado={id_estado}'
    cursor.execute(comando)
    conexao.commit()
    print("Registro atualizado com sucesso!")

def deletar_registro(conexao):
    cursor = conexao.cursor()
    id_estado = input("Digite o ID do estado a ser deletado: ")
    comando = f'DELETE FROM ESTADO WHERE IDEstado={id_estado}'
    cursor.execute(comando)
    conexao.commit()
    print("Registro deletado com sucesso!")

def menu():
    print("Escolha uma opção:")
    print("1. Criar registro")
    print("2. Exibir registros")
    print("3. Atualizar registro")
    print("4. Deletar registro")
    print("0. Sair")

def main():
    conexao = conectar_banco()

    while True:
        menu()
        opcao = input("Digite o número da opção desejada: ")

        if opcao == '1':
            criar_registro(conexao)
        elif opcao == '2':
            exibir_registros(conexao)
        elif opcao == '3':
            atualizar_registro(conexao)
        elif opcao == '4':
            deletar_registro(conexao)
        elif opcao == '0':
            break
        else:
            print("Opção inválida. Digite um número válido.")

    conexao.close()
    print("Programa encerrado.")

if __name__ == '__main__':
    main()
