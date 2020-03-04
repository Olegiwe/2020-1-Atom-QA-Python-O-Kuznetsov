import pytest

class TestDict:

    def test_dict_no_multiple_keys(self):
        dict1 = {"One": 1, "One": 2, "One": 3}
        assert dict1 == {"One": 3}

    def test_dict_no_mutable_keys(self):
        dict1 = dict()

        dict1.update({(1, 2): "tuple"})
        assert (1, 2) in dict1
        dict1.update({3: "num"})
        assert 3 in dict1
        dict1.update({"four": "str"})
        assert "four" in dict1
        with pytest.raises(TypeError):
            assert dict1.update({[5]: "list"})
        with pytest.raises(TypeError):
            assert dict1.update({{6, 7}: "set"})

    def test_dict_from_list(self):
        dict1 = dict.fromkeys([1, 2, 3], "v")
        assert len(dict1) == 3
        assert list(dict1.items()) == [(1, "v"), (2, "v"), (3, "v")]

    @pytest.mark.parametrize('i', range(10))
    def test_dict_key_error(self, i):
        dict1 = dict.fromkeys([1, 3, 5, 7, 9], "v")
        if i not in dict1:
            with pytest.raises(KeyError):
                assert dict1[i] == i

    def test_dict_del(self):
        dict1 = dict.fromkeys([1, 2, 3], "v")

        del(dict1[2])
        assert list(dict1.keys()) == [1, 3]
