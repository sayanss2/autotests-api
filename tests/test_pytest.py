import pytest


def test_first_try():
    print("Hello World!")


@pytest.fixture
def numbers():
    return [1, 2, 3]

def test_len(numbers):
    assert len(numbers) == 3


@pytest.mark.parametrize("a,b,expected", [
    (2, 2, 4),
    (10, 5, 15),
    (1, -1, 0),
    (2, 2, 5),
])
def test_add_positive_case(a, b, expected):
    print(f"Проверяем: {a} + {b}")
    assert a + b == expected


class TestUserAuthentication:
    def test_login(self):
        assert 1 == 1


class TestCalculator:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.data = [1, 2, 3]

    def test_sum(self):
        assert sum(self.data) == 6

    def test_len(self):
        assert len(self.data) == 3