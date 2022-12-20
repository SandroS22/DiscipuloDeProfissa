import PySimpleGUI as sg


class TelaCurso:
    def __init__(self):
        self.__window = None
        self.__layout = None

    def close(self):
        self.__window.Close()

    def open(self):
        button, values = self.__window.Read()
        return button, values

    def mostra_mensagem(self, titulo, msg):
        sg.popup(titulo, msg)

    def pega_dados(self):
        layout = [

            [sg.Text('Insira as informações')],
            [sg.Text('Nome', size=5), sg.InputText(key='it_nome')],
            [sg.Text('Código', size=5), sg.InputText(key='it_codigo')],
            [sg.Button('Voltar', key=0), sg.Button('Confirmar', key=1)]

                 ]
        self.__window = sg.Window('Dados Curso').Layout(layout)
        novos_dados = (self.open())
        self.__window.close()
        return novos_dados

    def menu_curso(self):
        layout = [

            [sg.Text('Menu curso', font=('Times New Roman', 20))],
            [sg.Button('Novo', key=1, font=('Times New Roman', 15)),
             sg.Button('Alterar', key=2, font=('Times New Roman', 15)),
             sg.Button('Excluir', key=3, font=('Times New Roman', 15)),
             sg.Button('Listar', key=4, font=('Times New Roman', 15))],
            [sg.Button('Voltar', key=0, font=('Times New Roman', 10))]

                 ]
        self.__window = sg.Window('Menu').layout(layout)
        escolha = (self.open())
        self.__window.close()
        return escolha[0]

