from abc import ABC


class AbstractTela(ABC):
    def mostra_msg(self, msg):
        print(msg)
