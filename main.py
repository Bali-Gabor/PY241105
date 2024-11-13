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


# 11. feladat (Zoldseges)

# alma=435
# szilva=659
# szolo=819
# print(f'alma:   {alma} ft/kg',f'szilva: {szilva} ft/kg',f'szőlő:  {szolo} ft/kg', sep='\n')
# gyumolcs=input('Milyen gyümölcsöt szeretne vásárolni?  ')
# if gyumolcs == 'alma':
#     mennyiseg=float(input('Hány kg almát szeretne?  '))
#     print(f'alma:   {alma} ft/kg',f'Vásárolt mennyiség: {mennyiseg} kg',f'A fizetendő összeg: {alma*mennyiseg:,} ft', sep='\n')
# if gyumolcs == 'szilva':
#     mennyiseg=float(input('Hány kg szilvát szeretne?  '))
#     print(f'szilva: {szilva} ft/kg',f'Vásárolt mennyiség: {mennyiseg} kg',f'A fizetendő összeg: {szilva*mennyiseg:,} ft',sep='\n')
# if gyumolcs == 'szőlő':
#     mennyiseg=float(input('Hány kg szőlőt szeretne?  '))
#     print(f'szőlő:  {szolo} ft/kg',f'Vásárolt mennyiség: {mennyiseg} kg',f'Fizetendő összeg: {szolo*mennyiseg:,} ft',sep='\n')


# 12. feladat (Hordo)

# hordo=int(input('Hány literes a hordó?  '))
# kancso=int(input('Hány literes a kancsó?  '))
# print(f'A hordóban {hordo // kancso} teli kancsónnyi víz van.', f'A hordóban {hordo - (hordo // kancso) * kancso} liter víz marad.', f'A horó és a kancsó térfogatának hányadosa: {hordo / kancso}', sep='\n')

# 13. feladat (Bankjegy)

# print('Bankautomata', end='\n\n')
# print('Legkisebb címlet: 1000 FT, a maximálisan felvehető összeg: 300 000 Ft', end='\n\n')
# felvetel=int(input('Adja meg, mekkora összeget kíván felvenni!  '))
# print('')
# if felvetel % 1000 == 0:
#     print('A kiadott bankjegyek:', end='\n\n')
#     print(f'{felvetel//10000} * 10 000 = {felvetel//10000*10000}')
#     print(f' {(felvetel-(felvetel//10000*10000))//5000} *  5 000 =   {(felvetel-(felvetel//10000*10000))//5000*5000}')
#     print(f' {(felvetel-(felvetel//10000*10000)-(felvetel-(felvetel//10000*10000))//5000*5000)//1000} *  1 000 =   {(felvetel-(felvetel//10000*10000)-(felvetel-(felvetel//10000*10000))//5000*5000)//1000*1000}')
#     print('--------------------')
#     print(f'Összeg:       {felvetel} Ft')
# else:
#     print('Csak 1000 Ft-tal osztható összeg vehető fel.')


# 14. feladat (Uzemido)

# ido=int(input('Kérem adja meg az eszköz üzemidejét másodpercben.  '))
# print('Üzemidő: ')
# print(f'{ido//86400} nap')
# print(f'{(ido-(ido//86400*86400))//3600} óra')
# print(f'{(ido-(ido//86400*86400)-(ido-(ido//86400*86400))//3600*3600)//60} perc')
# print(f'{ido-(ido//86400*86400)-((ido-(ido//86400*86400))//3600*3600)-((ido-(ido//86400*86400)-(ido-(ido//86400*86400))//3600*3600)//60*60)} másodperc')

# ido=int(input('Kérem adja meg az eszköz üzemidejét másodpercben.  '))
# print(f'Üzemidő: {ido//86400} óra, {(ido-(ido//86400*86400))//3600} óra, {(ido-(ido//3600*3600))//60} perc, {ido-(ido//60*60)} másodperc.')

# ido=int(input('Kérem adja meg az eszköz üzemidejét másodpercben.  '))
# print(f'Üzemidő: {ido//86400} óra, {(ido%86400)//3600} óra, {(ido%3600)//60} perc, {ido%60} másodperc')


# 15. feladat (Utazasiköltség)

# print('Utazási költségtérítés', end='\n\n')
# ut_hossz=float(input('Add meg a megtett utat km-ben!  '))
# fogyasztas=float(input('Add meg az autó fogyasztását 100km-re literben!  '))
# uzemanyag=float(input('Add meg az üzemanyagárat Ft-ban!  '))
# if ut_hossz <=100:
#     print(f'Költségtérítés: {(ut_hossz*fogyasztas*uzemanyag)/100} ft.')
# else:
#     print(f'Költségtérítés: {(ut_hossz*fogyasztas*uzemanyag)/100 + ut_hossz*25}')