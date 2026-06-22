from pessoa import Pessoa

from datetime import datetime

class ContaBancaria:
    
    def __init__(self, numero, agencia, titular: Pessoa, saldo=0):
        self.numero = numero
        self.agencia = agencia
        self.titular = titular
        self._saldo = saldo
        self.historico = []
        titular.adicionarConta(self)
        
    def __str__(self):
        return(
            f"contaBancaria(numero={self.numero})"
            f"titular={self.titular.nome}, saldo={self._saldo}"
        )
        
    def depositar(self, valor):
        if valor <= 0:
            raise ValueError("O valor do depósito deve ser maior que 0.")
        self._saldo += valor
        self._registrarOperacao("DEPÓSITO", valor)
        
    def sacar(self, valor):
        if valor <= 0:
            raise ValueError("O valor do saque deve ser maior que 0.")
        if valor > self._saldo:
            raise ValueError("Saldo insuficiente.")
        self._saldo -= valor
        self._registrarOperacao("SAQUE", valor)
        
    def consultarExtrato(self):
        return self.historico
    
    def consultarSaldo(self):
        return self._saldo
    
    
    def _registrarOperacao(self, tipo, valor, detalhe=""):
         registro= {
             "data": datetime.now().strftime("%d/%m/%Y, %H:%M:%S"),
             "tipo": tipo,
             "valor": valor,
             "detalhe": detalhe,
             "saldo_atual": self._saldo,
         }
         self.historico.append(registro)  
         
    def transferir(self, valor, contaDestino):
        if not isinstance(contaDestino, ContaBancaria):
            raise ValueError("Conta destino inválida.")  
        if valor <= 0:
            raise ValueError("O valor da transferência deve ser maior que 0.")
        if valor > self._saldo:
            raise ValueError("Saldo insuficiente para transferência.")
        self._saldo -= valor
        contaDestino._saldo += valor
        self._registrarOperacao("Transferência", valor, f"Transferência enviada para {contaDestino.numero}")
        contaDestino._registrarOperacao("Transferência", valor, f"Transferência recebida de {self.titular.nome}")
        