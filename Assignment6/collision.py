#! /usr/bin/env python3
# Copyright 2017 Siyuan Tang sytang7@bu.edu
# Copyright 2017 Jia Pei leojia@bu.edu
# Copyright 2017 Jiali Ge ivydany@bu.edu
import sys
import copy
import fileinput
import numpy as np
from numpy import linalg as LA
import math

class ball(object):
	def __init__(self,name,X,Y,Vx,Vy):
		self.name = name
		self.Position = np.array([float(X),float(Y)])
		self.V = np.array([float(Vx),float(Vy)])

	def isCollision(self,other,endtime):
		if math.isclose(self.V[0],0) and math.isclose(self.V[1],0) and math.isclose(other.V[0],0) and math.isclose(other.V[1],0):
			return -1
		a = float(LA.norm(self.V-other.V)**2)
		b = float((self.V-other.V).dot(self.Position-other.Position)*2)
		c = float(LA.norm(self.Position-other.Position)**2 - 100)
		if (b**2 - 4*a*c) >= 0 and a > 0:
			t1 = (-b-(b**2 - 4*a*c)**0.5)/(2*a)
			t2 = (-b+(b**2 - 4*a*c)**0.5)/(2*a)
			# print(t1)
			# print(t2)
			t1 = round(t1,8)
			t2 = round(t2,8)
			# print(endtime)
			if t1 >= 0 and t1 <= endtime:
				if math.isclose(t1,0) and t2 > 0:
					return t1
				elif math.isclose(t1,0) and t2 < 0:
					return -1
				else:
					return t1
			elif t2 >= 0 and t2 <= endtime:	
				if math.isclose(t2,0) and t1 > 0:
					return t2
				elif math.isclose(t2,0) and t1 < 0:
					return -1
				else:			
					return t2
			else:
				return -1
		else: 
			return -1

	def collision(self,other):
		tempV1 = self.V - (self.V-other.V).dot(self.Position-other.Position)/(LA.norm(self.Position-other.Position)**2)*(self.Position-other.Position)
		tempV2 = other.V - (other.V-self.V).dot(other.Position-self.Position)/(LA.norm(other.Position-self.Position)**2)*(other.Position-self.Position)
		# return tempV1,tempV2
		self.V = tempV1
		other.V = tempV2

	def update(self,time):
		tempP = self.Position + self.V.dot(time)
		self.Position = tempP

	def __str__(self):
		res = ""
		res += "{} {} {} {} {}".format(self.name,self.Position[0],self.Position[1],self.V[0],self.V[1])
		return res


def main():
	TIME = []
	LIST = []

	try:
		sys.argv[1]
		for para in sys.argv[1:]:
			if float(para) > 0:
				TIME.append(float(para))
		TIME.sort()
		if len(TIME) is 0:
			sys.exit()
	except ValueError:
		print("value on the command line is not a number")
		exit(2)
	except IndexError:
		print("no valid values on the command line")
		exit(2)
	except SystemExit:
		exit(2)

	try:
		for line in sys.stdin:
			para = line.strip().split()
			if len(para) > 5:
				sys.exit(1)
			LIST.append(ball(para[0],float(para[1]),float(para[2]),float(para[3]),float(para[4])))

	except ValueError:
		print("Input: invalid numbers")
		exit(1)
	except SystemExit:
		print("Input: too many fields on one line")
		exit(1)
	except IndexError:
		exit(1)

	time = 0
	for uptime in TIME:
		uptime = float(uptime)
		while time < uptime:
			tmptime = []
			tmpb1 = []
			tmpb2 = []
			

			# print(uptime)
			# print(time)
			for b1 in LIST:
				for b2 in LIST[LIST.index(b1)+1:]:
					tmptime.append(b1.isCollision(b2,uptime-time))
					tmpb1.append(b1)
					tmpb2.append(b2)
			if len(tmptime) is 0:
				LIST[0].update(uptime)
				break

			mTime = uptime-time
			for t in tmptime:
				if t is not -1 and mTime > t and t >= 0:
					mTime = t
			time += mTime
			for b in LIST:
				b.update(mTime)

			# print(tmptime)
			# print(mTime)
			# print(time)
			# for b in LIST:
			# 	print(b)
			D = {}
			if time <= uptime:
				for ind,t in enumerate(tmptime):
					if math.isclose(t,mTime):
						ind1,ind2 = LIST.index(tmpb1[ind]),LIST.index(tmpb2[ind])
						LIST[ind1].collision(LIST[ind2])
						# print(LIST[ind1])
						# print(LIST[ind2])
			if math.isclose(uptime,time):
				break				

		time = uptime
		print(uptime)
		for b in LIST:
			print(b)

if __name__ == '__main__':
	main()

