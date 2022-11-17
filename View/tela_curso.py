from View.abstract_tela import AbstractTela


class TelaCurso(AbstractTela):
    def pega_dados(self):
        print(10 * '-', 'Insira os dados do curso', 10 * '-')
        nome = input('Nome: ')
        while True:
            try:
                id_curso = int(input('ID do curso: '))
                return {'nome': nome, 'id_curso': id_curso}
            except ValueError:
                print('Valor inválido!')

    def mostra_curso(self, nome, id_curso):
        print(20 * '-')
        print('|', 'Nome: ', nome)
        print('| ', 'ID: ', id_curso)
        print(20 * '-')
