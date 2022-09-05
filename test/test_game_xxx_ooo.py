import pytest
from game_xxx_ooo import Board

def test_init():
    init_field=[[0 for i in range(3)] for j in range(3)]
    board=Board(dim=3)

    assert init_field==board.field

