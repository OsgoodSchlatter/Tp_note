#!/bin/python3
import binascii



from parser import readfile, move_block, Q1, Q2


def test_readfile():
    minipng = readfile('A.mp')

    assert len(minipng) == 53

# def test_Q1():


#     minipng=Q1('A.mp',0)
#     assert minipng[0]['largeur']==8
