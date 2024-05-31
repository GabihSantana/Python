# Responsabilidade única -> Módularizado, tudo separado

class SistemaCadastral:

    def cadastrar(self, nome: str, idade: int) -> None:
        if self.__validate_input(nome, idade):
            self.__register_user(nome, idade)
        else:
            self.__erro_handle()

    def __validate_input(self, nome: str, idade: int) -> bool:
        return isinstance(nome, str) and isinstance(idade, int)
    
    def __register_user(self, nome: str, idade: int) -> None:
        print("Acessando o banco de dados...")
        print(f"Cadastrar usuário {nome}, idade {idade}")

    def __erro_handle(self) -> None:
        print("Dados inválidos")

pessoa = SistemaCadastral()
pessoa.cadastrar(2, 4)