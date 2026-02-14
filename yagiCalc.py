#!/usr/bin/env python

from sys import argv
from sys import exit
import datetime
import os
from math import log10

#os.system('cls' if os.name == 'nt' else 'clear')

d = datetime.datetime.now()

example = 145.99
nelem = 3

########## For a more accurate calculation, change this ##########
########## For a more accurate calculation, change this ##########
########## For a more accurate calculation, change this ##########

diam = 8 # the elements diameter

##################################################################

def linea():
    print("--------------------------------------------------")

def usage():
    print("Usage:")
    print(f"$> python {argv[0]} {example} {nelem}\n")

if len(argv) < 3:
    print(f"Need Frequency and elements number !!! \n")
    usage()
    exit(1)

if not argv[2].isdigit():
    print("Use integer numbers ie 1 or 2 or 3 !!!\n")
    usage()
    exit(1)


########## Length Correction ##########
def correction(L):
    corr_d = diam / (2 * lambd * 1e3)
    corr_boom = 0.012
    return L * (1 - corr_d - corr_boom)

n = int(argv[2])

if n < 3:
    print("Minimum element number is 3 !!!\n")
    usage()
    n = 3
    print("I set the number of elements to 3")
    #exit()

########## Calculations ########## 

frequency = argv[1]

sol = 299792458.0 # speed of light

f = float(argv[1]) * 1e6

lambd = round(sol / f, 4)

#gain = 2 + 2.5 * (n -1)
gain = round(10 * log10(1.66 * n))
linea()
print(f"The frequency: {frequency} MHz")
print(f"The lambda is: {lambd*1e3:.2f} mm")
print(f"The elements : {n} ")
print(f"The gain is  : {gain} dBi")
linea()

# ----------------------------------------------------
# Reflector calc
refl = correction(0.51 * lambd * 1e3)
print(f"Reflector length:     {refl:.2f} mm")
print("Reflector is in:      0 mm\n")


# Dipole calc
dipole = correction(0.48 * lambd * 1e3)
dipDist = 0.2 * lambd * 1e3
print(f"Dipole length:        {dipole:.2f} mm")
print(f"Dipole distance:      {dipDist:.2f} mm\n")

# Directors calc
if n > 3:
    for i in range(1, n-1):
        director = correction(0.45 * lambd * 1e3)
        # L_dir(n) = L_dir - (0.005 * lambda * n)
        directorN = director - (0.005 * lambd * i)
        directorDist = dipDist + round(0.2 * lambd * 1e3 * i, 1)
        print(f"{i}. Director length:   {directorN:.2f} mm")
        print(f"{i}. Director distance: {directorDist:.2f} mm\n")

else:
    director = correction(0.45 * lambd * 1e3)
    directorDist = dipDist + (0.2 * lambd * 1e3)
    print(f"Director length:      {director:.2f} mm")
    print(f"Director distance:    {directorDist:.2f} mm\n")

balun = 0.03 * lambd * 1e3
print(f"Balun 4-6 thread, diameter {balun:.2f} mm")


linea()
print(d.strftime("%c"))
linea()

########## END ##########
