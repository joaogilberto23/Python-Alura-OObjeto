
class Cliente:

    def __init__(self, nome):
        self.__nome = nome

    # Implementando a anotação de propriedade
    # Quando o atributo é chamado, a classe aplica automaticamente o método com anotação de propriedade
    @property
    def nome(self):
        return self.__nome.title()

    # Implamentando a anotação setter
    # O atributo pode ser chamado e atribuído sem a necessidade de se referir a função com os parênteses ()
    @nome.setter
    def nome(self, nome):
        self.__nome = nome
