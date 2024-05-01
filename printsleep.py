import time

global time_sleep_choosen
time_sleep_choosen = 1

def print_fast(text):
    """Prints and waits a small interval. Used for quick texts.
    """
    print(text)
    time.sleep(1 * time_sleep_choosen)


def print_med(text):
    """Print and waits a slight bigger interval. Used for dialogues.
    """
    print(text)
    time.sleep(2 * time_sleep_choosen)


def print_long(text):
    """Prints and waits a big interval. Used for dramatic pauses.
    """
    print(text)
    time.sleep(4 * time_sleep_choosen)


def sleep_option():
    """Allows user to choose a time multiplier that will increase or decrease how much they wait between each message.
    """
    global time_sleep_choosen

    print("\n         Escolhe quanto tempo esperar entre cada texto:")
    print("         ▹ Devagar     (1.5x)")
    print("         ▹ Padrão      (1x)")
    print("         ▹ Rápido      (0.5x)")
    print("         ▹ Nenhum      (0x)\n")

    # Loop for the choice just so that if the user inputs something invalid the whole menu doesn't pop back up.
    while True:
        speed_choice = input(">>> ").lower()

        if speed_choice == "voltar" or speed_choice == "sair":

            # Exits the function, goes back to options().
            return

        elif speed_choice == "devagar":
            # Attributes value of 1.5 to the time.sleep multiplier that will apply to all text in the game.
            time_sleep_choosen = 1.5

            # Exits the function, goes back to options().
            return
        
        elif speed_choice == "padrão" or speed_choice == "padrao":
            # Attributes the default value of 1 to the multiplier.
            time_sleep_choosen = 1

            # Exits the function, goes back to options().
            return

        elif speed_choice == "rápido" or speed_choice == "rapido":
            # Attributes value of 1.5 to the multiplier.
            time_sleep_choosen = 0.5

            # Exits the function, goes back to options().
            return

        elif speed_choice == "nenhum":
            # Nullifies the multiplier.
            time_sleep_choosen = 0

            # Exits the function, goes back to options().
            return

        else:       # Checks for invalid input and asks for it again.
            print("\n> Entre uma opção válida.\n")
