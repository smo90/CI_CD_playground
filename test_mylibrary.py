import pytest

from mylibrary import sumValues

@pytest.mark.parametrize(
    "array, sum",
    [
        ([1,2,3], 6),
        ([3,5,6], 14)
    ],
)

def test_sumValues(array, sum):
    assert sumValues(array) == sum
