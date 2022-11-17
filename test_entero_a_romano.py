from main import entero_a_romano

def test_entero_a_romano():
    assert entero_a_romano(336) == ['0000', '300', '30', '6']

def test_entero_a_romano2():
    assert entero_a_romano(336) == "CCCXXXVI"