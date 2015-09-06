P-2-1 Hledání smíšených rovnovážných stavů
==========================================

Jedná se o skript pro jazyk Python 2.7.

Program vypíše všechny čisté rovnováhy (pure equilibria) a pokud existuje, tak
i smíšenou (mixed equilibria).

Pro oba hráče je možné zadat maximálně jeden obecný parametr libovolného názvu.
V tomto případě je výstupem smíšená strategie, která závisí na parametrech.


Spuštění v konzoli:
-------------------
    Příklady:
```
        $ cat mat1.txt | python p21.py
        
        9,4 1,3
        3,2 6,6
        
        pure equilibria:
        (p, q) =  (1, 1)
        (p, q) =  (0, 0)
        
        mixed equilibria:
        (p, q) =  (0.2727272727272727, 0.6)
```


```
	$ cat mat2.txt | python p21.py
	
        x,5 2,3
        4,1 8,y
        
        mixed equilibria:
        (p, q) =  ('4 / (x + 2)', '(-3 + y) / (y + 1)')

```
    
```
	$ cat mat3.txt | python p21.py
	
        5,7 a,b
        2,1 0,-1
        
        mixed equilibria:
        (p, q) =  ('-2 / (a + 3)', '-1 / (b + 5)')
```

