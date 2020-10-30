from sum import sum

class TestSum:
    # def test_failing_lists(self):
    #     assert [1] == [1, 2]

    def test_additions_are_additive(self):
        assert sum(0, 1) == 1, "expected two numbers to add up"