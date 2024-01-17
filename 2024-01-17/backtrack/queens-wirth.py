#!/usr/bin/python

# Direkte Umsetzung nach der Pascal-Lösung des 8 Damen Problems
# in Niklas Wirth. Algorithmen und Datenstrukturen. Teubner, 1983

import sys

a = {} # a[j] = True, <=> Zeile j ist frei
b = {} # b[k] = True, <=> k-te / Diagonale ist frei
c = {} # c[k] = True, <=> k-te \ Diagonale ist frei
x = {} # Position der Dame je Spalte

TAB = "  " * 4

class Queens:
    #----------------------------------
    def __init__(self, n, verbose):
        self.n = n
        self.verbose = verbose

        a = {} # a[j] = True, <=> Zeile j ist frei
        b = {} # b[k] = True, <=> k-te / Diagonale ist frei
        c = {} # c[k] = True, <=> k-te \ Diagonale ist frei
        x = {} # Position der Dame je Spalte

        for i in range (1, self.n+1): a[i] = True    #1 8
        for i in range (2, 2*self.n+1): b[i] = True  #2 16
        for i in range (-self.n+1, self.n): c[i] = True   #-7 7

        self.a, self.b, self.c, self.x = a, b, c, x

    #----------------------------------
    def show(self, x, level):
        n = self.n
        x = self.x

        indent = TAB * (level - 1)
        for i in range(1,n+1):
            queen_pos = x.get(i)
            row =''.join([" X" if p == queen_pos else " ." for p in range(1,n+1)])
            nr = queen_pos if queen_pos and self.verbose else ''
            print(f'{indent}{row}{nr:>3}')
        print()

    #----------------------------------
    def try_(self, i):
        j = 0
        q = False
        n = self.n
        a, b, c, x = self.a, self.b, self.c, self.x
        while j < n and not q:
            j += 1
            if a[j] and b[i + j] and c[i - j]:
                x[i] = j
                self.show(x, i)
                a[j] = b[i + j] = c[i - j] = False
                if i < n:
                    q = self.try_(i + 1)
                    if not q:
                        a[j] = b[i + j] = c[i - j] = True
                        del x[i]
                else:
                    q = True
        return q

#----------------------------------
def main():
    args = sys.argv[1:]
    filename = __file__.replace('\\','/').split('/')[-1]
    assert len(args) in (1,2), f"Aufruf: {filename} n (Anzahl Damen). Bei mehr als einem Argument ausführliche Ausgabe"
    n =int(args[0])
    verbose = len(args) > 1
    queens = Queens(n=n, verbose=verbose)
    q = queens.try_(1)
    print ("Gefunden" if q else "Nicht gefunden")


#----------------------------------
if __name__ == '__main__':
    main()
