import PySimpleGUI as sg


class TelaSistema:
    def __init__(self):
        self.__window = None
        self.__layout = None

    def close(self):
        self.__window.Close()

    def open(self):
        button, values = self.__window.Read()
        return button, values

    def menu(self):
        layout = [

            [sg.Text('Menu', font='Lucida')],
            [sg.Button('Cursos', key=1),
             sg.Button('Profissionais', key=2),
             sg.Button('Universitários', key=3)],
            [sg.Button('Sair', key=0)]

                 ]
        self.__window = sg.Window('Menu Principal').layout(layout)
        op = self.open()
        self.close()
        return op[0]
