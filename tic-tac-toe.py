"""

tic_tac_toe.py: piškvorky v terminálu
author: Valeriia Miller
email: mille56944@mot.sps-dopravni.cz
discord: idk

"""

def main():
    print("Vítejte ve hře Tic Tac Toe")
    
    # Vytvoření prázdné plochy (seznam 9 mezer)
    herni_plocha = [' ' for _ in range(9)]
    hra_bezi = True

    while hra_bezi:
        # Jednoduchý výpis plochy
        print(herni_plocha[0:3])
        print(herni_plocha[3:6])
        print(herni_plocha[6:9])
        
        # Aby se smyčka nezasekla, zatím ji ukončíme hned
        hra_bezi = False

if __name__ == "__main__":
    main()