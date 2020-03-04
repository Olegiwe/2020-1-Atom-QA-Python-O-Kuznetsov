import random
import pytest


class TestStr:

    def test_str_plus_operator(self):
        str1 = "hello"
        str2 = " "
        str3 = "pytest"

        assert str1 + str2 + str3 == "hello pytest"


    def test_str_isalnum(self):

        assert "hello".isalnum()

        assert "111".isalnum()

        assert "sUpErMiNeCrAfTeR2011".isalnum()

        assert not "LIKE 'SALAR%'".isalnum()

    @pytest.mark.parametrize('ind', random.sample(range(50), 10))
    def test_str_index(slf, ind):
        str1 = str()
        for i in range(25):
            str1 += (str(i) + "_")
        if ind >= 25:
            with pytest.raises(ValueError):
                str1.index(str(ind))

    def test_str_format(self):
        name = "Oleg"
        age = "21"
        str0 = "Oleg is 21 years old."
        str1 = f'{name} is {age} years old.'
        str2 = '{name} is {age} years old.'.format(name="Oleg", age="21")
        str3 = '{} is {} years old.'.format("Oleg", "21")
        assert str0 == str1 and str0 == str2 and str0 == str3

    def test_str_split_to_words(self):
        str1 = "hello pytest"
        assert str1.split(' ') == ['hello', 'pytest']
