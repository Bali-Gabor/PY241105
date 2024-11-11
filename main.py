# 1. feladat (Lakcim)

# iranyitoszam=input('Kérem adja meg az irányítószámot.  ')
# varos=input('Adja meg a település nevét.  ')
# kozterulet_nev=input('Közterület neve?  ')
# kozterulet_jelleg=input('Közterület jellege?  ')
# hazszam=input('Végül adja meg a házszámot.  ')
# print(iranyitoszam, varos, kozterulet_nev, kozterulet_jelleg, hazszam, sep=' ')


# 2. feladat (Nevek)

# vezeteknev1=input('Kérlek adj meg egy vezetéknevet.  ')
# vezeteknev2=input('Most adj meg egy másikat.  ')
# keresztnev1=input('Most adj meg egy keresztnevet.  ')
# keresztnev2=input('Végül adj meg egy másik keresztnevet.  ')
# print(vezeteknev1, keresztnev1, sep=" ")
# print(vezeteknev1, keresztnev2, sep=" ")
# print(vezeteknev2, keresztnev1, sep=" ")
# print(vezeteknev2, keresztnev2, sep=" ")


# 3. feladat (Fizetes)

# jovedelem=int(input('Kérem adja meg a havi bruttó jövedelmét.  '))
# print(f'Az ön bruttó éves jövedelme: {12*jovedelem:,} HUF')


# 4. feladat (Euro)

# arfolyam=float(input('Kérem adja meg az EURO árfolyamát HUF-ban.  '))
# euro=int(input('Most adja meg, hogy mennyi EURO-t szeretne átváltani.  '))
# print(f'Az átváltott EURO {arfolyam*euro:,} HUF.')


# 5. feladat (Teglalap kerulet, terulet)

# a=float(input('Kérem adja meg egy téglalap egyik oldalának hosszát cm-ben.  '))
# b=float(input('Kérem most adj meg a másik oldal hosszát cm-ben.  '))
# print(f'A téglalap kerülete: {(a+b)*2:.3f} cm')
# print(f'A téglalap területe: {a*b:.3f} cm2')


# 6. feladat (Teglalap krulete, terulete)

# import math
# from math import pi
# r=float(input('Kérem adj meg a kör sugarát cm-ben.  '))
# print(f'A kör kerülete: {2*r*pi} cm')
# print(f'A kör területe: {round(r**2*pi, 4)} cm2')


# 7. feladat (Pitagorasz)

# from math import sqrt
# print('Kérem adja meg egy derékszögű háromszög befogóinak hosszát cm-ben.')
# a=float(input('a:  '))
# b=float(input('b:  '))
# print(f'Az átfogó hossz: {sqrt(a**2+b**2):.2f} cm')


# 8. feladat (Atlagsebesseg)

# ido=float(input('Kéerm adja meg a menetidőt percben. '))/60
# ut_hossza=float(input('Most adja meg a megtett távolságot km-ben.  '))
# print(f'Átlagsebesség: {ut_hossza / ido} km/h')


# 9. feladat (Uzemanyag)

# fogyasztas=float(input('Kérem adja meg a gépjármű fogyasztását literben 100km-en.  '))
# ar=float(input('Adja meg az üzemanyag árát forintban.  '))
# ut_hossza=float(input('Adja meg a megtenni kívát út hosszát km-ben.  '))/100
# print(f'Útiköltség: {round(ut_hossza*fogyasztas*ar, 0)} Ft')


# 10. feladat (Testomegindex)

# magassag=int(input('Kérlek add meg a magasságod centiméterben.  '))/100
# testtomeg=float(input('Kérlek add meg a súlyodat kilógrammban.  '))
# tti=testtomeg/magassag**2
# print(f'A testömegindexed: {tti:.2f}')
# if tti<16: print('Testsúlyosztály: súlyos soványság') 
# elif tti<17: print('Testsúlyosztályod: mérsékelt soványság')
# elif tti<18.5: print('Testsúlyosztályod: enyhe soványság')
# elif tti<25: print('Tesesúlyosztályod: normális testsúly')
# elif tti<30: print('Testsúlyosztályod: túlsúlyos')
# elif tti<35: print('Testsúlyosztályod: I. fokú elhízás ')
# elif tti<40: print('Testsúlyosztályod: II. fokú elhízás')
# else: print('Testsúlyosztályod: III. fokú (súlyos) elhízás')






