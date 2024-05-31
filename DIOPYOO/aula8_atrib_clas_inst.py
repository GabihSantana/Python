class Estudante:
    # variável de classe - a msm p todos:
    escola = "DIO"

    def __init__(self, nome, matricula):
        # Variável de instância - diferente p cada: 
        self.nome = nome 
        self.matricula = matricula

    def __str__(self) -> str:
        return f"{self.nome} - {self.matricula} - {self.escola}" 

def mostrar_valores(*objs):
    for obj in objs:
        print(obj) 

aluno_1 = Estudante("Giovana", 10587)
aluno_2 = Estudante("Julia", 10954)

mostrar_valores(aluno_1, aluno_2)
Estudante.escola = "Python" # alterando a variável da classe
aluno_1.matricula = 32598
mostrar_valores(aluno_1, aluno_2)
