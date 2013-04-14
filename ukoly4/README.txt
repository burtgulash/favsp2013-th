P-4-1 Duel
==========

Program je skript pro jazyk Python 2.7.

Vstupem je na každém řádku:
* počáteční vzdálenost mezi hráči (N)
* klesající posloupnost pravděpodobností hráče A
* klesající posloupnost pravděpodobností hráče B

Výstupem je hráč A nebo B, který vystřelí první, a pravděpodobnost zásahu z
dané vzdálenosti.

Příklad použití:
----------------

$ python p41.py < seqs.txt

Duel from distance 8 with probabilities:
 d     A     B
 0 1.000 1.000
 1 0.500 0.900
 2 0.300 0.800
 3 0.200 0.700
 4 0.100 0.600
 5 0.050 0.500
 6 0.040 0.400
 7 0.010 0.300
 8 0.009 0.200
Player B shoots first at distance 3 with probability of hitting: 0.7





Princip
-------

Program začíná na vzdálenosti N, kterou v každém kroku sníží o 1. Zlomový bod,
kdy jeden z hráčů vystřelí, je pro oba hráče stejný. Pouze vystřelí ten, kdo se
k němu dostane první.

Hráč A se v každém kroku rozhoduje, zda vystřelit s pravděpodobností p(d), kde
d je vzdálenost v daném kroku. Stejnou pravděpodobnost hráče B popisuje q(d).
Hráče A zajímá, jestli výstřel, který má úspěšnost (užitek) p(d), je lepší než
čekat a nechat se v příštím kroce zastřelit hráčem B s pravděpodobností q(d -
1). Užitek hráče A z čekání je tedy 1 - q(d - 1).

Popsáno nerovnicí se hráč A rozhodne vystřelit pokud:
p(d) >= 1 - q(d - 1)

tj.
p(d) + q(d - 1) >= 1

Jakmile je tato nerovnost splněna pro hráče A, pak střílí. Symetricky pro hráče
B.


Reference
---------

YaleCourses - Backward induction: reputation and duels.
http://www.youtube.com/watch?v=SE7kP7XZuV4
