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

    @pytest.mark.parametrize('ind', [0, 1, 25, 26, 100])
    def test_str_index(self, ind):
        str1 = str()
        for i in range(25):
            str1 += (str(i) + "_")
        if ind >= 25:
            with pytest.raises(ValueError):
                str1.index(str(ind))

    @pytest.mark.parametrize('line', [
        '{name} is {age} years old.'.format(name="Oleg", age="21"),
        '{} is {} years old.'.format("Oleg", "21"),
        '%s is %s years old.' % ("Oleg", "21"),
        '{0} is {1} years old.'.format("Oleg", "21")
    ])
    def test_str_format(self, line):
        str0 = "Oleg is 21 years old."

        assert str0 == line

    def test_str_split_to_words(self):
        str1 = "hello pytest"
        assert str1.split(' ') == ['hello', 'pytest']
