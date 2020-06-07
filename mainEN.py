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
##               Computer calculator                 ##
##  1. Calculate the area of a triangle              ##
##  2. Calculate the area of a quadrilateral         ## 
##  3. Calculate the area of a disc                  ##
##  4. Calculate the volume of a cube                ##
##  5. Calculate the volume of a triangular solid    ##
##  6. Calculate the volume of a cylinder            ##
##  7. Calculate the volume of a prism               ##
#######################################################
##  8. Exit the program                              ##
#######################################################""")
            user_input = int(input("\nEnter the number associated with the option : \n"))
        except ValueError:
            cls()
            print("\nError: You must enter an integer.\n")
            time.sleep(2.45)
            continue
        if user_input == 8:
            cls()
            print("Thank you for using me !")
            break
        if user_input >= 9:
            print("\nError: Invalid option\n")
            time.sleep(2.45)
            continue
        ordre_grandeur_input = str(input("\nEnter the unit of measurement e.g. (mm, cm, m) : \n"))
        try:
            int(ordre_grandeur_input)
            print("\nError: You must enter a valid unit of measure.\n")
            time.sleep(2.65)
            continue  
        except:
            pass
        if user_input == 1:
            try:
                base_input = input("\nWhat is the size of its Base? : \n")
                base_input = float(base_input)
            except ValueError:
                print("\n\nError: You must enter a number.\n")
                time.sleep(2.45)
                continue
            try:
                hauteur_input = input("\nWhat is its height ? : \n")
                hauteur_input = float(hauteur_input)
            except ValueError:
                print("\n\nError: You must enter a number.\n")
                time.sleep(2.45) 
                continue
            print("\nThe answer is :", round(((base_input * hauteur_input) / 2), 3), ordre_grandeur_input.lower())
            time.sleep(5.5) 
            continue
        if user_input == 2:
            try:   
                base_input = input("\nWhat is the size of its Base? : \n")
                base_input = float(base_input)
            except ValueError:
                print("\n\nError: You must enter a number.\n")
                time.sleep(2.45) 
                continue
            try:   
                hauteur_input = input("\nWhat is its height ? : \n")
                hauteur_input = float(hauteur_input)            
            except ValueError:
                print("\n\nError: You must enter a number.\n")
                time.sleep(2.45) 
                continue
            print("\nThe answer is :", round((base_input * hauteur_input), 3), ordre_grandeur_input.lower())
            time.sleep(5.5) 
            continue
        if user_input == 3:
            try:
                rayon_input = input("\nHow big is the Ray ? : \n")
                rayon_input = float(rayon_input)
            except ValueError:
                print("\n\nError: You must enter a number.\n")
                time.sleep(2.45) 
                continue
            print("\nThe answer is :", round((math.pi * (rayon_input * rayon_input)), 3), ordre_grandeur_input.lower())
            time.sleep(5.5) 
            continue
        if user_input == 4:
            try:
                arret_input = input("\nHow big is a stop ? : \n")
                arret_input = float(arret_input)
            except ValueError:
                print("\n\nError: You must enter a number.\n")
                time.sleep(2.45) 
                continue
            print("\nThe answer is :", round(((arret_input * arret_input) * 6), 3), f"{ordre_grandeur_input.lower()}²")
            time.sleep(5.5) 
            continue
        if user_input == 5:
            cls()
            print("""
#############################################
##         Type of triangular solid        ##
##  1. Pyramid                             ##
##  2. Cone                                ## 
#############################################""")
            try:
                arret_input = int(input("\nWhat is the type of the base ? (1 or 2): \n"))
            except ValueError:
                print("\n\nError: You must enter a number.\n")
                time.sleep(2.45) 
                continue    
            if arret_input > 2:
                print("\n\nError: Invalid option\n")
                time.sleep(3.5) 
                continue
            if arret_input == 1:
                try:
                    base_input = input("\nWhat is the size of the Base (1 side only) ? : \n")
                    base_input = float(base_input)
                except ValueError:
                    print("\n\nError: You must enter a number.\n")
                    time.sleep(2.45) 
                    continue  
                try:  
                    hauteur_input = input("\nWhat is the Height (1 side only) ? : \n")
                    hauteur_input = float(hauteur_input)
                except ValueError:
                    print("\n\nError: You must enter a number.\n")
                    time.sleep(2.45) 
                    continue 
                resultat = (base_input * hauteur_input) / 2
                try:
                    hauteur_2_input = input("What is the Height of the pyramid ? : \n")
                    hauteur_2_input = float(hauteur_2_input)
                except ValueError:
                    print("\n\nError: You must enter a number.\n")
                    time.sleep(2.45) 
                    continue 
                print("\nThe answer is :", round(((resultat * hauteur_2_input) / 3), 3), f"{ordre_grandeur_input.lower()}³")
                time.sleep(5.5) 
                continue
            else:
                try:
                    rayon_input = input("\nWhat is the size of the base radius ? : \n")
                    rayon_input = float(rayon_input)
                except ValueError:
                    print("\n\nError: You must enter a number.\n")
                    time.sleep(2.45) 
                    continue    
                resultat = math.pi * (rayon_input * rayon_input)
                try:
                    hauteur_2_input = input("\nWhat is the height of the cone ? : \n")
                    hauteur_2_input = float(hauteur_2_input)
                except ValueError:
                    print("\n\nError: You must enter a number.\n")
                    time.sleep(2.45) 
                    continue 
                print("\nThe answer is :", round(((resultat * hauteur_2_input) / 3), 3), f"{ordre_grandeur_input.lower()}³")
                time.sleep(5.5) 
                continue
        if user_input == 6:
            try:                       
                rayon_input = input("\nWhat is the size of the radius of a base ? : \n")
                rayon_input = float(rayon_input)
            except ValueError:
                print("\n\nError: You must enter a number.\n")
                time.sleep(2.45) 
                continue             
            resultat = (rayon_input * rayon_input)
            try:
                hauteur_input = int(input("\nWhat is its height ? : \n"))
                hauteur_input = float(hauteur_input)
            except ValueError:
                print("\n\nError: You must enter a number.\n")
                time.sleep(2.45) 
                continue
            resultat_hauteur = resultat * hauteur_input
            resultat_last = resultat_hauteur + ((resultat)* 2)
            print("\nThe answer is :", round((resultat_last * math.pi), 3), f"{ordre_grandeur_input.lower()}³")
            time.sleep(5.5) 
            continue
        if user_input == 7:
            cls()
            print("""
#############################################
##        Type of triangular solid         ##
##  1. Triangular prism                    ##
##  2. Rectangular Prism                   ## 
##  3. Pentagonal prism                    ## 
#############################################""")
            try:
                prisme_input = int(input("\nWhat is the type of prism ? (1 to 3): \n"))
            except ValueError:
                print("\n\nError: You must enter a number.\n")
                time.sleep(2.45) 
                continue    
            if prisme_input > 3:
                print("\n\nError: Invalid option\n")
                time.sleep(3.5)  
                continue
            if prisme_input == 1:
                try:
                    base_input = input("\nWhat is the size of the air in the Base ? : \n")
                    base_input = float(base_input)
                except ValueError:
                    print("\n\nError: You must enter a number.\n")
                    time.sleep(2.45) 
                    continue  
                try:
                    hauteur_input = input("\nQuels est la longeur du Prisme ? : \n")
                    hauteur_input = float(hauteur_input)
                except ValueError:
                    print("\n\nError: You must enter a number.\n")
                    time.sleep(2.45) 
                    continue
                print("\nThe answer is :", round((base_input * hauteur_input), 3), f"{ordre_grandeur_input.lower()}³")
                time.sleep(5.5) 
                continue
            if prisme_input == 2:
                try:
                    base_input = input("\nWhat is the size of the air in the Base ? : \n")
                    base_input = float(base_input)
                except ValueError:
                    print("\n\nError: You must enter a number.\n")
                    time.sleep(2.45) 
                    continue  
                try:
                    hauteur_input = input("\nHow tall is the Prism ? : \n")
                    hauteur_input = float(hauteur_input)
                except ValueError:
                    print("\n\nError: You must enter a number.\n")
                    time.sleep(2.45) 
                    continue
                print("\nThe answer is :", round((base_input * hauteur_input), 3), f"{ordre_grandeur_input.lower()}³")
                time.sleep(5.5) 
                continue
            if prisme_input == 3:
                try:
                    apoteme_input = input("\nHow big is the apothem ? : \n")
                    apoteme_input = float(apoteme_input)
                except ValueError:
                    print("\n\nError: You must enter a number.\n")
                    time.sleep(2.45) 
                    continue  
                try:
                    segment_input = int(input("\nWhat is the size of a segment ? : \n"))
                    segment_input = float(segment_input)
                except ValueError:
                    print("\n\nError: You must enter a number.\n")
                    time.sleep(2.45) 
                    continue  
                resultat_apoteme = 0.5 * ((5 * segment_input) * apoteme_input)           
                try:
                    hauteur_input = input("\nHow tall is the Prism ? : \n")
                    hauteur_input = float(hauteur_input)
                except ValueError:
                    print("\n\nError: You must enter a number.\n")
                    time.sleep(2.45) 
                    continue
                print("\nThe answer is :", round((resultat_apoteme * hauteur_input), 3), f"{ordre_grandeur_input.lower()}³")
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
    """
    """[Things did]
        - Patch bugs [2020-05-30] - [2020-05-31] - [2020-06-01]
        - Add more options [2020-05-30] - [2020-05-31] - [2020-06-01]
        - Some optimisations [2020-06-01]
        - Add english langage [2020-06-07]
    """
###########################################
