import random
import math
import pytest

class TestInt:

    @pytest.mark.parametrize('num_x', random.sample(range(-5, 6), 4))
    @pytest.mark.parametrize('num_y', random.sample(range(-5, 6), 4))
    def test_int_double_star(self, num_x, num_y):
        if num_x == 0 and num_y < 0:
            with pytest.raises(ZeroDivisionError):
                assert num_x ** num_y
        else:
            assert num_x ** num_y == pow(num_x, num_y)

    @pytest.mark.parametrize('num_x', random.sample(range(-20, 20), 10))
    @pytest.mark.parametrize('num_y', random.sample(range(-20, 20), 10))
    def test_int_divmod(self, num_x, num_y):
        if num_y == 0:
            with pytest.raises(ZeroDivisionError):
                assert divmod(num_x, num_y)
        else:
            assert divmod(num_x, num_y) == (num_x//num_y, num_x%num_y)

    @pytest.mark.parametrize('num_x', [random.uniform(-20, 20) for _ in range(10)])
    def test_int_from_float(self, num_x):
        if num_x >= 0:
            assert int(num_x) == math.floor(num_x)
        else:
            assert int(num_x) == math.ceil(num_x)

    def test_int_to_binary(self):
        list_of_x = [(1, "0b1"), (2, "0b10"), (4, "0b100"), (7, "0b111")]
        for num_x in list_of_x:
            assert str(bin(num_x[0])) == num_x[1]

    @pytest.mark.parametrize('num_x', random.sample(range(-20, 20), 10))
    def test_int_from_string(self, num_x):
        str_x = str(num_x)
        assert num_x == int(str_x)
