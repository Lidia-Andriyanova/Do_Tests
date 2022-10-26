import pytest
from utils import to_binary, neg_fib


@pytest.mark.parametrize('decimal_num, binary_num', [(45, 101101),
                                                     (3, 11),
                                                     (129, 10000001),
                                                     (2, 10),
                                                     (17, 10001)])
def test_to_binary(decimal_num, binary_num):
    assert to_binary(decimal_num) == binary_num


@pytest.mark.parametrize('excepted_exception, decimal_num', [(TypeError, '2')])
def test_to_binary_with_error(excepted_exception, decimal_num):
    with pytest.raises(excepted_exception):
        to_binary(decimal_num)


@pytest.mark.parametrize('n, neg_list', [(1, [1]),
                                         (3, [2, -1, 1]),
                                         (5, [5, -3, 2, -1, 1]),
                                         (8, [-21, 13, -8, 5, -3, 2, -1, 1]),
                                         (10, [-55, 34, -21, 13, -8, 5, -3, 2, -1, 1])])
def test_neg_fib(n, neg_list):
    assert neg_fib(n) == neg_list


@pytest.mark.parametrize('excepted_exception, n', [(TypeError, '2')])
def test_neg_fib_with_error(excepted_exception, n):
    with pytest.raises(excepted_exception):
        to_binary(n)
