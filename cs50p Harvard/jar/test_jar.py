from jar import Jar

def test_init():
    jar = Jar()
    assert jar.capacity == 12
    assert jar.size == 0

    jar = Jar(5)
    assert jar.capacity == 5
    assert jar.size == 0

def test_str():
    jar = Jar()
    assert str(jar) == ""

    jar.deposit(1)
    assert str(jar) == "🍪"

    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"

def test_deposit():
    jar = Jar()
    jar.deposit(2)
    assert jar.capacity == 10
    assert jar.size == 2

    jar = Jar(5)
    jar.deposit(1)
    assert jar.capacity == 4
    assert jar.size == 1

def test_withdraw():
    jar = Jar()
    jar.deposit(2)
    jar.withdraw(1)
    assert jar.capacity == 11
    assert jar.size == 1


if __name__ == "__main__":
    test_init()
    test_str()
    test_deposit()
    test_withdraw()
    print("DONE!")
