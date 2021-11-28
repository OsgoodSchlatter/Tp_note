

import matplotlib
from parser import Q1, readfile, move_block, dec_to_bin, Q2, Q4_afficher_image, Q4_afficher_image_autre, palette


valid_files = ["A.mp", "E.mp", "./other/ok/damier.mp",
               "./other/ok/french-flag.mp"]
invalid_files = ["./bw/nok/broken-dimensions2.mp",
                 "./bw/nok/missing-data.mp", "./bw/nok/wrong-magic.mp"]


def test_number_of_blocks_0():
    filename = "A.mp"
    block2, _ = move_block(filename, 2)
    block3, _ = move_block(filename, 3)

    assert block2 != b''
    assert block3 == b''


def test_number_of_blocks_1():
    filename = "./other/ok/damier.mp"
    block1, _ = move_block(filename, 1)
    block2, _ = move_block(filename, 2)

    assert block1 != b''
    assert block2 == b''


def test_number_of_blocks_2():
    filename = "./other/ok/french-flag.mp"
    block1, _ = move_block(filename, 1)
    block2, _ = move_block(filename, 2)

    assert block1 != b''
    assert block2 == b''


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

    assert readfile(filename)[:8] == b"Mini-PNG"


def test_missing_magic():
    filename = "./bw/nok/wrong-magic.mp"

    assert readfile(filename)[:8] != b"Mini-PNG"


def test_incorrect_header():
    filename = "./bw/nok/missing-header.mp"
    header = readfile(filename)
    assert header[8:9] != b"H"


def test_correct_header():
    filename = "A.mp"
    header = readfile(filename)
    assert header[8:9] == b"H"


def test_correct_data():
    filename = "A.mp"
    block_data, _ = move_block(filename, 1)
    print(block_data)
    assert block_data[len(block_data)-1:len(block_data)] == b"D"


def test_correct_data():
    filename = "A.mp"
    block_data, _ = move_block(filename, 1)
    print(block_data)
    assert block_data[len(block_data)-1:len(block_data)] == b"D"


def test_incorrect_data():
    filename = "./bw/nok/missing-data.mp"
    block_data, _ = move_block(filename, 1)
    print(block_data)
    assert block_data[len(block_data)-1:len(block_data)] != b"D"


def test_dec_to_bin():
    assert 1010 == dec_to_bin(10)


def test_Q2():
    filename = "A.mp"
    bloc = Q2(filename, Q1(filename, 0))

    assert(bloc['commentaires'] == b"La lettre A")


def test_Q4():
    filename = "A.mp"
    affichage = Q4_afficher_image(filename, 2)

    assert affichage == " 01111110"


def test_Q4_autre():
    filename = "./other/ok/damier.mp"
    affichage = Q4_afficher_image_autre(filename, 1, Q1(filename, 0))
    assert len(affichage[1]) == Q1(filename, 0)['largeur']


def test_palette():
    filename = "./other/ok/damier.mp"
    affichage = palette(filename, 1, 2, Q1(filename, 0))
    assert len(affichage[0]) == 18
