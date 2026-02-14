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

--------------------------------------------------
The frequency: 145.99 MHz
The lambda is: 2053.5 mm
The elements : 3 
The gain is  : 7 dBi
--------------------------------------------------
Reflector length:     1032.68 mm
Reflector is in:      0 mm

Dipole length:        971.93 mm
Dipole distance:      410.7 mm

Director length:      911.19 mm
Director distance:    821.4 mm

Balun 4-6 thread, diameter 61.6 mm
--------------------------------------------------
Sat Feb 14 16:02:06 2026
--------------------------------------------------

```
---

```sh

--------------------------------------------------
The frequency: 437.88 MHz
The lambda is: 684.6 mm
The elements : 5 
The gain is  : 9 dBi
--------------------------------------------------
Reflector length:     342.92 mm
Reflector is in:      0 mm

Dipole length:        322.74 mm
Dipole distance:      136.9 mm

1. Director length:   302.57 mm
1. Director distance: 273.8 mm

2. Director length:   302.56 mm
2. Director distance: 410.70000000000005 mm

3. Director length:   302.56 mm
3. Director distance: 547.7 mm

Balun 4-6 thread, diameter 20.54 mm
--------------------------------------------------
Sat Feb 14 16:03:07 2026
--------------------------------------------------

```

