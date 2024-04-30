from printsleep import *

def main_menu():
    print(">~{ O JOGO DE TEXTO }~<\n")
    print(") jogar (")
    print(") opções (")
    print(") créditos (")
    print(") sair (")

    print("> Digite o que quer fazer: ")
    menu_choice = input(">>> ").lower()

    if menu_choice == "jogar":
        time.sleep(1)
        print_med("\n> Uma ótima escolha! Agora, por favor, me diga seu nome:")

        name = input(">>> ")

        print(f"\n- Bem-vindo, {name}, a essa aventura!")
        print_med("\nPara as respostas, por favor limite-se às opções simples sugeridas.")
        print_long(f"\n- Agora, {name}, sua jornada pode começar...")

        return name
    
    elif menu_choice == "opções" or menu_choice == "opcões" or menu_choice == "opçoes" or menu_choice == "opcoes": 
        options()

    elif menu_choice == "sair":
        return 0


def options():
    print()
