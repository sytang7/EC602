#!/bin/bash
# copyright Siyuan Tang sytang7@bu.edu


g++ -o fourargs fourargs.cpp
python fourargs.py 1 2 3 4 5 6
python fourargs.py 1 2 3
./fourargs 1 2 3 4 5 6
./fourargs 1 2 3
