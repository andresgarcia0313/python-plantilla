"""Mostar Textos"""


from colorama import Fore, Style


class TextPrinter:
    """
    Clase para imprimir texto en pantalla con formato utilizando colorama.
    """
    def __init__(self, text) -> None:
        self.text = text

    def print_text(self):
        """
        Imprime el texto en pantalla con formato verde y brillante.
        """
        formatted_text = (
            f"{Fore.GREEN}{Style.BRIGHT}{self.text}{Style.RESET_ALL}"
        )
        print(formatted_text)

    def print_reversed_text(self):
        """
        Imprime el texto en pantalla con formato invertido.
        """
        reversed_text = self.text[::-1]
        formatted_text = (
            f"{Fore.RED}{Style.BRIGHT}{reversed_text}{Style.RESET_ALL}"
        )
        print(formatted_text)


TEXT_TO_PRINT = "¡Hola, este es un texto con formato!"
# Crear una variable de tipo TextPrinter con sus funciones o metodos
obj = TextPrinter(TEXT_TO_PRINT)
# Imprimir el texto en pantalla con formato
obj.print_text()
obj.print_reversed_text()
