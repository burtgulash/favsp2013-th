P-3-1 Hledání čistých rovnovážných stavů
========================================


Jedná se o skript pro jazyk Python 2.7, který vyřeší dynamickou hru N hráčů
zadanou stromem, kde každý řádek označuje jeden uzel nebo list.  První řádek je
kořenový uzel, ostatní řádky představují vždy název rozhodnutí a jméno hráče,
který se bude v dalším kroku rozhodovat. Pokud se jedná o list, neuvádíme jméno
hráče, ale užitky pro všechny hráče v pořadí, v jakém se vyskytli v textovém
souboru. Jména rozhodnutí a užitky jsou odděleny dvojtečkou. Uzly tromu musí
být odsazeny pouze pomocí mezer.

Př.: Válka pohlaví
------------------

start:zena
 hokej:muz
  opera::0,0
  hokej::1,4
 opera:muz
  opera::3,1
  hokej::0,0


představuje strom:

               start 
                 |
               (zena)
                 |
         -----------------
        |                 |
      hokej             opera 
        |                 |
      (muz)             (muz)
        |                 |
 -----------        ---------------
|           |      |               |
opera     hokej   opera          hokej
|           |      |               |
0,0        1,4    3,1             0,0  


---------------------------------------------------

Výstup programu po příkazu:

$ python p31.py < valka_pohlavi.txt

je vyřešený strom, kde u každého uzlu a listu je nejlepší skóre pro svůj podstrom a SPNE, tedy Nashovo rovnováha vzhledem k podhrám.

 start zena [3, 1]
  opera muz [3, 1]
   opera  [3, 1]
   hokej  [0, 0]
  hokej muz [1, 4]
   opera  [0, 0]
   hokej  [1, 4]
Subgame Perfect Nash Equilibrium: ['start', 'opera', 'opera']
