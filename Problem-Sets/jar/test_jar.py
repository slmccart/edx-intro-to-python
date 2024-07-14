from jar import Jar
import pytest

def test_default_capacity():
    jar = Jar()
    assert jar.capacity == 12

def test_initialization():
    jar = Jar(10)
    assert jar.capacity == 10
    assert jar.size == 0

    with pytest.raises(ValueError):
        jar = Jar(-2)

def test_initial_str():
    jar = Jar()
    assert jar.__str__() == ""

def test_deposit_valid():
    jar = Jar()
    assert jar.size == 0
    jar.deposit(5)
    assert jar.size == 5

def test_deposit_invalid():
    jar = Jar(10)
    assert jar.size == 0
    jar.deposit(10)
    assert jar.size == 10
    with pytest.raises(ValueError):
        jar.deposit(1)

def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"

def test_withdraw_valid():
    jar = Jar()
    assert jar.size == 0
    jar.deposit(5)
    assert jar.size == 5
    jar.withdraw(2)
    assert jar.size == 3

def test_withdraw_invalid():
    jar = Jar()
    assert jar.size == 0
    jar.deposit(2)
    assert jar.size == 2
    with pytest.raises(ValueError):
        jar.withdraw(3)
