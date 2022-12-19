from controlador_curso import ControladorCurso


class Sistema:
    def __init__(self):
        self.__controlador_curso = ControladorCurso()

    def menu(self):
        while True:
