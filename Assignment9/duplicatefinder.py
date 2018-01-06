"""
# Copyright 2017 Siyuan Tang sytang7@bu.edu
# Copyright 2017 Pei Jia leojia@bu.edu
"""

from os import listdir
import re
import hashlib
import sys
import numpy as np
from skimage.io import imread


def searchkey(filename):
    "serchkey"
    number = int(re.search(r'[0-9]{1,10}', filename).group(0))
    return number


def searchkeyl(line):
    "searchkeyl"
    number = int(re.search(r'[0-9]{1,10}', line[0]).group(0))
    return number


def process(img1):
    "process image"
    parameter = []
    parameter.append(hashlib.sha256(bytes(img1)).hexdigest())
    img2 = np.rot90(img1)
    parameter.append(hashlib.sha256(bytes(img2)).hexdigest())
    img3 = np.rot90(img2)
    parameter.append(hashlib.sha256(bytes(img3)).hexdigest())
    img4 = np.rot90(img3)
    parameter.append(hashlib.sha256(bytes(img4)).hexdigest())
    img5 = np.fliplr(img)
    resize = np.nonzero(img5)
    img5 = img5[min(resize[0]):max(resize[0])+1,
                min(resize[1]):max(resize[1])+1]
    parameter.append(hashlib.sha256(bytes(img5)).hexdigest())
    img6 = np.rot90(img5)
    parameter.append(hashlib.sha256(bytes(img6)).hexdigest())
    img7 = np.rot90(img6)
    parameter.append(hashlib.sha256(bytes(img7)).hexdigest())
    img8 = np.rot90(img7)
    parameter.append(hashlib.sha256(bytes(img8)).hexdigest())
    return frozenset(parameter)

FOLDERNAME = './'
FILENAMES = listdir(FOLDERNAME)
IMGDICT = {}
for name in FILENAMES:
    if name[len(name) - 3:len(name)] == 'png':
        img = 1-imread(name, as_grey=True)
        data = np.nonzero(img)
        im = img[min(data[0]):max(data[0])+1, min(data[1]):max(data[1])+1]
        imgparameter = process(im)
        if imgparameter in IMGDICT.keys():
            IMGDICT[imgparameter].append(name)
        else:
            IMGDICT[imgparameter] = [name]

RES = []
TMP = list(IMGDICT.values())
for ind, val in enumerate(TMP):
    RES.append(sorted(val, key=searchkey))
RES = sorted(RES, key=searchkeyl)
for ind, val in enumerate(RES):
    RES[ind] = ' '.join(elem for elem in val)
RES = '\n'.join(elem for elem in RES)
RES = RES + '\n'
M = hashlib.sha256()
M.update(RES.encode('utf-8'))
R = M.hexdigest()
print(R)
if sys.argv[1]:
    FILE = open(sys.argv[1], 'w')
    FILE.write(RES)
    FILE.close()
