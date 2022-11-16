from Model.pessoa import Pessoa


class Profissional(Pessoa):
    def __init__(self, nome, cod, cursou, nivel):
        super().__init__(nome, cod)
        self.__cursou = cursou
        self.__nivel = nivel
