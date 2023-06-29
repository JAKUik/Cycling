# Zde je návrh metody pro vygenerování všech dostupných cílových polí pro pohyb hráče:
def get_accessible_positions(field, player_pos, steps):
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
            if field.is_accessible(next_x, next_y):
                get_accessible_positions_recursive(next_x, next_y, steps-1)

    get_accessible_positions_recursive(x, y, steps)
    return accessible_positions

# Tato metoda používá rekurzi pro procházení všech dostupných cest a ukládání dostupných cílových polí do
# listu accessible_positions. Vstupní parametry jsou pozice hráče a počet kroků o které se má posunout.
# Výstupem je list dostupných cílových polí.



# Here is the modified code that allows you to specify the folder where the files should be saved and loaded from,
# with comments in simple English:

import pickle
import os

# define the object
my_object = {'key1': 'value1', 'key2': [1, 2, 3], 'key3': {'nested_key': 'nested_value'}}

# specify the folder where the file should be saved
folder = '/tmp'

# create the full path to the file
file_path = os.path.join(folder, 'my_object.pickle')

# save the object to the file
with open(file_path, 'wb') as file:
    pickle.dump(my_object, file)

# load the object from the file
with open(file_path, 'rb') as file:
    loaded_object = pickle.load(file)

# verify that the loaded object is the same as the original
assert my_object == loaded_object

# In this modified version of the code, we added an additional variable folder that specifies the folder where the
# file should be saved and loaded from. We then use the os.path.join function to create the full path to the file
# by joining the folder path with the file name. The rest of the code remains unchanged and works in the same way as before.


Zde
je
příklad
funkce
v
jazyce
Python, která
projde
zadanou
složku
na
disku
a
vytvoří
další
verzi
souboru
podle
zadaného
klíče:

import os


def create_next_version(path, key):
    # získáme seznam souborů ve složce
    files = os.listdir(path)

    # inicializujeme čítač verzí
    version = 0

    # projdeme všechny soubory ve složce
    for file in files:
        # pokud soubor odpovídá klíči
        if file.startswith(key):
            # získáme číslo verze ze jména souboru
            file_version = int(file[len(key):-4])
            # aktualizujeme čítač verzí
            version = max(version, file_version + 1)

    # vytvoříme název nového souboru
    new_file = f"{key}{version:03d}.sav"

    # vytvoříme nový soubor
    with open(os.path.join(path, new_file), 'w') as file:
        pass

    # vrátíme název nového souboru
    return new_file


# Zde je příklad funkce v jazyce Python, která projde zadanou složku na disku a vytvoří další verzi souboru podle
# zadaného klíče:
import os
def create_next_version(path, key):
    # získáme seznam souborů ve složce
    files = os.listdir(path)

    # inicializujeme čítač verzí
    version = 0

    # projdeme všechny soubory ve složce
    for file in files:
        # pokud soubor odpovídá klíči
        if file.startswith(key):
            # získáme číslo verze ze jména souboru
            file_version = int(file[len(key):-4])
            # aktualizujeme čítač verzí
            version = max(version, file_version + 1)

    # vytvoříme název nového souboru
    new_file = f"{key}{version:03d}.sav"

    # vytvoříme nový soubor
    with open(os.path.join(path, new_file), 'w') as file:
        pass

    # vrátíme název nového souboru
    return new_file

# Tato funkce bere jako argumenty cestu ke složce (path) a klíč (key), podle kterého se mají hledat existující soubory.
# Funkce nejprve získá seznam všech souborů ve složce a inicializuje čítač verzí na 0. Poté projde všechny soubory
# ve složce a pokud název souboru odpovídá klíči, získá číslo verze ze jména souboru a aktualizuje čítač verzí.
# Nakonec funkce vytvoří název nového souboru pomocí klíče a aktualizovaného číslo verze, vytvoří nový prázdný soubor
# a vrátí jeho název.
#
# Použitím této funkce můžete např. vytvořit novou verzi souboru save_board_000.sav ve složce /tmp takto:

new_file = create_next_version('/tmp', 'save_board_')
print(new_file)  # save_board_001.sav





