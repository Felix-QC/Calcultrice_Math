#coding utf-8
#librarys
import math
import time
# Function
cls = lambda: print('\n' * 100)
def main():
    count = 0
    while True:
        count += 1
        if count > 1:
            cls()
        try:
            print("""
#######################################################
##                Made by Felix-QC                   ##
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
            cls()
            print("\nErreur : Vous devez entrer un nombre entier.\n")
            time.sleep(2.45)
            continue
        if user_input == 8:
            cls()
            print("Merci de m'avoir utiliser !")
            break
        if user_input >= 9:
            print("\nErreur : Option non valide\n")
            time.sleep(2.45)
            continue
        ordre_grandeur_input = str(input("\nEntrer l'unite de mesure ex:(mm, cm, m) : \n"))
        try:
            int(ordre_grandeur_input)
            print("\nErreur : Vous devez entrer une unitee de mesure valide.\n")
            time.sleep(2.65)
            continue  
        except:
            pass
        if user_input == 1:
            try:
                base_input = input("\nQuels est la grandeur de sa Base ? : \n")
                base_input = float(base_input)
            except ValueError:
                print("\n\nErreur : Vous devez entrer un nombre.\n")
                time.sleep(2.45)
                continue
            try:
                hauteur_input = input("\nQuels est sa Hauteur ? : \n")
                hauteur_input = float(hauteur_input)
            except ValueError:
                print("\n\nErreur : Vous devez entrer un nombre.\n")
                time.sleep(2.45) 
                continue
            print("\nLa reponse est :", round(((base_input * hauteur_input) / 2), 3), ordre_grandeur_input.lower())
            time.sleep(5.5) 
            continue
        if user_input == 2:
            try:   
                base_input = input("\nQuels est la grandeur de sa Base ? : \n")
                base_input = float(base_input)
            except ValueError:
                print("\n\nErreur : Vous devez entrer un nombre.\n")
                time.sleep(2.45) 
                continue
            try:   
                hauteur_input = input("\nQuels est sa Hauteur ? : \n")
                hauteur_input = float(hauteur_input)            
            except ValueError:
                print("\n\nErreur : Vous devez entrer un nombre.\n")
                time.sleep(2.45) 
                continue
            print("\nLa reponse est :", round((base_input * hauteur_input), 3), ordre_grandeur_input.lower())
            time.sleep(5.5) 
            continue
        if user_input == 3:
            try:
                rayon_input = input("\nQuels est la grandeur du Rayon ? : \n")
                rayon_input = float(rayon_input)
            except ValueError:
                print("\n\nErreur : Vous devez entrer un nombre.\n")
                time.sleep(2.45) 
                continue
            print("\nLa reponse est :", round((math.pi * (rayon_input * rayon_input)), 3), ordre_grandeur_input.lower())
            time.sleep(5.5) 
            continue
        if user_input == 4:
            try:
                arret_input = input("\nQuels est la grandeur d'une arret ? : \n")
                arret_input = float(arret_input)
            except ValueError:
                print("\n\nErreur : Vous devez entrer un nombre.\n")
                time.sleep(2.45) 
                continue
            print("\nLa reponse est :", round(((arret_input * arret_input) * 6), 3), f"{ordre_grandeur_input.lower()}²")
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
                print("\n\nErreur : Vous devez entrer un nombre.\n")
                time.sleep(2.45) 
                continue    
            if arret_input > 2:
                print("\n\nErreur : Option non valide\n")
                time.sleep(3.5) 
                continue
            if arret_input == 1:
                try:
                    base_input = input("\nQuels est la grandeur de la Base (1 face seulement) ? : \n")
                    base_input = float(base_input)
                except ValueError:
                    print("\n\nErreur : Vous devez entrer un nombre.\n")
                    time.sleep(2.45) 
                    continue  
                try:  
                    hauteur_input = input("\nQuels est la Hauteur (1 face seulement) ? : \n")
                    hauteur_input = float(hauteur_input)
                except ValueError:
                    print("\n\nErreur : Vous devez entrer un nombre.\n")
                    time.sleep(2.45) 
                    continue 
                resultat = (base_input * hauteur_input) / 2
                try:
                    hauteur_2_input = input("Quels est la Hauteur de la pyramide ? : \n")
                    hauteur_2_input = float(hauteur_2_input)
                except ValueError:
                    print("\n\nErreur : Vous devez entrer un nombre.\n")
                    time.sleep(2.45) 
                    continue 
                print("\nLa reponse est :", round(((resultat * hauteur_2_input) / 3), 3), f"{ordre_grandeur_input.lower()}³")
                time.sleep(5.5) 
                continue
            else:
                try:
                    rayon_input = input("\nQuels est la grandeur du Rayon de la base ? : \n")
                    rayon_input = float(rayon_input)
                except ValueError:
                    print("\n\nErreur : Vous devez entrer un nombre.\n")
                    time.sleep(2.45) 
                    continue    
                resultat = math.pi * (rayon_input * rayon_input)
                try:
                    hauteur_2_input = input("\nQuels est la Hauteur du cone ? : \n")
                    hauteur_2_input = float(hauteur_2_input)
                except ValueError:
                    print("\n\nErreur : Vous devez entrer un nombre.\n")
                    time.sleep(2.45) 
                    continue 
                print("\nLa reponse est :", round(((resultat * hauteur_2_input) / 3), 3), f"{ordre_grandeur_input.lower()}³")
                time.sleep(5.5) 
                continue
        if user_input == 6:
            try:                       
                rayon_input = input("\nQuels est la grandeur du Rayon d'une base ? : \n")
                rayon_input = float(rayon_input)
            except ValueError:
                print("\n\nErreur : Vous devez entrer un nombre.\n")
                time.sleep(2.45) 
                continue             
            resultat = (rayon_input * rayon_input)
            try:
                hauteur_input = int(input("\nQuels est sa Hauteur ? : \n"))
                hauteur_input = float(hauteur_input)
            except ValueError:
                print("\n\nErreur : Vous devez entrer un nombre.\n")
                time.sleep(2.45) 
                continue
            resultat_hauteur = resultat * hauteur_input
            resultat_last = resultat_hauteur + ((resultat)* 2)
            print("\nLa reponse est :", round((resultat_last * math.pi), 3), f"{ordre_grandeur_input.lower()}³")
            time.sleep(5.5) 
            continue
        if user_input == 7:
            cls()
            print("""
#############################################
##        Type de solide triangulaire      ##
##  1. Prisme Triangulaire                 ##
##  2. Prisme Rectangulaire                ## 
##  3. Prisme Pentagonal                   ## 
#############################################""")
            try:
                prisme_input = int(input("\nQuels est le type de prisme ? (1 a 3): \n"))
            except ValueError:
                print("\n\nErreur : Vous devez entrer un nombre.\n")
                time.sleep(2.45) 
                continue    
            if prisme_input > 3:
                print("\n\nErreur : Option non valide\n")
                time.sleep(3.5)  
                continue
            if prisme_input == 1:
                try:
                    base_input = input("\nQuels est la grandeur de l'air de la Base ? : \n")
                    base_input = float(base_input)
                except ValueError:
                    print("\n\nErreur : Vous devez entrer un nombre.\n")
                    time.sleep(2.45) 
                    continue  
                try:
                    hauteur_input = input("\nQuels est la longeur du Prisme ? : \n")
                    hauteur_input = float(hauteur_input)
                except ValueError:
                    print("\n\nErreur : Vous devez entrer un nombre.\n")
                    time.sleep(2.45) 
                    continue
                print("\nLa reponse est :", round((base_input * hauteur_input), 3), f"{ordre_grandeur_input.lower()}³")
                time.sleep(5.5) 
                continue
            if prisme_input == 2:
                try:
                    base_input = input("\nQuels est la grandeur de l'air de la Base ? : \n")
                    base_input = float(base_input)
                except ValueError:
                    print("\n\nErreur : Vous devez entrer un nombre.\n")
                    time.sleep(2.45) 
                    continue  
                try:
                    hauteur_input = input("\nQuels est la hauteur du Prisme ? : \n")
                    hauteur_input = float(hauteur_input)
                except ValueError:
                    print("\n\nErreur : Vous devez entrer un nombre.\n")
                    time.sleep(2.45) 
                    continue
                print("\nLa reponse est :", round((base_input * hauteur_input), 3), f"{ordre_grandeur_input.lower()}³")
                time.sleep(5.5) 
                continue
            if prisme_input == 3:
                try:
                    apoteme_input = input("\nQuels est la grandeur de l'apoteme ? : \n")
                    apoteme_input = float(apoteme_input)
                except ValueError:
                    print("\n\nErreur : Vous devez entrer un nombre.\n")
                    time.sleep(2.45) 
                    continue  
                try:
                    segment_input = int(input("\nQuels est la grandeur d'un segmant ? : \n"))
                    segment_input = float(segment_input)
                except ValueError:
                    print("\n\nErreur : Vous devez entrer un nombre.\n")
                    time.sleep(2.45) 
                    continue  
                resultat_apoteme = 0.5 * ((5 * segment_input) * apoteme_input)           
                try:
                    hauteur_input = input("\nQuels est la hauteur du Prisme ? : \n")
                    hauteur_input = float(hauteur_input)
                except ValueError:
                    print("\n\nErreur : Vous devez entrer un nombre.\n")
                    time.sleep(2.45) 
                    continue
                print("\nLa reponse est :", round((resultat_apoteme * hauteur_input), 3), f"{ordre_grandeur_input.lower()}³")
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
        - Patch bugs [2020-05-30] - [2020-05-31] - [2020-06-01]
        - Add more options [2020-05-30] - [2020-05-31] - [2020-06-01]
        - Some optimisations [2020-06-01]
    """
###########################################
