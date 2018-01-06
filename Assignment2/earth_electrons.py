#!/usr/bin/env python
# Copyright © 2017 Siyuan Tang sytang7@bu.edu

Mass_Earth = 5.972e24
Mass_Proton = 1.672e-27

Proton = Mass_Earth / Mass_Proton
Estimate_Electron =  Proton * 0.4 / 8e12
Upper_bound = Proton * 0.5 / 8e12
Lower_bound = Proton * 5/14 / 8e12
print(Estimate_Electron)
print(Lower_bound)
print(Upper_bound)