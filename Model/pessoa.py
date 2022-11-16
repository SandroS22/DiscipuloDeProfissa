from abc import ABC


class Pessoa(ABC):
    def __init__(self, nome, cod):
        self.__nome = nome
        self.__cod = cod

    @property
    def nome(self):
        return self.__nome

    @property
    def cod(self):
        return self.__cod

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @cod.setter
    def cod(self, cod):
        self.__cod = cod
