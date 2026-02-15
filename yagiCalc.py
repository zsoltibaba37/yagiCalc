#!/usr/bin/env python

from sys import argv
from sys import exit
import datetime
import os
from math import log10
from termcolor import cprint

#os.system('cls' if os.name == 'nt' else 'clear')

d = datetime.datetime.now()

example = 145.99
nelem = 3

########## For a more accurate calculation, change this ##########
########## For a more accurate calculation, change this ##########
########## For a more accurate calculation, change this ##########

diam = 10 # the elements diameter

##################################################################
########## Inspections ########## 

def linea():
    print("----------------------------------------")

def usage():
    cprint("Usage:", "blue")
    print(f"$> python {argv[0]} {example} {nelem}\n")

if len(argv) < 3:
    print(f"Need Frequency and elements number !!! \n")
    usage()
    exit(1)

if not argv[2].isdigit():
    print("Use integer numbers ie 1 or 2 or 3 !!!\n")
    usage()
    exit(1)

n = int(argv[2])

if n < 3:
    print("Minimum element number is 3 !!!\n")
    usage()
    n = 3
    cprint("I set the number of elements to 3", "green")
    #exit()

########## Length Correction ##########
def correction(L):
    #corr_d = diam / (2 * lambd * 1e3)
    corr_d = 0.015 * (diam / 10)
    #corr_boom = 0.012
    corr_boom = 0.006
    return L * (1 - corr_d - corr_boom)

##################################################################
########## Calculations ########## 

frequency = argv[1]

sol = 299792458.0 # speed of light

f = float(argv[1]) * 1e6

lambd = sol / f

#gain = 2 + 2.5 * (n -1)
gain = 10 * log10(1.66 * n)
linea()
print("       - Yagi Antenna Design -")
linea()
print(f" The frequency is    : ", end='')
cprint(f"{frequency} MHz", "yellow")
print(f" The lambda is       : {lambd*1e3:.2f} mm")
print(f" The elements nr     : ", end='')
cprint(f"{n} ", "blue")
print(f" The gain is         : ", end='')
cprint(f"{gain:.2f} dBi", "green")
print(f" The element diameter: ", end='')
cprint(f"{diam} mm", "blue")
linea()

# ----------------------------------------------------
# Reflector calc
refl = correction(0.51 * lambd * 1e3)
print(f" Reflector length    : ", end='')
cprint(f"{refl:.2f} mm", "yellow")
print(" Reflector is in     : ", end='')
cprint("0 mm", "white")


# Dipole calc
dipole = correction(0.48 * lambd * 1e3)
dipDist = 0.2 * lambd * 1e3
print()
print(f" Dipole length       : ", end='')
cprint(f"{dipole:.2f} mm", "yellow")
print(f" Dipole distance     : ", end='')
cprint(f"{dipDist:.2f} mm", "yellow")

# Directors calc
if n > 3:
    for i in range(1, n-1):
        print()
        director = correction(0.45 * lambd * 1e3)
        #directorN = director - (0.005 * lambd * i)
        directorN = director * (1 - 0.01*i/(n-2))
        directorDist = dipDist + (0.2 * lambd * 1e3 * i)
        print(f" {i}. Director length  : ", end='')
        cprint(f"{directorN:.2f} mm", "yellow")
        print(f" {i}. Director distance: ", end='')
        cprint(f"{directorDist:.2f} mm", "yellow")
else:
    print()
    director = correction(0.45 * lambd * 1e3)
    directorDist = dipDist + (0.2 * lambd * 1e3)
    print(f" Director length     : ", end='')
    cprint(f"{director:.2f} mm", "yellow")
    print(f" Director distance   : ", end='')
    cprint(f"{directorDist:.2f} mm", "yellow")

# Balun calc
balun = 0.03 * lambd * 1e3
linea()
print(" 5 turns RG-58 on ferrite ring - or")
print(f" Balun 4-6 thread, diameter {balun:.2f} mm")

linea()
print("      ", end='')
cprint(d.strftime("%c"), "green")
linea()
########## END ##########
