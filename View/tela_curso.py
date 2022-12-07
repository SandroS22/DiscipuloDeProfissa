import PySimpleGUI as sg


class TelaCurso:
    def __init__(self):
        self.__window = None
        self.__layout = None

    def close(self):
        self.__window.Close()

    def open(self):
        button, values = self.__window.Read()
        if button is not None:
            return self.__layout.index(button), values
        else:
            return ['', values]

    def mostra_mensagem(self, titulo, msg):
        sg.popup(titulo, msg)

    def pega_dados(self):
        layout = [

            [sg.Text('Insira as informações')],
            [sg.Text('Nome', size=5), sg.InputText(key='it_nome')],
            [sg.Text('Código', size=5), sg.InputText(key='it_codigo')],
            [sg.Button('Voltar', key=0)]

                 ]
        self.__window = sg.Window('Dados Curso').Layout(layout)
        op = (self.open())
        self.__tela.close()


t = TelaCurso()
t.pega_dados()
