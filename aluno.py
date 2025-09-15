class Aluno:
    nome = ""
    nota = 0

    def mostrarSituacao(self):
        if self.nota >= 5:
            print(self.nome, "foi aprovado")
        else:
            print(self.nome, "foi reprovado") 

a1 = Aluno()
a1.nome = "Diego"
a1.nota = 55

a1.mostrarSituacao()


































