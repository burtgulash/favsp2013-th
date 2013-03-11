P-1-1 Hledání čistých rovnovážných stavů
========================================


Jedná se o skript pro jazyk Python 2.7.


Vysvětlivky:
------------

++ znamená ostře dominující strategii sloupce nebo řádku.
+  znamená neostře dominující strategii.
-  je dominovaná strategie.

4|5 znamená Nashovu rovnováhu.
4,5 není Nashova rovnováha.

Pozn. podle definice 4.17 Nashovy rovnováhy z knihy James N. Webb - Game Theory 
jsou zde uvažovány neostré rovnováhy.



Spuštění v konzoli:
-------------------

1. Náhodně vygenerovaná matice
    $ python p11.py -r|--ranlom [ŘÁDKŮ] [SLOUPCŮ]

    Příklady:
    $ python p11.py --random 3 3

      výstup:
           -   -   + 
       ++ 9,2 6,3 7|9
        - 4,7 5,2 5,9
        - 2,5 5,2 5,5

    $ python p11.py -r 2 6

      výstup:
           -   ++  -   -   -   - 
        - 5,0 6|9 6,3 4,2 7,1 1,5
        - 9,1 6|8 1,2 9,7 4,1 7,0

2. Vstup vlastní matice
    Zadáme matici v následujícím formátu a vstup ukončíme přes End of File 
    (Ctrl+D pro Unix, Ctrl+Z pro Windows).

    Zadání matice ručně:
    $ python p11.py
      2,5 3,4
      8,9 2,3
      
      výstup:
           ++  - 
        - 2,5 3,4
        - 8|9 2,3
  
  
    Zadání matice ze souboru:
    $ python p11.py < matice.txt

      výstup:
         -   -   - 
      - 0,0 3,8 1,5
      - 7|5 6,0 8,0
      - 6,3 3,7 4,2
      - 4,8 1,7 9,4
      - 1,5 7|5 4,5
