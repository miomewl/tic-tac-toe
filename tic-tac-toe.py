"""

tic_tac_toe.py: piškvorky v terminálu
author: Valeriia Miller
email: mille56944@mot.sps-dopravni.cz
discord: idk

"""

def main():
    oddelovac = "=" * 40
    
    # 1. Úvodní výpis pravidel hry
    print("Vítejte ve hře Tic Tac Toe")
    print(oddelovac)
    print("PRAVIDLA HRY:")
    print("Každý hráč může umístit jeden symbol (nebo kámen)")
    print("na hrací pole 3x3. VYHRÁVÁ ten, kdo umístí")
    print("tři své symboly do:")
    print("* horizontální,")
    print("* vertikální nebo")
    print("* diagonální řady.")
    print(oddelovac)
    print("Pojďme začít hrát!")

    # Vytvoříme seznam 9 prázdných mezer (indexy 0-8)
    herni_plocha = [' ' for _ in range(9)]
    aktualni_hrac = 'X' # Začíná hráč X
    hra_bezi = True

    # Hlavní smyčka hry - běží, dokud někdo nevyhraje nebo není remíza
    while hra_bezi:
        print(f"\nNa tahu je: {aktualni_hrac}")    
        print("-" * 40)
        
        # Vykreslení aktuálního stavu hrací plochy
        print("+---+---+---+")
        print(f"| {herni_plocha[0]} | {herni_plocha[1]} | {herni_plocha[2]} |")
        print("+---+---+---+")
        print(f"| {herni_plocha[3]} | {herni_plocha[4]} | {herni_plocha[5]} |")
        print("+---+---+---+")
        print(f"| {herni_plocha[6]} | {herni_plocha[7]} | {herni_plocha[8]} |")
        print("+---+---+---+")
        print(oddelovac)

        # Načtení vstupu od uživatele
        vstup = input("Zadej pozici (1-9): ")

        # --- Validace (kontrola) vstupu ---
        
        # 1. Kontrola, zda uživatel zadal číslo
        if not vstup.isdigit():
            print("Chyba: Zadej číslo.")
            continue
        
        cislo = int(vstup)
        
        # 2. Kontrola, zda je číslo v rozsahu 1-9
        if cislo < 1 or cislo > 9:
            print("Chyba: Rozsah 1-9.")
            continue
            
        # Převedeme číslo (1-9) na index seznamu (0-8)
        index = cislo - 1
        
        # 3. Kontrola, zda je pole volné
        if herni_plocha[index] != ' ':
            print("Obsazeno.")
            continue
            
        # Zápis tahu do hrací plochy
        herni_plocha[index] = aktualni_hrac
        
        # --- Vyhodnocení hry ---
        
        # Seznam všech možných výherních kombinací (řádky, sloupce, diagonály)
        vyherni_kombinace = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8], # Řádky
            [0, 3, 6], [1, 4, 7], [2, 5, 8], # Sloupce
            [0, 4, 8], [2, 4, 6]             # Diagonály
        ]
        
        vitezi = False
        # Projdeme kombinace a zjistíme, jestli hráč obsadil celou trojici
        for a, b, c in vyherni_kombinace:
            if herni_plocha[a] == aktualni_hrac and herni_plocha[b] == aktualni_hrac and herni_plocha[c] == aktualni_hrac:
                vitezi = True
                break
        
        if vitezi:
            print(f"Hráč {aktualni_hrac} vyhrál!")
            hra_bezi = False # Ukončíme hru
            
        # Pokud nikdo nevyhrál a už není volné místo -> remíza
        elif ' ' not in herni_plocha:
            print("Remíza!")
            hra_bezi = False
            
        else:
            # Pokud hra nekončí, přepneme hráče na další kolo
            if aktualni_hrac == 'X':
                aktualni_hrac = 'O'
            else:
                aktualni_hrac = 'X'

# Spuštění programu
if __name__ == "__main__":
    main()