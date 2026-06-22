class Pessoa:
    def __init__(self, nome,email,cpf):
        self.nome = nome
        self.email = email
        self.cpf = cpf
        self.contas = []
        
        def __str__(self):
            return f"Pessoa(nome={self.nome}, cpf={self.cpf})"
        
        def adicionarConta(self, conta):
            self.contas.append(conta)
            
            
        def listarContas(self):
            numeroContas=[]
            for conta in self.contas:
                numeroContas.append(conta.numero)
            return numeroContas

        def atualizarEmail(self, novoEmail):
            self.email = novoEmail