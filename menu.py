import time
from printsleep import *


def main_menu():
    """Starting menu of the game where players can choose to start the game, go to options, credits or quit it.
    """

    # Loop for the main menu so the player can choose something then come back to it.
    while True:
        print("\n◸                    ◹")
        print(">~{ O JOGO DE TEXTO }~<")
        print("◺                    ◿\n")
        print("▷ Jogar")
        print("▷ Opções")
        print("▷ Créditos")
        print("▷ Sair")

        print("\n> Digite o que quer fazer: ")

        # Loop for the choice just so that if the user inputs something invalid the whole menu doesn't pop back up.
        while True:
            menu_choice = input(">>> ").lower()

            if menu_choice == "jogar":      # Gets the player name then exits out of the menu funcion and goes to the main() one.
                time.sleep(1)
                print("\n> Uma ótima escolha! Agora, por favor, me diga seu nome:")

                name = input(">>> ")

                print_fast(f"\n- Bem-vindo, {name}, a essa aventura!")
                print_med("\nPara as respostas, por favor limite-se às opções simples sugeridas.")
                print_long(f"\n- Agora, {name}, sua jornada pode começar...")

                # Exits the function and "name" gets assigned to the variable name in the main file.
                return name
            
            elif menu_choice == "opções" or menu_choice == "opcões" or menu_choice == "opçoes" or menu_choice == "opcoes": 
                options()
                break

            elif menu_choice == "créditos" or menu_choice == "creditos":
                credits()
                break

            elif menu_choice == "sair":         # Finishes the program.
                quit()
            
            else:       # Checks for invalid input and asks for it again.
                print("\n> Entre uma opção válida.\n")


def options():
    """Handles the game settings: time between each message (controled by printsleep.py) or the language.
    """
    print("\n     ▻ Tempo")
    print("     ▻ Linguagem")

    print("\n> O que quer mudar: ")

    # Same as the last loop, exists so the whole menu above doesn't pop up again after an invalid input. 
    while True:
        options_choice = input(">>> ").lower()

        if options_choice == "voltar" or options_choice == "sair":

            # Exits the funcion, then breaks on menu() and goes back to the main menu.
            return

        elif options_choice == "tempo":
            sleep_option()

            # Exits the function, then breaks on menu() and goes back to the main menu.
            return

        elif options_choice == "linguagem":
            print("\n> Opção ainda não disponível.\n")

        else:       # Checks for invalid input and asks for it again.
            print("\n> Entre uma opção válida.\n")


def credits():
    print("\n> PYTHON TEXT ADVENTURE")
    print("Feito por 4wardAerial, ou Lucas para os mais próximos, no decorrer de 2024.")
    print("\n\"Meus agradecimentos ao Python, ao GitHub, minha família e meus amigos que me deram forças para continuar o projeto.\"")
    print("                                                                                         - Luc '4wardAerial' as, 2024")
    print("\nVersão brasileira - Herbet Richers")
    print("\n© 2005 - 2024 Aerial Productions")
    print("Todos os direitos reservados")
   
    time.sleep(8)