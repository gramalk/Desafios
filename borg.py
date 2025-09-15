#Classe chamada Pesssoa
class Pessoa:
    #Atributos: características
    nome = "" #atributo nome
    idade = 0 #atributo idade
    cidade = ""
    profissao = ""

#Primeira Pessoa
p1 = Pessoa()
p1.nome = "Matheus Borges" 
p1.idade = 17
p1.cidade = "São Paulo"
p1.profissao = "bombardeiro"
#segunda Pessoa
    p2 = Pessoa()
    p2.nome = "Roberto"
    p2.idade = 16

#terceira Pessoa
    p3 = Pessoa()
    p3.nome = "Andrew"
    p3.idade = 27

#quarta Pessoa
    p4 = Pessoa()
    p4.nome = "Cesar"
    p4.idade = 22

#quinta Pessoa
    p5 = Pessoa()
    p5.nome = "julio"
    p5.idade = 43

#Imprimindo dados
Print("pessoa 1:", p1.nome, "-", p1.idade, " anos")
Print("Pessoa 2:", p2.nome, "-", p2.idade, " anos")