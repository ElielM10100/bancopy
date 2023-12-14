# # Classe pai
# class Funcionario:
#     def __init__(self, matricula, nome, salario):
#         self.matricula = matricula
#         self.nome = nome
#         self.salario = salario
#     def exibirDados(self):
#         # if isinstance(self, Professor):
#         #     print("Dados do professor!")
#         print("--- DADOS DO FUNCIONÁRIO ---")
#         print(f"Matricula: {self.matricula}")
#         print(f"Nome: {self.nome}")
#         print(f"Salário: {self.salario}")
#
# class Professor(Funcionario):
#     def __init__(self, matricula, nome, salario, turma):
#         super().__init__(matricula, nome, salario)
#         self.turma = turma
#
#     def exibirDados(self):
#         super().exibirDados()
#         print(f"Turma: {self.turma}")
#
# class Monitor(Funcionario):
#     def __init__(self, matricula, nome, salario, carga_horaria):
#         super().__init__(matricula, nome, salario)
#         self.carga_horaria = carga_horaria
#     def exibirDados(self):
#         super().exibirDados()
#         print(f'Carga horaria: {self.carga_horaria}')
# class Coordenador(Funcionario):
#     def __init__(self, matricula, nome, salario, area):
#         super().__init__(matricula, nome, salario)
#         self.area = area
#     def exibirDados(self):
#         super().exibirDados()
#         print(f'Área: {self.area}')
# p1 = Professor(1, "Luiz", 3500, "DFS519")
# p1.exibirDados()
#
# c1 = Coordenador(2, "Ana", 4500, "Exatas")
# c1.exibirDados()
#
# m1 = Monitor(3, "Julia", 1600, 300)
# m1.exibirDados()


# # Classe pai
# class Funcionario:
#     def __init__(self, matricula, nome, salario):
#         self.matricula = matricula
#         self.nome = nome
#         self.salario = salario
#     def exibirDados(self):
#         # if isinstance(self, Professor):
#         #     print("Dados do professor!")
#         print("--- DADOS DO FUNCIONÁRIO ---")
#         print(f"Matricula: {self.matricula}")
#         print(f"Nome: {self.nome}")
#         print(f"Salário: {self.salario}")
#
# class Professor(Funcionario):
#     def __init__(self, matricula, nome, salario, turma):
#         super().__init__(matricula, nome, salario)
#         self.turma = turma
#
#     def exibirDados(self):
#         super().exibirDados()
#         print(f"Turma: {self.turma}")
#
# class Monitor(Funcionario):
#     def __init__(self, matricula, nome, salario, carga_horaria):
#         super().__init__(matricula, nome, salario)
#         self.carga_horaria = carga_horaria
#     def exibirDados(self):
#         super().exibirDados()
#         print(f'Carga horaria: {self.carga_horaria}')
# class Coordenador(Funcionario):
#     def __init__(self, matricula, nome, salario, area):
#         super().__init__(matricula, nome, salario)
#         self.area = area
#     def exibirDados(self):
#         super().exibirDados()
#         print(f'Área: {self.area}')
# p1 = Professor(1, "Luiz", 3500, "DFS519")
# p1.exibirDados()
#
# c1 = Coordenador(2, "Ana", 4500, "Exatas")
# c1.exibirDados()
#
# m1 = Monitor(3, "Julia", 1600, 300)
# m1.exibirDados()


class Conta:
    def __init__(self, n_conta, cliente, saldo):
        self.n_conta = n_conta
        self.cliente = cliente
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor
        print(f"Deposito realizado com sucesso!")
        print(f"Saldo atual: {self.saldo}")

    def exibirDados(self):
        print(f"Número da conta: {self.n_conta}")
        print(f"Nome: {self.cliente}")
        print(f"Saldo: {self.saldo}")
class ContaCorrente(Conta):
    def __init__(self, n_conta, cliente, saldo, limite):
        super().__init__(n_conta, cliente, saldo)
        self.limite = limite

    def exibirDados(self):
        super().exibirDados()
        print(f"Limite: {self.limite}")

class ContaPoupanca(Conta):
    def __init__(self, n_conta, cliente, saldo, taxa):
        super().__init__(n_conta, cliente, saldo)
        self.taxa = taxa
    def exibirDados(self):
        super().exibirDados()
        print(f"Taxa de rendimentos: {self.taxa}%")

cc = ContaCorrente(1, "Alberto", 1000, 150)
cc.depositar(100)
cc.exibirDados()

poup = ContaPoupanca(1, "Adriana", 2500, 1)
poup.depositar(100)
poup.exibirDados()