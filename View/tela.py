import PySimpleGUI as sg


class Tela:
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
