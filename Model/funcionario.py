from Model.pessoa import Pessoa


class Funcionario(Pessoa):
    def __init__(self, nome, cod, cursou):
        super().__init__(nome, cod)
        self.__cursou = cursou