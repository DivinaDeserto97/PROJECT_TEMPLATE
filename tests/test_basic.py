from tools.hello import say_hello


def test_say_hello_default():
    assert say_hello() == "Hallo Welt!"


def test_say_hello_name():
    assert say_hello("ChatGPT") == "Hallo ChatGPT!"
