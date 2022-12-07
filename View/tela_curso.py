from tela import Tela
import PySimpleGUI as sg


class TelaCurso:
    def __init__(self):
        self.__tela = Tela()

    @property
    def tela(self):
        return self.__tela

    def pega_dados(self):
        layout = [

            [sg.Text('Insira as informações')],
            [sg.Button('Voltar', key=0)]

                 ]
        self.__tela.window = sg.Window('Teste').Layout(layout)
        op = (self.__tela.open())
        self.__tela.close()


t = TelaCurso()
t.pega_dados()
