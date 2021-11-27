#!/bin/python3

import binascii


import matplotlib.pyplot as plt

# filename = "A.mp"
# filename = "./other/ok/french-flag.mp"
# filename = "./other/ok/damier.mp"
filename = "./other/ok/french-palette.mp"
# filename = "./other/ok/german-flag-palette.mp"
# filename = "./bw/nok/broken-dimensions2.mp"
# filename = "./bw/nok/missing-data.mp"


def readfile(filename):
    f = open(filename, "rb")  # bin
    b = f.read()
    output = binascii.hexlify(b)  # hexa
    print(b[8:9])
    return (b)


readfile(filename)


def move_block(filename, b_number):
    b = readfile(filename)
    b = b[9:]
    a = 0
    blockstart = 0
    b_len = int.from_bytes(b[blockstart:blockstart + 4], "big") + 5
    while a != b_number:
        blockstart += b_len
        a += 1
        b_len = int.from_bytes(b[blockstart:blockstart + 4], "big") + 5
        # print(b[blockstart:blockstart + b_len])
    return (b[blockstart:blockstart + b_len])


# move_block(filename, 3)


def dec_to_bin(x):
    return int(bin(x)[2:])


def bin_to_ascii(code):
    code = code.replace("1", " ")
    code = code.replace("0", "X")
    return(code)


#################################


def Q1(filename, id_block):

    b = move_block(filename, id_block)
    data_start = 5
    bloc = dict()
    bloc['largeur'] = int.from_bytes(b[data_start:data_start + 3], "big")
    bloc['hauteur'] = int.from_bytes(b[data_start + 3:data_start + 7], "big")
    bloc['type de pixels'] = int.from_bytes(b[data_start + 7:data_start + 8],
                                            "big")

    return (bloc)


Q1(filename, 0)

#################################


def Q2(filename, bloc):

    data_start = 4
    block_commentaire = move_block(filename, 1)
    bloc['commentaires'] = block_commentaire[data_start:-1]

    print(bloc)
    return(bloc)


# Q2(filename, Q1(filename, 0))

##################################


def Q4_afficher_image(filename, block):
    affichage = " "
    bloc_affichage = move_block(filename, block)
    data_start = 4

    for line in bloc_affichage[data_start:]:
        if len(str(dec_to_bin(line))) != 8:
            for i in range(8 - len(str(dec_to_bin(line))) % 8):
                affichage += "0"

        affichage += str(dec_to_bin(line))
        print(bin_to_ascii(affichage))
        affichage = " "


# Q4_afficher_image(filename, 2)

#################################


def Q4_afficher_image_autre(filename, block, donnees):
    type_de_pixel = donnees['type de pixels']
    largeur = donnees['largeur']
    bloc_affichage = move_block(filename, block)
    data_start = 4
    pixel = []
    image = []
    image_bonne_dimension_temp = []
    image_bonne_dimension = []
    i = 0
    j = 0
    for couleur in bloc_affichage[data_start:]:
        i += 1
        pixel.append(couleur)

        if i == type_de_pixel:
            image.append(pixel)
            pixel = []
            i = 0

    for elem in image:
        j += 1
        image_bonne_dimension_temp.append(elem)

        if j == largeur:
            image_bonne_dimension.append(image_bonne_dimension_temp)
            j = 0
            image_bonne_dimension_temp = []

    return(image_bonne_dimension)


# Q4_afficher_image_autre(filename, 1, Q1(filename, 0))


# plt.imshow(Q4_afficher_image_autre(filename, 1, Q1(filename, 0)), cmap='gray',
#            vmin=0, vmax=255)
# plt.show()


#########################################


def palette(filename, id_block_P, id_block_image, donnees):
    largeur = donnees['largeur']
    data_start = 4
    bloc_palette = move_block(filename, id_block_P)
    bloc_image = move_block(filename, id_block_image)
    palette = []

    couleur = []
    image = []
    image_temp = []
    i = 0
    row = 0
    for elem in bloc_palette[data_start:]:
        couleur.append(elem)
        i += 1
        if i == 3:
            palette.append(couleur)
            couleur = []
            i = 0
    for id_couleur in bloc_image[data_start:]:
        image_temp.append(palette[id_couleur])
        row += 1
        if row == largeur:
            image.append(image_temp)
            image_temp = []
            row = 0

    return (image)


# palette(filename, 1, 2, Q1(filename, 0))

# plt.imshow(palette(filename, 1, 2, Q1(filename, 0)),
#            vmin=0, vmax=255)
# plt.show()
