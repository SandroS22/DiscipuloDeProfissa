from View.tela_curso import TelaCurso
from Model.curso import Curso


class ControladorCurso:
    def __init__(self):
        self.__tela_curso = TelaCurso()
        self.__cursos = []

    def menu_curso(self):
        while True:
            escolha = self.__tela_curso.menu_curso()
            if escolha is None or escolha == 0:
                break
            elif escolha == 1:
                self.novo_curso()

    @property
    def cursos(self):
        return self.__cursos

    def novo_curso(self):
        dados_curso = self.__tela_curso.pega_dados()
        if dados_curso is None:
            return
        novo_curso = Curso(dados_curso[1]['it_nome'], dados_curso[1]['it_codigo'])
        for curso in self.__cursos:
            if novo_curso.id_curso == curso.id_curso or novo_curso.nome == curso.nome:
                self.__tela_curso.mostra_mensagem('Esse curso já existe!')
                return
        else:
            self.__cursos.append(novo_curso)

    def listar_cursos(self):
        pass

    def excluir_curso(self):
        pass
