import random
import math
import pytest

class TestInt:

    @pytest.mark.parametrize('x', random.sample(range(-5, 6), 4))
    @pytest.mark.parametrize('y', random.sample(range(-5, 6), 4))
    def test_int_double_star(self, x, y):
        if x == 0 and y < 0:
            with pytest.raises(ZeroDivisionError):
                assert x ** y
        else:
            assert x ** y == pow(x, y)

    @pytest.mark.parametrize('x', random.sample(range(-20, 20), 10))
    @pytest.mark.parametrize('y', random.sample(range(-20, 20), 10))
    def test_int_divmod(self, x, y):
        if y == 0:
            with pytest.raises(ZeroDivisionError):
                assert divmod(x, y)
        else:
            assert divmod(x, y) == (x//y, x%y)

    @pytest.mark.parametrize('x', [random.uniform(-20, 20) for _ in range(10)])
    def test_int_from_float(self, x):
        if x >= 0:
            assert int(x) == math.floor(x)
        else:
            assert int(x) == math.ceil(x)

    def test_int_to_binary(self):
        xs = [(1, "0b1"), (2, "0b10"), (4, "0b100"), (7, "0b111")]
        for x in xs:
            assert str(bin(x[0])) == x[1]

    @pytest.mark.parametrize('x', random.sample(range(-20, 20), 10))
    def test_int_from_string(self, x):
        str_x = str(x)
        assert x == int(str_x)
