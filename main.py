#coding utf-8
#librarys
import math
import time
# Function
cls = lambda: print('\n' * 100)
clr = lambda: print('\n' * 22)
user_input = int
ordre_grandeur_input = str
def main():
    count = 0
    while True:
        count += 1
        if count > 1:
            cls()
        try:
            print("""
#######################################################
##             Calculateur informatique              ##
##  1. Calculer l'aire d'un triangle                 ##
##  2. Calculer l'aire d'un quadrilatere             ## 
##  3. Calculer l'aire d'un disque                   ##
##  4. Calculer le volume d'un cube                  ##
##  5. Calculer le volume d'un solide triangulaire   ##
##  6. Calculer le volume d'un cylindre              ##
##  7. Calculer le volume d'un prisme                ##
#######################################################
##  8. Quitter le programme                          ##
#######################################################""")
            user_input = int(input("\nEntrer le numero associer a l'option : \n"))
        except ValueError:
            clr()
            print("\nErreur : Vous devez entrer un nombre entier.\n")
            time.sleep(2.45)
            continue
        if user_input == 8:
            clr()
            print("Merci de m'avoir utiliser !")
            break
        if user_input >= 9:
            print("\nErreur : Option non valide\n")
            time.sleep(2.45)
            continue
        if user_input == 7: # Will be there later
            print("\nOption pas encore disponible\n")
            time.sleep(5.5) 
            continue
        ordre_grandeur_input = str(input("\nEntrer l'unite de mesure ex:(cm, mm, m) : \n"))
        try:
            int(ordre_grandeur_input)
            print("\nErreur : Vous devez entrer une unitee de mesure valide.\n")
            time.sleep(2.65)
            continue  
        except:
            pass
        if user_input == 1:
            try:
                base_input = int(input("\nQuels est la grandeur de sa Base ? : \n"))
            except ValueError:
                print("\n\nErreur : Vous devez entrer un nombre entier.\n")
                time.sleep(2.45)
                continue
            try:
                hauteur_input = int(input("\nQuels est sa Hauteur ? : \n"))
            except ValueError:
                print("\n\nErreur : Vous devez entrer un nombre entier.\n")
                time.sleep(2.45) 
                continue
            print("\nLa reponse est :", (base_input * hauteur_input) / 2, ordre_grandeur_input.lower())
            time.sleep(5.5) 
            continue
        if user_input == 2:
            try:   
                base_input = int(input("\nQuels est la grandeur de sa Base ? : \n"))
            except ValueError:
                print("\n\nErreur : Vous devez entrer un nombre entier.\n")
                time.sleep(2.45) 
                continue
            try:   
                hauteur_input = int(input("\nQuels est sa Hauteur ? : \n"))
            except ValueError:
                print("\n\nErreur : Vous devez entrer un nombre entier.\n")
                time.sleep(2.45) 
                continue
            print("\nLa reponse est :", (base_input * hauteur_input), ordre_grandeur_input.lower())
            time.sleep(5.5) 
            continue
        if user_input == 3:
            try:
                rayon_input = int(input("\nQuels est la grandeur du Rayon ? : \n"))
            except ValueError:
                print("\n\nErreur : Vous devez entrer un nombre entier.\n")
                time.sleep(2.45) 
                continue
            print("\nLa reponse est :", (math.pi * (rayon_input * rayon_input)), ordre_grandeur_input.lower())
            time.sleep(5.5) 
            continue
        if user_input == 4:
            try:
                arret_input = int(input("\nQuels est la grandeur d'une arret ? : \n"))
            except ValueError:
                print("\n\nErreur : Vous devez entrer un nombre entier.\n")
                time.sleep(2.45) 
                continue
            print("\nLa reponse est :", ((arret_input * arret_input) * 6), f"{ordre_grandeur_input.lower()}²")
            time.sleep(5.5) 
            continue
        if user_input == 5:
            cls()
            print("""
#############################################
##        Type de solide triangulaire      ##
##  1. Pyramide                            ##
##  2. Cone                                ## 
#############################################""")
            try:
                arret_input = int(input("\nQuels est le type de la base ? (1 ou 2): \n"))
            except ValueError:
                print("\n\nErreur : Vous devez entrer un nombre entier.\n")
                time.sleep(2.45) 
                continue    
            if arret_input == 1:
                try:
                    base_input = int(input("\nQuels est la grandeur de la Base (1 face seulement) ? : \n"))
                except ValueError:
                    print("\n\nErreur : Vous devez entrer un nombre entier.\n")
                    time.sleep(2.45) 
                    continue  
                try:  
                    hauteur_input = int(input("\nQuels est la Hauteur (1 face seulement) ? : \n"))
                except ValueError:
                    print("\n\nErreur : Vous devez entrer un nombre entier.\n")
                    time.sleep(2.45) 
                    continue 
                resultat = (base_input * hauteur_input) / 2
                try:
                    hauteur_2_input = int(input("Quels est la Hauteur de la pyramide ? : \n"))
                except ValueError:
                    print("\n\nErreur : Vous devez entrer un nombre entier.\n")
                    time.sleep(2.45) 
                    continue 
                print("\nLa reponse est :", ((resultat * hauteur_2_input) / 3), f"{ordre_grandeur_input.lower()}³")
                time.sleep(5.5) 
                continue
            else:
                try:
                    rayon_input = int(input("\nQuels est la grandeur du Rayon de la base ? : \n"))
                except ValueError:
                    print("\n\nErreur : Vous devez entrer un nombre entier.\n")
                    time.sleep(2.45) 
                    continue    
                resultat = math.pi * (rayon_input * rayon_input)
                try:
                    hauteur_2_input = int(input("\nQuels est la Hauteur du cone ? : \n"))
                except ValueError:
                    print("\n\nErreur : Vous devez entrer un nombre entier.\n")
                    time.sleep(2.45) 
                    continue 
                print("\nLa reponse est :", ((resultat * hauteur_2_input) / 3), f"{ordre_grandeur_input.lower()}³")
                time.sleep(5.5) 
                continue
        if user_input == 6:
            try:                       
                rayon_input = int(input("\nQuels est la grandeur du Rayon d'une base ? : \n"))
            except ValueError:
                print("\n\nErreur : Vous devez entrer un nombre entier.\n")
                time.sleep(2.45) 
                continue             
            resultat = (rayon_input * rayon_input)
            try:
                hauteur_input = int(input("\nQuels est sa Hauteur ? : \n"))
            except ValueError:
                print("\n\nErreur : Vous devez entrer un nombre entier.\n")
                time.sleep(2.45) 
                continue
            resultat_hauteur = resultat * hauteur_input
            resultat_last = resultat_hauteur + ((resultat)* 2)
            print("\nLa reponse est :", (resultat_last * math.pi), f"{ordre_grandeur_input.lower()}³")
            time.sleep(5.5) 
            continue

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
    """[Things did]
        - Patch bugs [2020-05-30]
        - Add more options [2020-05-30]
    """
###########################################