# Hangman – Oběšenec

Jednoduchá konzolová hra Oběšenec (Hangman) vytvořená v jazyce Python.

## O projektu

Cílem projektu bylo naprogramovat klasickou slovní hru Oběšenec, kterou si uživatel může zahrát přímo v terminálu.

Součástí přípravy bylo seznámení s principy hry podle knihy *Invent with Python* a vytvoření vývojového diagramu znázorňujícího herní logiku a jednotlivé kroky programu.

## Inspirace a zdroje

Při přípravě projektu jsem vycházela z kapitoly [Invent with Python – Chapter 7](https://inventwithpython.com/invent4thed/chapter7.html).

Projekt vznikl v rámci studia programování v kurzu [Konečně Python](https://dokazesprogramovat.cz).

## Vývoj projektu

Tento repozitář obsahuje základní verzi hry. Do budoucna plánuji její další rozšíření a vylepšení.

## Jak se hra hraje

Hangman (Oběšenec) je slovní hra, ve které se hráč snaží uhodnout skryté slovo.

Program náhodně vybere slovo ze souboru `words.txt` a místo jednotlivých písmen zobrazí podtržítka.

Hráč postupně zadává jednotlivá písmena.

- **Správný tip:** Písmeno se odkryje na všech odpovídajících pozicích ve slově.
- **Nesprávný tip:** Postupně se vykresluje oběšenec.
- **Opakované písmeno:** Pokud hráč zadá písmeno, které už hádal, program ho upozorní. Pokus se nezapočítává.
- **Neplatný vstup:** Pokud hráč zadá něco jiného než jedno písmeno, program ho upozorní a pokus se nezapočítává.
- **Přehled chyb:** Program průběžně zobrazuje seznam nesprávně hádaných písmen.
- **Výhra:** Hráč vyhrává, pokud uhodne celé slovo dříve, než je oběšenec dokončen.
- **Prohra:** Hra končí prohrou, pokud je oběšenec dokončen dříve, než hráč uhodne celé slovo. Program následně odhalí hledané slovo.

Na konci hry se zobrazí počet správných a nesprávných tipů. Hráč si také může vybrat, zda chce hrát znovu.

## Jak hru spustit

Hra Hangman je napsaná v Pythonu a spouští se v terminálu.

1. Stáhni si projekt pomocí tlačítka **Code → Download ZIP** na GitHubu.
2. Rozbal stažený ZIP archiv.
3. Otevři terminál ve složce, která obsahuje soubory `main.py`, `hangman_pictures.py` a `words.txt`.
4. Spusť hru příkazem:

   `python main.py`

5. Postupuj podle pokynů zobrazených v terminálu.

### Požadavky

Pro spuštění hry je potřeba mít na počítači nainstalovaný **Python 3**, který je zdarma dostupný na [python.org](https://www.python.org/downloads/).

Hra využívá také soubor `words.txt`, ze kterého načítá slova, a soubor `hangman_pictures.py`, který obsahuje jednotlivé fáze vykreslování oběšence. Oba soubory musí zůstat ve stejné složce jako `main.py`.
