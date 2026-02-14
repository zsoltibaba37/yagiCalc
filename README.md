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
The frequency       : 437.8 MHz
The lambda is       : 684.77 mm
The elements        : 5 
The gain is         : 9.19 dBi
The element diameter: 12 mm
----------------------------------------
Reflector length:     340.85 mm
Reflector is in:      0 mm

Dipole length:        320.80 mm
Dipole distance:      136.95 mm

1. Director length:   299.75 mm
1. Director distance: 273.91 mm

2. Director length:   298.75 mm
2. Director distance: 410.86 mm

3. Director length:   297.74 mm
3. Director distance: 547.82 mm

----------------------------------------
5 turns RG-58 on ferrite ring - or
Balun 4-6 thread, diameter 20.54 mm
----------------------------------------
Sat Feb 14 19:58:37 2026
----------------------------------------
```
---

```sh
----------------------------------------
       - Yagi Antenna Design -
----------------------------------------
The frequency       : 145.99 MHz
The lambda is       : 2053.51 mm
The elements        : 3 
The gain is         : 6.97 dBi
The element diameter: 12 mm
----------------------------------------
Reflector length:     1022.16 mm
Reflector is in:      0 mm

Dipole length:        962.03 mm
Dipole distance:      410.70 mm

Director length:      901.90 mm
Director distance:    821.41 mm

----------------------------------------
5 turns RG-58 on ferrite ring - or
Balun 4-6 thread, diameter 61.61 mm
----------------------------------------
Sat Feb 14 19:57:28 2026
----------------------------------------
```

