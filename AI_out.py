# Zde je návrh metody pro vygenerování všech dostupných cílových polí pro pohyb hráče:
def get_accessible_positions(player_pos, steps):
    x, y = player_pos
    accessible_positions = []

    def get_accessible_positions_recursive(x, y, steps):
        if steps == 0:
            accessible_positions.append((x, y))
            return

        if x % 2 == 0:
            next_positions = [(x+1, y), (x+1, y-1)]
        else:
            next_positions = [(x+1, y+1), (x+1, y)]

        for next_x, next_y in next_positions:
            if Field.is_accessible(next_x, next_y):
                get_accessible_positions_recursive(next_x, next_y, steps-1)

    get_accessible_positions_recursive(x, y, steps)
    return accessible_positions

# Tato metoda používá rekurzi pro procházení všech dostupných cest a ukládání dostupných cílových polí do
# listu accessible_positions. Vstupní parametry jsou pozice hráče a počet kroků o které se má posunout.
# Výstupem je list dostupných cílových polí.