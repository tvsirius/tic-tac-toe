import random
import pytest
from board import Board
import time

init3_field = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]


@pytest.fixture(autouse=True)
def footer_function_scope():
    """Сообщает продолжительность теста после каждой функции."""
    start = time.time()
    yield
    stop = time.time()
    delta = stop - start
    print('\ntest duration : {:0.3} seconds'.format(delta))

# @pytest.fixture
# def testdim():
#     return 3
@pytest.fixture
def dim():
    return 3


def test_init(dim):
    init_field = [[0 for i in range(dim)] for j in range(dim)]
    board = Board(dim=dim)

    assert init_field == board.field


@pytest.mark.parametrize('testdim', [3, 4, 5, 6, 7, 11])
class Test1():
    @pytest.mark.xfail
    def test_init_dim(self, testdim):
        # init_field=[[0 for i in range(testdim)] for j in range(testdim)]
        board = Board(dim=testdim)
        assert init3_field == board.field

    def test_copy1(self, testdim):
        init_field = [[random.randint(0, 1) for i in range(testdim)] for j in range(testdim)]
        board = Board(dim=testdim, field=init_field)
        assert init_field == board.field

    def test_copy2(self, testdim):
        init_field = [[random.randint(0, 1) for i in range(testdim)] for j in range(testdim)]
        board = Board(dim=testdim, field=init_field)
        assert init_field == board.field
