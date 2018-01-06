# Copyright © 2017 Siyuan Tang sytang7@bu.edu
import numpy as np
a = input().strip().split(' ')
b = input().strip().split(' ')
a = [float(x) for x in a]
b = [float(x) for x in b]
if all(item == 0 for item in np.convolve(a,b)):
	print(0)
else :
	for item in np.convolve(a, b):
		print(item, end=" ")