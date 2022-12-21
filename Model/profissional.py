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
        self.__discipulos = []

    @property
    def cursou(self):
        return self.__cursou

    @property
    def nivel(self):
        return self.__nivel

    @property
    def discipulos(self):
        return self.__discipulos

    @cursou.setter
    def cursou(self, curso):
        self.__cursou = curso

    @nivel.setter
    def nivel(self, nivel: Nivel):
        self.__nivel = nivel
