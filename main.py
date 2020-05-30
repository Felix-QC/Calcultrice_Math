#librarys
import os
import math

# Function
cls = lambda: print('\n' * 100)
def main():
    count = 0
    while True:
        count += 1
        if count > 1:
            cls()
        print("""
#######################################################
##             Calculateur informatique              ##
##  1. Calculer l'aire d'un triangle                 ##
##  2. Calculer l'aire d'un quadrilatere             ## 
##  3. Calculer l'aire d'un disque                   ##
##  4. Calculer le volume d'un cube                  ##
##  5. Calculer le volume d'un solide triangulaire   ##
##  6. Quitter le programme                          ##
#######################################################""")
        user_input = int(input("\nEntrer le numero associer a l'option : \n"))
        if user_input == 6:
            cls()
            print("Merci de m'avoir utiliser !")
            break
        ordre_grandeur_input = str(input("\nEntrer l'unite de mesure ex:(cm, mm, m) : \n"))
        if user_input == 1:
            base_input = int(input("\nQuels est la grandeur de sa Base ? : \n"))
            hauteur_input = int(input("\nQuels est sa Hauteur ? : \n"))
            print("\nLa reponse est :", (base_input * hauteur_input) / 2, ordre_grandeur_input)
            stop_program = str(input("\nVoulez vous continuez ? (y, n) : \n"))
            if stop_program.startswith("y"):
                continue
            else:
                cls()                
                print("Merci de m'avoir utiliser !")
                break
        if user_input == 2:
            base_input = int(input("\nQuels est la grandeur de sa Base ? : \n"))
            hauteur_input = int(input("\nQuels est sa Hauteur ? : \n"))
            print("\nLa reponse est :", (base_input * hauteur_input), ordre_grandeur_input)
            stop_program = str(input("\nVoulez vous continuez ? (y, n) : \n"))
            if stop_program.startswith("y"):
                continue
            else:
                cls()                
                print("Merci de m'avoir utiliser !")
                break
        if user_input == 3:
            rayon_input = int(input("\nQuels est la grandeur du Rayon ? : \n"))
            float(rayon_input)
            print("\nLa reponse est :", (math.pi * (rayon_input * rayon_input)), ordre_grandeur_input)
            stop_program = str(input("\nVoulez vous continuez ? (y, n) : \n"))
            if stop_program.startswith("y"):
                continue
            else:
                cls()
                print("Merci de m'avoir utiliser !")
                break
        if user_input == 4:
            arret_input = int(input("\nQuels est la grandeur d'une arret ? : \n"))
            print("\nLa reponse est :", ((arret_input * arret_input) * 6), f"{ordre_grandeur_input}²")
            stop_program = str(input("\nVoulez vous continuez ? (y, n) : \n"))
            if stop_program.startswith("y"):
                continue
            else:
                cls()
                print("Merci de m'avoir utiliser !")
                break
        if user_input == 5:
            cls()
            print("""
#############################################
##        Type de solide triangulaire      ##
##  1. Pyramide                            ##
##  2. Cone                                ## 
#############################################""")
            arret_input = int(input("\nQuels est le type de la base ? (1 ou 2): \n"))
            if arret_input == 1:
                base_input = int(input("\nQuels est la grandeur de la Base (1 face seulement) ? : \n"))
                hauteur_input = int(input("\nQuels est la Hauteur (1 face seulement) ? : \n"))
                resultat = (base_input * hauteur_input) / 2
                hauteur_2_input = int(input("Quels est la Hauteur de la pyramide ? : \n"))
                print("\nLa reponse est :", ((resultat * hauteur_2_input) / 3), f"{ordre_grandeur_input}³")
            else:
                rayon_input = int(input("\nQuels est la grandeur du Rayon de la base ? : \n"))
                float(rayon_input)
                resultat = math.pi * (rayon_input * rayon_input)
                hauteur_2_input = int(input("\nQuels est la Hauteur du cone ? : \n"))
                print("\nLa reponse est :", ((resultat * hauteur_2_input) / 3), f"{ordre_grandeur_input}³")
            stop_program = str(input("\nVoulez vous continuez ? (y, n) : \n"))
            if stop_program.startswith("y"):
                continue
            else:
                cls()
                print("Merci de m'avoir utiliser !")
                break

if __name__ == "__main__":
    main()

###########################################
##               Dev Part                ##
###########################################
    """[To do]
        - Patch bugs
        - Some optimisations
        - Add more options
        - Add english langage
    """
###########################################