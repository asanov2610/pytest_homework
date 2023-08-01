import pytest

from utils import arrs


@pytest.fixture
def dicts_fixture():
    return [1, 2, 3]


def test_get(dicts_fixture):
    assert arrs.get(dicts_fixture, 1, "test") == 2
    assert arrs.get([], 0, "test") == "test"


def test_slice(dicts_fixture):
    assert arrs.my_slice(dicts_fixture, 1, 3) == [2, 3]
    assert arrs.my_slice(dicts_fixture, 1) == [2, 3]
    assert arrs.my_slice(dicts_fixture, -2) == [2, 3]
    assert arrs.my_slice(dicts_fixture, 0) == [1, 2, 3]
    assert arrs.my_slice([], 0) == []
    assert arrs.my_slice([], -1) == []
    assert arrs.my_slice([1, 2, 3], -4) == [1, 2, 3]

