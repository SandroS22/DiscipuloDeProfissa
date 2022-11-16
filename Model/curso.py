class Curso:
    def __init__(self, nome, id_curso):
        self.__nome = nome
        self.__id_curso = id_curso

    @property
    def nome(self):
        return self.__nome

    @property
    def id_curso(self):
        return self.__id_curso

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @id_curso.setter
    def id_curso(self, id_curso):
        self.__id_curso = id_curso
