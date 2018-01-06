#!/usr/bin/python
# -*- coding: UTF-8 -*-
# Copyright © 2017 Siyuan Tang sytang7@bu.edu


Table = "{:<6} {:<22} {:<22} {:<22}"
print(Table.format('Bytes','Largest Unsigned Int','Minimum Signed Int','Maximum Signed Int'))

for x in range(1,9):
	bit = 8*x
	uint = 2**bit - 1
	imax = 2**(bit - 1) - 1
	imin = imax - uint
	print(Table.format(x, uint, imin, imax))