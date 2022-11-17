from View.tela_curso import TelaCurso


class ControladorCurso:
    def __init__(self):
        self.__tela_curso = TelaCurso()
        self.__cursos = []

    @property
    def cursos(self):
        return self.__cursos
