from Controller.controlador_curso import ControladorCurso
from View.tela_sistema import TelaSistema


class Sistema:
    def __init__(self):
        self.__controlador_curso = ControladorCurso()
        self.__tela = TelaSistema()

    def menu(self):
        while True:
            opt = self.__tela.menu()
            if opt is None or opt == 0:
                break
            elif opt == 1:
                self.__controlador_curso.menu_curso()

    def iniciar(self):
        self.menu()
