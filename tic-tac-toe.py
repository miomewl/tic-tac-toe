"""

tic_tac_toe.py: piškvorky v terminálu
author: Valeriia Miller
email: mille56944@mot.sps-dopravni.cz
discord: idk

"""

def main():
    print("Vítejte ve hře Tic Tac Toe")
    herni_plocha = [' ' for _ in range(9)]
    hra_bezi = True

    while hra_bezi:
        # Výpis plochy
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
            
        herni_plocha[index] = 'X'
        
        # Provizorní ukončení po jednom tahu pro test
        # hra_bezi = False 

if __name__ == "__main__":
    main()