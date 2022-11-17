from View.tela_curso import TelaCurso
from Model.curso import Curso


class ControladorCurso:
    def __init__(self):
        self.__tela_curso = TelaCurso()
        self.__cursos = []

    @property
    def cursos(self):
        return self.__cursos

    def novo_curso(self):
        dados_curso = self.__tela_curso.pega_dados()
        novo_curso = Curso(dados_curso['nome'], dados_curso['id_curso'])
        for curso in self.__cursos:
            if novo_curso.id_curso == curso.id_curso or novo_curso.nome == curso.nome:
                self.__tela_curso.mostra_msg('Este curso já existe!')
                break
        else:
            self.__cursos.append(novo_curso)
