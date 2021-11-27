

import matplotlib
from parser import Q1, readfile, move_block


def test_number_of_blocks_0():
    filename = "A.mp"

    assert move_block(filename, 2) != b''
    assert move_block(filename, 3) == b''


def test_number_of_blocks_1():
    filename = "./other/ok/damier.mp"

    assert move_block(filename, 1) != b''
    assert move_block(filename, 2) == b''


def test_number_of_blocks_2():
    filename = "./other/ok/french-flag.mp"

    assert move_block(filename, 1) != b''
    assert move_block(filename, 2) == b''


def test_data_file_0():
    filename = "A.mp"
    bloc = Q1(filename, 0)

    assert bloc['largeur'] == 8
    assert bloc['hauteur'] == 10
    assert bloc['type de pixels'] == 0


def test_data_file_1():
    filename = "./other/ok/damier.mp"
    bloc = Q1(filename, 0)

    assert bloc['largeur'] == 64
    assert bloc['hauteur'] == 64
    assert bloc['type de pixels'] == 1


def test_data_file_2():
    filename = "./other/ok/german-flag-palette.mp"
    bloc = Q1(filename, 0)

    assert bloc['largeur'] == 18
    assert bloc['hauteur'] == 15
    assert bloc['type de pixels'] == 2


def test_data_file_3():
    filename = "./other/ok/french-flag.mp"
    bloc = Q1(filename, 0)

    assert bloc['largeur'] == 6
    assert bloc['hauteur'] == 4
    assert bloc['type de pixels'] == 3


def test_magic():
    filename = "./other/ok/french-palette.mp"

    assert readfile(filename)[:9] == b"Mini-PNGH"


def test_missing_magic():
    filename = "./bw/nok/wrong-magic.mp"

    assert readfile(filename)[:9] != b"Mini-PNGH"


def test_correct_header():
    filename = "./bw/nok/missing-header.mp"
    header = readfile(filename)
    assert header[8:9] != "H"
