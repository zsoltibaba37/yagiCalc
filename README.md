# yagiCalc

---

A small script that help to calculate a Yagi antenna dimensions.


## Usage

Need a Frequency and the alement number to calculate.

```sh

$> ./yagiCalc.py 145.99 3
```
### Example

```sh
----------------------------------------
       - Yagi Antenna Design -
----------------------------------------
 The frequency is    : 145.99 MHz
 The lambda is       : 2053.51 mm
 The elements nr     : 3 
 The gain is         : 6.97 dBi
 The element diameter: 10 mm
----------------------------------------
 Reflector length    : 1025.30 mm
 Reflector is in     : 0 mm

 Dipole length       : 964.99 mm
 Dipole distance     : 410.70 mm

 Director length     : 904.68 mm
 Director distance   : 821.41 mm
----------------------------------------
 5 turns RG-58 on ferrite ring - or
 Balun 4-6 thread, diameter 61.61 mm
----------------------------------------
      Sun Feb 15 09:26:56 2026
----------------------------------------
```
---

```sh
----------------------------------------
       - Yagi Antenna Design -
----------------------------------------
 The frequency is    : 437.8 MHz
 The lambda is       : 684.77 mm
 The elements nr     : 4 
 The gain is         : 8.22 dBi
 The element diameter: 10 mm
----------------------------------------
 Reflector length    : 341.90 mm
 Reflector is in     : 0 mm

 Dipole length       : 321.79 mm
 Dipole distance     : 136.95 mm

 1. Director length  : 300.17 mm
 1. Director distance: 273.91 mm

 2. Director length  : 298.66 mm
 2. Director distance: 410.86 mm
----------------------------------------
 5 turns RG-58 on ferrite ring - or
 Balun 4-6 thread, diameter 20.54 mm
----------------------------------------
      Sun Feb 15 09:27:55 2026
----------------------------------------
```

