from tools import say_hello


def test_say_hello_default():
    assert say_hello() == "Hallo Welt!"


def test_say_hello_with_name():
    assert say_hello("Projekt") == "Hallo Projekt!"
