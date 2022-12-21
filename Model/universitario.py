from Model.pessoa import Pessoa


class Universitario(Pessoa):
    def __init__(self, nome, cod, curso):
        super().__init__(nome, cod)
        self.__curso = curso
        self.__mestre = None

    @property
    def curso(self):
        return self.__curso

    @curso.setter
    def curso(self, curso):
        self.__curso = curso

    @property
    def mestre(self):
        return self.__mestre

    @mestre.setter
    def mestre(self, mestre):
        self.__mestre = mestre
