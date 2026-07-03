# EXERCÍCIO 1
# class Retangulo:
#     def __init__(self, comprimento, largura):
#         self.comprimento = comprimento
#         self.largura = largura

#     def area(self):
#         return self.comprimento * self.largura

#     def perimetro(self):
#         return 2 * (self.comprimento + self.largura)
# retangulo = Retangulo(10, 5)
# print(f"Área do Retângulo: {retangulo.area()}")
# print(f"Perímetro do Retângulo: {retangulo.perimetro()}")


# EXERCÍCIO 2
# class Pessoa:
#     def __init__(self, nome, idade):
#         self.nome = nome
#         self.idade = idade

#     def exibir_informacoes(self):
#         return f"Nome: {self.nome}, Idade: {self.idade} anos"
# pessoa1 = Pessoa("Ana", 16)
# print(pessoa1.exibir_informacoes())


# EXERCÍCIO 3
# class Produto:
#     def __init__(self, nome, preco, quantidade):
#         self.nome = nome
#         self.preco = preco
#         self.quantidade = quantidade

#     def valorTotal(self):
#         return self.preco * self.quantidade

# produto1 = Produto("Notebook", 4500.00, 4)
# print(f"Produto: {produto1.nome} | Valor Total em Estoque: R${produto1.valorTotal():}")


# EXERCÍCIO 4
# class ContaBancaria:
#   def __init__(self, saldo):
#     self.saldo = saldo  

#   def depositar(self, valor):
#     if valor < 0:
#       return "Valor Inválido. Digite um número positivo!"
#     else:
#       self.saldo += valor
#       return "Saldo atualizado com sucesso!"

#   def sacar(self, valor):
#     if valor > self.saldo:
#       return "Saldo Insuficiente!"
#     elif self.saldo:
#       return "Sem saldo na conta!"
#     else:
#       self.saldo -= valor
#       return "Saque efetuado com sucesso!"

# contaAna = ContaBancaria(100)
# print(contaAna.depositar(50))
# print(contaAna.sacar(50))


# EXERCÍCIO 5
# class Aluno:
#     def __init__(self, matricula, nome, nota_p1, nota_p2, nota_trabalho):
#         self.matricula = matricula
#         self.nome = nome
#         self.nota_p1 = nota_p1
#         self.nota_p2 = nota_p2
#         self.nota_trabalho = nota_trabalho

#     def media(self):
#         return ((self.nota_p1 * 2.5) + (self.nota_p2 * 2.5) + (self.nota_trabalho * 2)) / 7

#     def notaFinal(self):
#         media_atual = self.media()
#         if media_atual >= 7.0:
#             return 0.0
#         else:
#             return 7.0 - media_atual

# aluno1 = Aluno("202601", "Ana", 10.0, 10.0, 10.0)
# print(f"Aluno: {aluno1.nome} | Média Semestral: {aluno1.media():}")
# print(f"Necessita para a Prova Final: {aluno1.notaFinal():}")


# EXERCÍCIO 6
# class PessoaEvolutiva:
#     def __init__(self, nome, idade, peso, altura):
#         self.nome = nome
#         self.idade = idade
#         self.peso = peso
#         self.altura = altura

#     def envelhecer(self, anos=1):
#         for _ in range(anos):
#             if self.idade < 21:
#                 self.crescer(0.08)  
#             self.idade += 1

#     def engordar(self, quilos):
#         self.peso += quilos

#     def emagrecer(self, quilos):
#         self.peso -= quilos

#     def crescer(self, metros):
#         self.altura += metros

# jovem = PessoaEvolutiva("Ana", 16, 44.0, 1.50)
# print(f"Antes - Idade: {jovem.idade} anos, Altura: {jovem.altura:}m")
# jovem.envelhecer(2)
# print(f"Depois - Idade: {jovem.idade} anos, Altura: {jovem.altura:}m")


# EXERCÍCIO 7
# class ContaInvestimento:
#     def __init__(self, saldo_inicial, taxa_juros):
#         self.saldo = saldo_inicial
#         self.taxa_juros = taxa_juros  

#     def adicione_juros(self):
#         self.saldo += self.saldo * (self.taxa_juros / 100)

# poupanca = ContaInvestimento(1000.00, 10)

# for i in range(5):
#     poupanca.adicione_juros()

# print(f"Saldo resultante após render juros 5 vezes: R${poupanca.saldo:}")


# EXERCÍCIO 8
# class BombaCombustivel:
#     def __init__(self, tipo_combustivel, valor_litro, quantidade_combustivel):
#         self.tipo_combustivel = tipo_combustivel
#         self.valor_litro = valor_litro
#         self.quantidade_combustivel = quantidade_combustivel

#     def abastecer_por_valor(self, valor):
#         litros_abastecidos = valor / self.valor_litro
#         if litros_abastecidos > self.quantidade_combustivel:
#             print("Não há combustível suficiente na bomba para este abastecimento.")
#         else:
#             self.quantidade_combustivel -= litros_abastecidos
#             print(f"Foram colocados {litros_abastecidos:} litros de {self.tipo_combustivel}.")

#     def abastecer_por_litro(self, litros):
#         if litros > self.quantidade_combustivel:
#             print("Não há combustível suficiente na bomba para este abastecimento.")
#         else:
#             valor_a_pagar = litros * self.valor_litro
#             self.quantidade_combustivel -= litros
#             print(f"Valor a ser pago pelo cliente: R${valor_a_pagar:}")

#     def alterar_valor(self, novo_valor):
#         self.valor_litro = novo_valor

#     def alterar_combustivel(self, novo_tipo):
#         self.tipo_combustivel = novo_tipo

#     def alterar_quantidade_combustivel(self, nova_quantidade):
#         self.quantidade_combustivel = nova_quantidade

# bomba = BombaCombustivel("Gasolina", 5.50, 1000)
# bomba.abastecer_por_valor(110.00)
# print(f"Combustível restante na bomba: {bomba.quantidade_combustivel:} litros.")


# EXERCÍCIO 9
# class Usuario:
#     def __init__(self, usuario, senha):
#         self.usuario = usuario
#         self.senha = senha

#     def verifica_senha(self, entrada_senha):
#         return entrada_senha == self.senha

# user = Usuario("ana", "01102609ana")
# print("Senha correta?", user.verifica_senha("01102609ana"))


# EXERCÍCIO 10
# class Temperatura:
#     def __init__(self, celsius):
#         self.celsius = celsius

#     def celsius_fahrenheit(self):
#         return (self.celsius * 9/5) + 32

#     def celsius_kelvin(self):
#         return self.celsius + 273.15

# temp = Temperatura(25)
# print(f"Temperatura em Fahrenheit: {temp.celsius_fahrenheit()}°F")
# print(f"Temperatura em Kelvin: {temp.celsius_kelvin()}K")
