# 1. feladat (Lakcím)

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


# 3. feladat (Fizetés)

# jovedelem=int(input('Kérem adja meg a havi bruttó jövedelmét.  '))
# print(f'Az ön bruttó éves jövedelme: {12*jovedelem:,} HUF')


# 4. feladat (Euro)



# 10. feladat (Testömegindex)

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