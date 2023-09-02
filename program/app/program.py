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
        print(
            f"{Fore.GREEN}{Style.BRIGHT}{self.text}{Style.RESET_ALL}"
        )

    def print_reversed_text(self):
        """
        Imprime el texto en pantalla con formato invertido.
        """
        reversed_text = self.text[::-1]
        print(
            f"{Fore.RED}{Style.BRIGHT}{reversed_text}{Style.RESET_ALL}"
        )


obj = TextPrinter("¡Bienvenido!")
obj.print_text()
obj.print_reversed_text()
