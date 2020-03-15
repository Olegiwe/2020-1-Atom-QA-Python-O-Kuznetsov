import copy
import pytest

class TestList:

    def test_list_plus_operator(self):
        strs = ["Java", "Python", "C++"]
        nums = [1, 4, 9, 16]
        concated_lists = ["Java", "Python", "C++", 1, 4, 9, 16]

        assert strs + nums == concated_lists

    def test_list_append_itself(self):
        strs = ["Java", "Python", "C++"]
        strs.append(strs)

        assert strs[3] == strs

    @pytest.mark.parametrize('rnd', [0, 1, 49, 50, -1, -49, -50, -120])
    def test_list_index_error(self, rnd):
        nums = list(range(50))
        if -50 <= rnd < 50:
            assert nums[rnd] == rnd or nums[rnd] == 50 + rnd
        else:
            with pytest.raises(IndexError):
                assert nums[rnd]

    def test_list_shallow_copy_constructor(self):
        lst = [1000, ["two", "three", "four"], 5000]
        newlst = list(lst)

        newlst[0] = "thousand"
        newlst[1][2] = "iv"

        assert lst[0] != newlst[0]
        assert lst[1][2] == newlst[1][2]


    def test_list_deepcopy(self):
        lst = [1000, ["two", "three", "four"], 5000]
        newlst = copy.deepcopy(lst)

        newlst[0] = "thousand"
        newlst[1][2] = "iv"

        assert lst[0] != newlst[0]
        assert lst[1][2] != newlst[1][2]
