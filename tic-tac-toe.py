"""

tic_tac_toe.py: piškvorky v terminálu
author: Valeriia Miller
email: mille56944@mot.sps-dopravni.cz
discord: idk

"""

def main():
    oddelovac = "=" * 40
    
    # 1. ÚVOD A PRAVIDLA
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
    
    herni_plocha = [' ' for _ in range(9)]
    aktualni_hrac = 'X'
    hra_bezi = True

    while hra_bezi:
        print(f"\nNa tahu je: {aktualni_hrac}")
        print(f"{herni_plocha[0]} | {herni_plocha[1]} | {herni_plocha[2]}")
        print(f"{herni_plocha[3]} | {herni_plocha[4]} | {herni_plocha[5]}")
        print(f"{herni_plocha[6]} | {herni_plocha[7]} | {herni_plocha[8]}")

        vstup = input("Zadej pozici (1-9): ")

        if not vstup.isdigit():
            print("Chyba: Zadej číslo.")
            continue
        
        cislo = int(vstup)
        if cislo < 1 or cislo > 9:
            print("Chyba: Rozsah 1-9.")
            continue
            
        index = cislo - 1
        if herni_plocha[index] != ' ':
            print("Obsazeno.")
            continue
            
        herni_plocha[index] = aktualni_hrac
        
        # KONTROLA VÝHRY
        vyherni_kombinace = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],
            [0, 3, 6], [1, 4, 7], [2, 5, 8],
            [0, 4, 8], [2, 4, 6]
        ]
        
        vitezi = False
        for a, b, c in vyherni_kombinace:
            if herni_plocha[a] == aktualni_hrac and herni_plocha[b] == aktualni_hrac and herni_plocha[c] == aktualni_hrac:
                vitezi = True
                break
        
        if vitezi:
            print(f"Hráč {aktualni_hrac} vyhrál!")
            hra_bezi = False
        elif ' ' not in herni_plocha:
            print("Remíza!")
            hra_bezi = False
        else:
            if aktualni_hrac == 'X':
                aktualni_hrac = 'O'
            else:
                aktualni_hrac = 'X'

if __name__ == "__main__":
    main()