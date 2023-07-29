# Cycling

Cycling je desková hra na šestiúhelníkovém hracím plánu, která využívá některé principy z silniční cyklistiky.

## O projektu

Projekt byl ukončen a slouží pouze pro ukázku mých dovedností v Pythonu (jedná se prakticky o první mnou zpracovávaný projekt). Aktuálně pracuji na verzi 2, která má rozvinutější herní mechaniky a lepší možnosti pro taktiku a pohyb hráčů. Vychází také z úplně jiné logiky reprezentace uspořádání šestiúhelníhového herního plánu v programu.


### Pravidla hry

- První hráč při vyšší hodnotě na hrací kostce se pohybuje o jedno pole méně.
- Ostatní hráči ve skupině s házejícím hráčem přebírají původní hodnotu házejícího hráče. Skupinou jsou pokud spolu hráči sousedí alespoň jednou stranou hracího pole.
- Skupina se tedy pohybuje rychleji než samostatný hráč.
- Jsou zde dále možnosti úniku, sprintu, brždění ostatních hráčů.

### Hrací plán

Hrací plán je automaticky generován programem a obsahuje zatáčky a různou šířku cesty pro jezdce.

### Ovládání

V tomto projektu jsou naprogramovány všechny varianty pohybů hráčů. Program sám vypočítá všechny možné pole pro pohyb hráče a umožní místo pohybu zadat z klávesnice.

## Použité technologie

- Python 3.11
- Knihovna PyGame (využití pro vykreslování hracího pole)

## Licence

Projekt není záměrně dokončen a tedy není určen k dalšímu šíření.
Autor však nemá výhrady k použití jeho částí či použitých algoritmů.

## Kontakt

Jaroslav Kučera, kucera1968 na gmailu.
