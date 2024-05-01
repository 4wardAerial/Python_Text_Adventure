import time
import random
from menu import *
from ascii import ascii_money


def death_check(player_name : str, potato_status : bool, death_status : bool, num_deaths : int):
    """Checks if the player can and wants to continue playing after a death; if not, ends the game.

    Parameters:

    player_name = "name", the name the player chose

    potato_status = "potato_in_bag", if the player has or not the potato

    death_status = "is_dead", if the player has died or not

    num_deaths = "deaths", the number of times the player has died
    """
    name = player_name
    potato_in_bag = potato_status
    is_dead = death_status
    deaths = num_deaths


    if is_dead:         # Checks if the player is actually dead as they should be.
        print_med("\n- Parece-me que sua aventura chegou ao fim...")

        if potato_in_bag:       # Checks if they have the potato.
            if deaths == 1:         # And if they have already died before.
                print_med("- Mas vejo que já conseguiu....")
                print_med("- ...ela.")
                print_med("- Pois bem, se você quiser, eu posso te levar de volta ao início. Ela ainda tem um destino para cumprir.")
                print_fast("- O que me diz? Pense bem.")

            else:      # Or if it's their first death. 
                print_fast("- Já sabe:")

            print("\n] sim | não [")
            reset = input(">>> ").lower()

            if reset == "sim":
                # Changes their death status, making them alive.
                is_dead = False

                time.sleep(1)

                if deaths == 0:     # Extra dialogue if it's their first death.
                    print_med("\n- Excelente... realmente excelente...")
                
                print_med(f"- Boa sorte, {name}, vai precisar.")
                print_long("\n> Um clarão te cega e você desmaia, caíndo no que parece ser o infinito.")

                # Exits the function and "is_dead" gets assigned to the variable is_dead in the main function.
                return is_dead

            else:       # Finishes the program.
                time.sleep(1)
                print_med("\n- Que assim seja.\n")
                quit()

        else:       # Checks if the player doesn't have the potato and finishes the program.
            print_med("- Infelizmente você não cumpriu o requisito para continuar a aventura...")
            print_long("- Mas não é nada pessoal, entenda; é a burocracia, a papelada, essas coisas, sabe?")
            print_med(f"\n- Bom, acho que isso é um adeus, {name}.\n")
            quit()


def death_messages(num : int, num_deaths : int, endings_seen : list):
    """Prints out a death message and the total number of endings found.

    Parameters:

    num = the specific ending's id number

    num_deaths = "deaths", the number of times the player has died

    endings_seen = a list made out of the id numbers of the deaths the player has seen
    """
    index = num
    deaths = num_deaths
    total_deaths_seen = len(endings_seen)

    # Updates the amount of times they've died.
    deaths += 1

    messages = ["\n# Sua aventura chega ao fim pelas piranhas famintas... #",
                "\n# Sua aventura chega ao fim pelo peso da magia da consciência... #",
                "\n# Sua aventura chega ao fim pelo ataque de um ser desconhecido... #",
                "\n# Sua aventura chega ao fim por uma batata jogada comicamente rápida na sua cara... #",
                "\n# Sua aventura chega ao fim pela mordida na perna feita por um bicho que mirava a batata... #",
                "\n# Sua aventura chega ao fim pela gula causada pela batata... #",
                "\n# Sua aventura chega ao fim por um goblin que apenas queria comer algumas batatas... #",
                "\n# Sua aventura chega ao fim pelo ataque inesperado do espantalho... #"
                ]
    
    print_med(messages[index])
    print_long(f"Final: {index + 1} de {len(messages)} | Vistos: {total_deaths_seen}")

    # Exits the function and "deaths" gets assigned to the variable deaths in the main function.
    return deaths


def money_get(current_money : int):
    """Prints out an ascii image of a dollar bill, then says how much money the player has.
    """
    money = current_money

    ascii_money()

    print_long("\n{ 1 DINHEIRO ADQUIRIDO }\n")
    print_long(f"> Você agora tem {money} dinheiro!")


def input_error(player_name : str):
    """Randomly picks an error message to print if the user inputs something that they shouldn't.
    """
    name = player_name
    
    errors = ["> Isso não é válido agora,",
              "> Acho que não dá para fazer isso agora,",
              "> Não tem como você fazer isso,",
              "> Não é a hora para isso,",
              "> Outra coisa talvez funcione,",
              "> Não, isso não tá certo,",
              "> Procure outra escolha,",
              "> No momento, essa não é uma escolha boa,",
              "> Tente escolher uma opção plausível,"
              ]

    print_fast(f"{random.choice(errors)} {name}.")
