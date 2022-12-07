from Model.pessoa import Pessoa


class Nivel(Enum):
    Junior = 1
    Pleno = 2
    Senior = 3


class Profissional(Pessoa):
    def __init__(self, nome, cod, cursou, nivel):
        super().__init__(nome, cod)
        self.__cursou = cursou
        self.__nivel = nivel

    @property
    def cursou(self):
        return sel.__cursou

    @property
    def nivel(self):
        return self.__nivel

    @cursou.setter
    def cursou(self, curso):
        self.__cursou = curso

    @nivel.setter
    def nivel(self, nivel: Nivel):
        sel.__nivel = nivel
