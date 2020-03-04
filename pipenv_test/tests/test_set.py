import random
import pytest

class TestSet:

    def test_set_xor(self):
        set1 = {1, 2, 3, 4}
        set2 = {6, 5, 4, 3, 2}
        set3 = {1, 2, 4, 6, 8}

        assert (set1 ^ set2) ^ set3 == {2, 4, 5, 8}

    def test_set_unpack(self):
        set1 = {1, 2, 3}

        assert {*set1, 1, 4, 9, 16} == {1, 2, 3, 4, 9, 16}

    @pytest.mark.parametrize('lst', [[random.randint(0, 3) for _ in range(1000)] for _ in range(20)])
    def test_set_from_list_with_repetitions(self, lst):
        set1 = set(lst)

        assert set1 == {0, 1, 2, 3}

    @pytest.mark.parametrize('i', range(10))
    def test_set_remove(self, i):
        set1 = {0, 1, 2, 4, 8}
        if i not in set1:
            with pytest.raises(KeyError):
                assert set1.remove(i)

    def test_set_no_hash_func(self):
        set1 = {0, 1, 2, 4, 8}
        with pytest.raises(TypeError):
            assert hash(set1)
