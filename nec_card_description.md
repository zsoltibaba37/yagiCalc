## 1. Komment blokkok

```sh
CM --- NEC2 Input File created or edited by xnec2c 3.5 ---
CM  Yagi for 145 MHz
CE --- End Comments ---
```

Mit jelent?
Kártya	Jelentés
CM	Comment (komment sor)
CE	Comment End

👉 Ezeket a NEC figyelmen kívül hagyja, csak dokumentáció.
Pythonban: sima szöveg.

---

## 2. Geometria – huzalok (GW)

Ez a legfontosabb rész.
Formátum:
```sh
GW tag segments x1 y1 z1 x2 y2 z2 radius
```
Példa:
```
GW 1 25 0.0 0.509 0.0  0.0 -0.509 0.0  0.005
```
Jelentése:
Paraméter	Jelentés
1       	Wire ID (tag number)
25	        szegmensek száma
x1,y1,z1	huzal kezdőpont
x2,y2,z2	huzal végpont
0.005	    sugár (m)
Mit látsz itt konkrétan?

---

Ez egy 6 elemes Yagi:
Tag	    Elem
1	    Reflektor
2	    Dipól
3-6	    Direktorek

Mind függőleges huzalok (Y irányban állnak).

---

## 3. GM — geometria tükrözés
```
GM 0 0 0 0 0 -1 0 0 0
```
Ez egy mirror transform.

👉 Jelentése:

* tükrözi a geometriát az XZ síkra
* így a huzal két fele automatikusan szimmetrikus

Gyakran használják dipóloknál.

---

## 4. GE — geometria vége
```
GE 0
```
Jelenti:
👉 "Geometry End"

Innen már nem jöhet GW.

---

## 5. FR — frekvencia sweep
```
FR 0 21 0 0 140 0.5
```
Formátum:
```
FR mode Nstep 0 0 fstart fstep
```
Jelentése:
Paraméter       Érték
21	            frekvencia pontok száma
140             MHz	kezdő freki
0.5 MHz	        lépés

👉 tehát:
140 → 150 MHz sweep

---

## 6. EX — gerjesztés (betáplálás)
```
EX 0 2 13 0 1.0 0
```
Formátum:
```
EX type tag segment 0 voltage phase
```
Jelentése:
Paraméter   	Érték
2	            melyik huzal (dipól)
13	            melyik szegmens
1.0	            1V feszültség

👉 tehát:
Dipól közepén táplálod

---

## 7. LD — vezetőképesség
```
LD 5 0 0 0 3.7e7
```
Ez:

👉 anyag paraméter

3.7e7 S/m = alumínium.

---

## 8. NE — Near Field grid
```
NE 0 20 15 1 -1.4 -1.4 0.05 0.2 0.2
```
Ez:

👉 közel-tér számítási rács
Ritkán kell kezdőknek.

---

## 9. RP — sugárzási diagram
```
RP 0 37 73 1000 0 0 5 5
```
Formátum:
```
RP calc theta_steps phi_steps ...
```
👉 itt:

* 37 theta pont
* 73 phi pont
* 3D pattern

---

## 10. EN — program vége
```
EN
```
Kötelező.

---

