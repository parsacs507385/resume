import bank

def test_bank():
    assert bank.value("Hello") == 0
    assert bank.value("Hell") == 20
    assert bank.value("wah") == 100
    assert bank.value("How") == 20
    assert bank.value("ajfhsf") == 100
