import os
import time
from pessoa import Pessoa
from contabancaria import ContaBancaria



# Listas globais na memória (iguais ao seu modelo)
clientes_cadastrados = []
contas_cadastradas = []
def carregarDados():
    global clientes_cadastrados, contas_cadastradas
    if not os.path.exists("banco_dados.txt"):
        return
        
    with open("banco_dados.txt", "r", encoding="utf-8") as f:
        linhas = f.readlines()
        
    for linha in linhas:
        linha = linha.strip()
        if not linha:
            continue
            
        partes = linha.split(";")
        tipo = partes[0]
        
        if tipo == "CLIENTE":
            # CLIENTE;nome;email;cpf
            nome = partes[1]
            email = partes[2]
            cpf = partes[3]
            novo_cliente = Pessoa(nome, email, cpf)
            clientes_cadastrados.append(novo_cliente)
            
        elif tipo == "CONTA":
            # CONTA;numero;agencia;cpf_titular;saldo
            numero = partes[1]
            agencia = partes[2]
            cpf_titular = partes[3]
            saldo = float(partes[4])
            
            # Procura o titular correspondente na lista
            titular_encontrado = None
            for cliente in clientes_cadastrados:
                if cliente.cpf == cpf_titular:
                    titular_encontrado = cliente
                    break
            
            if titular_encontrado:
                nova_conta = ContaBancaria(numero, agencia, titular_encontrado, saldo)
                contas_cadastradas.append(nova_conta)

def salvarDados():
    with open("banco_dados.txt", "w", encoding="utf-8") as f:
        # Salva todos os clientes primeiro
        for cliente in clientes_cadastrados:
            f.write(f"CLIENTE;{cliente.nome};{cliente.email};{cliente.cpf}\n")
        # Salva todas as contas criadas
        for conta in contas_cadastradas:
            f.write(f"CONTA;{conta.numero};{conta.agencia};{conta.titular.cpf};{conta.consultarSaldo()}\n")
            
def menu():
    carregarDados()
    while True:
        print("\n===== Sistema Bancário =====")
        print("1 - Cadastrar Cliente")
        print("2 - Criar Conta Bancária")
        print("3 - Depositar")
        print("4 - Consultar Extrato")
        print("0 - Sair")

        opcao = int(input("Escolha: "))

        if opcao == 1:
            nome = str(input("Digite o nome: "))
            email = str(input("Digite o email: "))
            cpf = str(input("Digite o CPF: "))
            
            # Verifica se o cliente já existe
            existe = False
            for c in clientes_cadastrados:
                if c.cpf == cpf:
                    existe = True
                    break
                    
            if not existe:
                cliente = Pessoa(nome, email, cpf)
                clientes_cadastrados.append(cliente)
                salvarDados()
                print("Cliente cadastrado com sucesso!")
            else:
                print("CPF já cadastrado!")
            input("Pressione ENTER para continuar...")

        elif opcao == 2:
            cpf = str(input("Digite o CPF do cliente: "))
            
            titular = None
            for c in clientes_cadastrados:
                if c.cpf == cpf:
                    titular = c
                    break
                    
            if titular:
                numero = str(input("Digite o numero da conta: "))
                agencia = str(input("Digite a agencia: "))
                
                conta = ContaBancaria(numero, agencia, titular)
                contas_cadastradas.append(conta)
                salvarDados()
                print("Conta criada com sucesso!")
            else:
                print("Cliente não encontrado!")
            input("Pressione ENTER para continuar...")

        elif opcao == 3:
            numero = str(input("Digite o numero da conta: "))
            
            conta_encontrada = None
            for c in contas_cadastradas:
                if c.numero == numero:
                    conta_encontrada = c
                    break
                    
            if conta_encontrada:
                valor = float(input("Digite o valor do deposito: "))
                conta_encontrada.depositar(valor)
                salvarDados()
                print("Depósito realizado com sucesso!")
            else:
                print("Conta não encontrada!")
            input("Pressione ENTER para continuar...")

        elif opcao == 4:
            numero = str(input("Digite o numero da conta: "))
            
            conta_encontrada = None
            for c in contas_cadastradas:
                if c.numero == numero:
                    conta_encontrada = c
                    break
                    
            if conta_encontrada:
                # Usa exatamente o método consultarExtrato que você criou
                print("Histórico de Operações:")
                print(conta_encontrada.consultarExtrato())
            else:
                print("Conta não encontrada!")
            input("Pressione ENTER para continuar...")

        elif opcao == 0:
            print("Encerrando...")
            time.sleep(2)
            break
        else:
            print("Opção inválida!")
            time.sleep(2)
            
        os.system("cls")

if __name__ == "__main__":
    menu()