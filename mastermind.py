from random import randint
import sys

# Différentes couleurs présentes dans notre jeu.
class colors:
    BLUE = '\u001b[34m'
    GREEN = '\u001b[32m'
    RED = '\u001b[31m'
    YELLOW = '\u001b[33m'
    PURPLE = '\u001b[35m'
    CYAN = '\u001b[36m'
    RESET = '\u001b[0m'
    WHITE = '\u001b[37m'
    BLACK = '\u001b[30m'
    PINK = '\u001b[31;1m'

blue_C = colors.BLUE
green_C = colors.GREEN
red_C = colors.RED
yellow_C = colors.YELLOW
purple_C = colors.PURPLE
cyan_C = colors.CYAN
reset_color = colors.RESET
white_C = colors.WHITE
black_C = colors.BLACK
pink_C = colors.PINK

attemps_amount = 20

# L'ordinateur choisit aléatoirement une combinaison (pouvant être composée de 6 couleurs différentes)
# Rouge, bleu, cyan, vert, jaune, magenta.

# Fonction qui permet de créer une ligne aléatoire à partir du nombre de pions
# que le joueur souhaite utiliser.
def choose_random_combination(nb_per_line):
    combination = []
    for i in range(0, nb_per_line):
        random_number = randint(0, 5)
        switcher = {
            0: cyan_C,
            1: blue_C,
            2: red_C,
            3: purple_C,
            4: green_C,
            5: yellow_C
        }
        color = switcher.get(random_number)
        combination.append(color + "⬤")
    return combination

# Fonction qui permet d'afficher la solution à l'écran.
def display_colored_combination(combination):
    print(*combination)
    print(reset_color)

def print_actual_answer(answer_array):
    displayed_user_combination = []
    for i in range(0, len(answer_array)):
        switcher = {
            'C': cyan_C,
            'B': blue_C,
            'R': red_C,
            'P': purple_C,
            'G': green_C,
            'Y': yellow_C
        }
        color = switcher.get(answer_array[i])
        displayed_user_combination.append(color + "⬤")
    # display_colored_combination(displayed_user_combination)
    # print(displayed_user_combination)
    return displayed_user_combination

# Tous les pions qui sont présents dans les deux listes mais pas aux mêmes index.
def first_comparation (list1, list2):
    same_pions = []
    for k in list1:
        if k in list2:
            same_pions.append(k)
    return same_pions

# Retourne les éléments qui sont exactement à la même place dans les deux listes.
def second_comparation(list1, list2):
    same_index = []
    for i in list1:
        for j in list2:
            if (list1.index(i) == list2.index(j)) and (i == j):
                same_index.append(i)
    return same_index

def analyse_ans(answer, final):
    splited_answer = list(answer)
    treated_answer = print_actual_answer(answer)
    if treated_answer == final:
        print("Félicitations ! Vous avez gagné !")

        sys.exit()
    else:
        result_of_first_compare = first_comparation(treated_answer, final)
        result_of_second_compare = second_comparation(treated_answer, final)
        for k in result_of_first_compare:
            if (k in result_of_second_compare):
                print(pink_C + "⬤" + reset_color)
            if (k not in result_of_second_compare):
                print(white_C + "⬤" + reset_color)

def start_playing(pions_amount):
    choosed_combination = choose_random_combination(pions_amount)
    # display_colored_combination(choosed_combination)
    print(reset_color)
    attemps = 0
    print(cyan_C + "⬤ (C) " + red_C + "⬤ (R) " + blue_C + "⬤ (B) " + green_C + "⬤ (G) " + yellow_C + "⬤ (Y) " + purple_C + "⬤ (P)" + reset_color)
    while(attemps < attemps_amount):
        awnser = input("Votre réponse >>> ")
        analyse_ans(awnser, choosed_combination)
        attemps += 1

print("Bonjour ! Bienvenue sur le Mastermind Console !")
choice = int(input("--- Menu Principal ---\n1 - Jouer\n2 - Help\n3 - Quitter\n>>> "))
if(choice == 1):
    pions_amount = int(input("Veuillez entrer un nombre de pions à générer (min : 2 et max : 6) >>> "))
    start_playing(pions_amount)
elif(choice ==2):
    print("Règles du jeu : L'ordinateur va générer pour vous une série de X points (quantité que vous allez indiquer). Votre but sera de trouver quelle est la combinaison générée par l'ordinateur.")
    print("Pour y arriver, vous allez devoir écrire une série de X pions que vous soupçonnez être valide.")
    print("Cette ligne devra s'écrire sous la forme suivante : CCYR")
    print("Ici j'ai annoncé CYAN CYAN YELLOW RED par exemple.")
    print("Il y a 6 couleurs : CYAN (C), BLUE (B), RED (R), GREEN (G), YELLOW (Y) et PURPLE (P). Retenez les bien ! Vous n'avez que 12 tentatives par partie.")
    print("Pour vous aider, l'ordinateur vous donnera 2 indices :")
    print("- Point blanc : Une couleur est bonne mais elle n'est pas à la bonne place.")
    print("- Point rose : Une couleur est bonne et à la bonne place.")
    print("Les points seront indiqués sur la même ligne. Soyez donc attentifs aux indices que vous donne l'ordinateur et sachez les interpréter.")
    print("En revanche, si aucun indice ne vous est donné, c'est que vous avez tout faux et qu'il faut se ressaisir !")
    print("Bon courage ! Pour jouer, vous n'avez qu'à marquer : \"lu\" dans le champ ci-dessous.")
    read = input(">>> ")
    if(read == "lu"):
        pions_amount = int(input("Veuillez entrer un nombre de pions à générer (min : 2 et max : 6) >>> "))
        start_playing(pions_amount)
    else:
        print("Vous n'avez pas marqué lu !")
        read = input(">>> ")
    


