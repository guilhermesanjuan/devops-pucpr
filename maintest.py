"""Testes unitários para o módulo main."""

from main import hello, add, is_even, reverse_string


def test_hello():
    """Testa se a função hello retorna a saudação correta."""
    assert hello() == "Hello World!!!!"


def test_add_positive():
    """Testa a soma de dois números positivos."""
    assert add(2, 3) == 5


def test_add_negative():
    """Testa a soma com números negativos."""
    assert add(-1, -4) == -5


def test_is_even_true():
    """Testa se um número par é identificado corretamente."""
    assert is_even(4) is True


def test_is_even_false():
    """Testa se um número ímpar é identificado corretamente."""
    assert is_even(3) is False


def test_reverse_string():
    """Testa se a string é invertida corretamente."""
    assert reverse_string("abc") == "cba"
