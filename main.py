"""Módulo simples com funções utilitárias."""


def hello():
    """Retorna uma saudação."""
    return "Hello World!!!"


def add(a, b):
    """Retorna a soma de dois números."""
    return a + b


def is_even(n):
    """Retorna True se o número for par."""
    return n % 2 == 0


def reverse_string(s):
    """Retorna a string invertida."""
    return s[::-1]


if __name__ == "__main__":
    print(hello())