#!/bin/python3

import binascii


def readfile(filename):
    f = open(filename, "rb")  # bin
    b = f.read()
    output = binascii.hexlify(b)  # hexa
    return(b)


readfile("A.mp")


def move_block(filename, b_number):
    b = readfile(filename)
    b = b[9:]
    a = 0
    blockstart = 0
    b_len = int.from_bytes(b[blockstart:blockstart+4], "big") + 5
    while a != b_number:
        blockstart += b_len
        a += 1
        b_len = int.from_bytes(b[blockstart:blockstart+4], "big") + 5
    return(b[blockstart:blockstart+b_len])


# move_block("A.mp", 3)


def Q1(filename, block):
    bloc_H = []

    b = move_block(filename, block)
    data_start = 5
    bloc_h = dict()
    bloc_h['largeur'] = int.from_bytes(b[data_start:data_start+3], "big")
    bloc_h['hauteur'] = int.from_bytes(b[data_start+3:data_start+7], "big")
    bloc_h['type de pixels'] = int.from_bytes(
        b[data_start+7:data_start+8], "big")
    bloc_H.append(bloc_h)
    # print(bloc_H)
    return(bloc_H)


# Q1("A.mp", 0)


def Q2(block):
    bloc_c = dict()
    data_start = 4
    block_commentaire = move_block("A.mp", 1)
    bloc_c['commentaires'] = block_commentaire[data_start:-1]
    block.append(bloc_c)
    print(block)


# Q2(Q1("A.mp", 0))
