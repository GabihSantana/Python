# SOLID
# S - Single Responsability -> responsabilidade única

class SistemaCadastral:

    def cadastrar(self, nome: str, idade: int) -> None:
        if isinstance(nome, str) and isinstance(idade, int):
            print("Acessando o banco de dados...")
            print(f"Cadastrar usuário {nome}, idade {idade}")
        else:
            print("Dados inválidos")

pessoa = SistemaCadastral()
pessoa.cadastrar(2, 4)