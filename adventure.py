import time
import random
from menu import main_menu
from ascii import ascii_boat, ascii_candle, ascii_rope, ascii_potato 
from printsleep import print_fast, print_long, print_med
from events import death_check, death_messages, money_get, input_error

deaths = 0
is_dead = False
deaths_seen = []

bag = ["batata"]
money = 0
potato_in_bag = True

shop = ""
store = ["Barco? ", "Corda? ", "Vela? "]
shop_visits = 0
shop_visits_potato = False

house_visits = 0
house_visits_potato = False

farm_potatoes = random.randint(100, 200)
farm_guesses = 0
farm_seen = False
scarecrow_visits = False
scarecrow_visits_potato = 0
farm_visits = 0


def path_2_shop():
    """Takes care of the shop.
    """
    global deaths
    global is_dead
    global deaths_seen

    global bag
    global potato_in_bag
    global money
    global shop
    global store
    global shop_visits
    global shop_visits_potato



    if potato_in_bag and not shop_visits_potato:        # Triggers when it's the first time visiting the shop with the potato in bag 
        print_med("\n> Você entra na loja e o vendedor começa a fungar, como se estivesse cheirando algo.")
        print_long("- Isso é... Tem que ser... Não tem como confundir! Você conseguiu uma batata daquele espantalho! Elas são tão...")
        print_long("- ...preciosas.")
        print_long("- Hm esse cheiro de batata me deixou com fome... Eu não vou conseguir trabalhar com o desejo da batata...")
        print_long("- Ei, o que acha de você me vender essa batata? Vamos lá, eu te vendi o barco, lembra? Eu pago bem por ela, é sério! E aí?")

        print("\n] sim | não [")
        potato_bargain = input(">>> ").lower()

        if potato_bargain == "sim":         # Updates shop_visits_potato so not to trigger the scene again
            shop_visits_potato = True

            time.sleep(1)
            print_long("\n> Você está prestes a colocar a batata no balcão mas não encontra forças para isso. E como se a batata não quisesse se separar de você...")
            print_med("> Você desiste e guarda a batata na mochila.")
            print_long("> O vendedor te olha furioso.")
            print_med("> E se joga em cima de você.")

            # Ending 5
            is_dead = True
            if 5 not in deaths_seen:
                deaths_seen.append(5)
            deaths = death_messages(5, deaths, deaths_seen)

            # Exits the funcion dead, goes to the death check.
            return

        elif potato_bargain == "não" or "nao":      # Updates shop_visits_potato so not to trigger the scene again and gives 1 money
            shop_visits_potato = True
            money += 1

            time.sleep(1)
            print_med("\n- Bom a batata é sua, então você decide. Mas saiba que perdeu uma oferta milionária!")
            print_med("- O problema é que agora é que fiquei com fome e nem é horário de almoço ainda...")
            print_med("- Que tal assim: eu te dou um dinheiro como compensação por não te atender agora, você sai daqui e eu faço meu lanchinho!")
            print_med("- Sim, eu sei que eu sou generoso.\n")

            money_get(money)

            print_med("\n> Você sai da loja para o vendedor comer e confuso quanto ao poder da batata")


            # Exits the function.
            return
    
    if store[0] == "" and store[1] == "" and store[2] == "":        # When player buys all of the itens
        print_med("\n- Bom me desculpe, mas você já comprou tudo que eu tinha! Volte aqui quando eu tiver novos produtos.")

    elif shop_visits == 0:      # When player visits the shop for the first time, updates shop_visits so not to trigger the scene again
        shop_visits += 1

        print_med("\n- Ora vejam só um freguês novo! Faz um bom tempo que não recebo dinheiro vindo de outras bandas!")
        print_med(f"- {store[0]}{store[1]}{store[2]} É tudo seu, isso se você tiver o dinheiro suficiente!")
        print_fast("- Então, o que vai ser? ")

        print("\n] barco | vela | corda | sair [")
        shop = input(">>> ").lower()

    else:
        if shop_visits_potato:      # If the player enters the shop with the potato (after having that first special scene)
            time.sleep(1)
            print("\n- Olha só é o cara batata! Já sabe:")

        else:       # If the player enters the shop again but without the potato
            time.sleep(1)
            print("\n- Você de novo? Bom, já sabe:")

        # Default text for vending. When some item is bought, its name in the list is changed to a blank space, removing it from the text.
        print(f"- {store[0]}{store[1]}{store[2]} Tudo pode ser seu com um pouco de dinheiro!")
        print_fast("- Então, já se decidiu? ")

        print("\n] barco | vela | corda | sair [")
        shop = input(">>> ").lower()

    if shop == "barco":     
        if money == 0:      # Player has no money.
            print_med("\n- Mas você não tem nenhum dinheiro! Some daqui!")
        
        else:       # Player has money.      
            if store[0] == "Barco? ":       # And the store has the boat.
                money -= 1

                print_med("\n- Pois bem aqui está seu barco, não me pergunte como você vai guardar isso.\n")

                ascii_boat()
                print_long("\n{ BARCO ADQUIRIDO }")

                bag.append("barco")
                store[0] = ""
            
            else:       # But the store doens't have the boat
                print_med("\n- Você por acaso vê algum outro barco aqui na loja? Não? Pois é...")

    elif shop == "corda":       # Player has no money.
        if money == 0:
            print_med("\n- Eu vou é te amarrar com a corda se você vier aqui sem dinheiro de novo!")

        else:       # Player has money.      
            if store[1] == "Corda? ":       # And the store has the rope.
                money -= 1

                print_med("\n- Uma corda para outra corda... ou algo assim, não sei.\n")

                ascii_rope()
                print_long("\n{ CORDA ADQUIRIDA }")

                bag.append("corda")
                store[1] = ""

            else:       # But the store doesn't have the rope.
                print_med("\n- É você comprou a última corda, mas quem ficou num nó fui eu...")

    elif shop == "vela":        # Player has no money.
        if money == 0:
            print_med("\n- A chama queimou seu dinheiro? Não? Então volta com um!")
        
        else:       # Player has money.
            if  store[2] == "Vela? ":       # And the store has the candle.
                money -= 1

                print_med("\n- Aqui está! Ela ilumina muito bem! Mas acho que você já sabe disso...\n")

                ascii_candle()
                print_long("\n{ VELA ADQUIRIDA }")

                bag.append("vela")
                store[2] = ""

            else:       # But the store doesn't have the candle.
                print_med("\n- Acha que vela dá em árvore? Se desse seria uma árvela. Mas não é...")

    elif shop == "voltar" or shop == "sair":    # User exits.
        print_fast("\n- Já vai embora? Pois bem, fique a vontade.")

    else:       # User inputs something invalid and gets out of store.
        print_med("\n- Acho que não temos isso no estoque, meu bom. Por que você não procura lá fora?")


def house_hints():
    global farm_potatoes

    hints = ["  ~ Há um rio perto da vila, você precisa de algo para desviar das piranhas.",
             "  ~ A taverna é um bom lugar para conseguir dinheiro.",
             "  ~ A floresta é perigosa no escuro.",
             f"  ~ Menos que {farm_potatoes + 25}, eu diria.",
             f"  ~ Mais que {farm_potatoes - 25}, se tivesse que chutar.",
             "  ~ Há coisas muito poderosas nesse mundo.",
             "  ~ Todo lugar tem algo importante.",
             f"  ~ {name} não é um nome comum aqui.",
             "  ~ Dizem que alguém se perdeu na floresta e nunca mais voltou.",
             "  ~ ...o fim nunca é o fim nunca é o fim nunca é o fim nunca é o fim nunca é o fim nunca é..."
             ]
    
    # Chooses 3 random items from the list and prints them as hints for the player.
    chosen = random.sample(hints, 3)
    print_fast(f"{chosen[0]}")
    print_fast(f"{chosen[1]}")
    print_fast(f"{chosen[2]}")


def path_2_house():
    """Takes care of the strange house.
    """
    global deaths
    global is_dead
    global deaths_seen

    global name
    global money
    global bag
    global potato_in_bag
    global house_visits
    global house_visits_potato

    if house_visits < 3:        # Checks how many time the user has visited the house.
        if house_visits == 0:       # Triggers when the player visits the house for the first time.
            print_med("\n> Você empurra a porta velha e revela uma sala escura com uma pessoa no centro.")
            print("\n- Hm seu rosto é novo por aqui... Qual seu nome?")

            answer = input(">>> ")
            if answer != name:
                print_med(f"\n- É MENTIRA!!!! Eu sei tudo sobre você, {name}! Inclusive o que vai acontecer agora!")

                # Ending 1
                is_dead = True
                if 1 not in deaths_seen:
                    deaths_seen.append(1)
                deaths = death_messages(1, deaths, deaths_seen)
                
                # Exits the funcion dead, goes to the death check.
                return

            else:
                money += 1
                print_med("\n- Bom eu já sabia disso, só queria checar sua honestidade.")
                print_med("- Aqui, pega um dinheiro como recompensa. Vai lá, pode pegar, você mereceu.\n")

                money_get(money)

                print_med("\n- Se você veio aqui imagino que esteja procurando por direções...")
                print_med("- Não posso dizer exatamente seu destino, mas posso lhe oferecer dicas:\n")

        elif house_visits > 0:      # Replaces the question from the first time. 
            print_med("\n- Hugh, você de novo? Quer mais dicas ou quer que eu repita? Que seja:\n")

        # Updates the number of visits after the texts.
        house_visits += 1

        house_hints()

        print_med("\n- Isso é tudo que tenho a dizer, e não tenho tanta paciência então maneire nas visitas.")
        print_med("> Ela te empurra para fora da casa e fecha a porta na sua cara.")

        if potato_in_bag and not house_visits_potato:       # Checks if the player has the potato (even if they've already entered the house before).
           
            # Adds 4 to the number of visits so that the house is automatically locked after the dialogue.
            house_visits += 4
            
            time.sleep(2)
            print_med("\n> Você está prestes a sair quando ouve a porta runhir.")
            print_med("\n- Na verdade tem mais uma coisa... Tem a ver com essa sua batata cuja presença é difícil de não notar.")
            print_long("- Muitos vão cobiça-la, mas eu sei que você vai dá-la apenas para quem a merece, mesmo que esse seja um sujeito diferente...")
            print_long("- Eu mesma sinto uma certa atração por tamanho vegetal... Mas consigo me conter... Eu acho...")
            print_long("- Na verdade é melhor você sair logo daqui com ela, antes que eu perca a razão. Confie em mim, é para o bem de nós dois.")
            print_med("\n> Você sai da casa apreensivo quanto ao destino da batata e escuta a porta sendo trancada.")

    elif house_visits == 3:         # Checks if the player has already visited the house 3 times; if so, locks it.
        house_visits += 1

        print_med("\n- Já falei que não quero você me visitando toda hora! Sai fora daqui de uma vez!")
        print_med("> Você é empurrado para fora da casa e escuta a porta sendo trancada.")

    elif house_visits > 3:          # Shows that the door is locked.

        print_fast("\n> É inútil, a porta está trancada")


def path_2_scarecrow():
    """Takes care of the scarecrow encounter.
    """
    global deaths
    global is_dead
    global deaths_seen

    global bag
    global potato_in_bag
    global farm_guesses
    global farm_visits
    global scarecrow_visits
    global scarecrow_visits_potato
    global farm_seen

    print_med("\n> O barco te leva tranquilamente até a outra margem do extenso rio.")
    print_med("> Você atraca o barco num pilar de madeira convenientemente colocado e segue reto.")

    # Loop from the margin of the river to the scarecrow.
    while True:
        print_med("\n> No horizonte a frente, você avista uma extensa plantação com o que parece ser um homem parado no centro.")  
        print_fast("> Para qual direção você vai ir?")

        print("\n] plantação | rio [")
        path_3 = input(">>> ").lower()

        if path_3 == "rio":         # Breaks out of the loop, exits the funcion.
            print_fast("\n> Você volta ao barco e retorna à outra margem.")
            break

        elif path_3 == "plantação" or path_3 == "plantaçao" or path_3 == "plantacão" or path_3 == "plantacao":
            if potato_in_bag:           # Checks if the player has already gotten the potato to block them from getting another
                if scarecrow_visits_potato < 2:         # Checks how many times they visited the scarecrow after getting the potato.
                    
                    # Updates the number of visits.
                    scarecrow_visits_potato += 1

                    print_med("\n- Mas o que ocê veio fazer aqui de novo, uai? Cê me perdoa mas eu não vou te dar mais nenhuma batatinha não, viu!")
                    print_med("- Então pode ir dando a volta, uma já basta.")
                    print_med("> Você dá meia volta e se afasta da plantação.")

                else:       # Checks if the player has gone more than 3 time to the scarecrow after getting the potato. 
                    print_med("\n- Ok agora já chega! Ocê já tem uma batata, se tá vindo aqui toda hora de novo é porque quer roubar mais uma!")
                    print_med("- Pois eu não vou deixar não, uai!")

                    # Ending 7
                    is_dead = True
                    if 7 not in deaths_seen:
                        deaths_seen.append(7)
                    deaths = death_messages(7, deaths, deaths_seen)

                    # Exits the funcion dead, goes to the death check.
                    return

            else:
                if not farm_seen:       # Checks if it's the first time the player has gotten here for more descriptive dialogue.
                    farm_seen = True        # Updates the checker.

                    print_med("\n> Avançando um pouco mais, você consegue ver que se trata de uma enorme plantação de batatas.")
                    print_med("> Em uma inspeção mais próxima, você vê que o misterioso homem é na verdade um grande espantalho.")
                    print_med("> Ele parece se movimentar um pouco, talvez seja devido ao vento.\n")

                elif farm_seen and not scarecrow_visits:        # Checks if the player has already been here but hasn't talked to the scarecrow yet. 
                    print_med("\n> O espantalho continua balançando solitariamente no campo de batatas.\n")

                else:       # Checks if the player has been here and has talked to the scarecrow already.
                    print_med("\n> O espantalho vigia atentamente suas batatas a procura de pessoas como você.\n")

                # Loop for the scarecrow encounter and minigame.
                while True:
                    if farm_visits == 0:        # Checks if it's the first time getting to the farm.
                        print_med("> A fragrância batatal te enche de determinação.")
                        print_fast("> Você pode tentar pegar uma batata ou ir embora. O que fazer?")

                        print("\n] pegar | voltar [")
                        path_4 = input(">>> ").lower()
                    
                    else:       # Checks if the player is returning.
                        print_fast("- Oia sô, ocê voltou! Vai tenta pega minhas batata dinovo?")

                        print("\n] pegar | voltar [")
                        path_4 = input(">>> ").lower()

                    if path_4 == "voltar":          # Breaks out of the loop, goes back to the start of the first loop.
                        if not scarecrow_visits:        # For if the player has not yet trigged the scarecrow scene.
                            print_med("\n> Enquanto volta, pelo canto do olho, você percebe o espantalho se movendo.")
                            break
                    
                        else:
                            print_fast("\n- Inté!")         # For if the player has already trigged the scarecrow scene.
                            print_med("> Você vai embora acenando para o espantalho enquanto se questiona como ele fala.")
                            break

                    elif path_4 == "pegar":
                        if not scarecrow_visits:        # Checks if it's the player first time interacting with the scarecrow.
                            scarecrow_visits = True         # Updates the checker.

                            print_med("\n> Você se prepara para puxar uma batata suculenta da terra.")
                            print_med("> O espantalho se move.")
                            print_med("\n- EI! EI! EI! Pode ir parando aí, sô! Tá pegando minhas batata porque?")
                            print_long("- Essas batatinhas são minhas e só minhas! Tira essas mãos di gente da cidade delas! Vai matar as coitada!")
                            print_long("- Nem adianta tenta pega elas, eu tô sempre de vigia, sô!\n")
                            print_med("- Mas intão, o que é que ocê faz aqui no meu batatal?")
                            print_med("- Quer uma batata, né? Elas são muito preciosa pra mim...")
                            print_long("- Mas eu acho que posso te dar uma, sô. Se ocê conseguir adivinhar quantas batata tem aqui na minha plantação todinha!")

                        else:
                            if farm_visits == 0:        # Checks if the player has never played the minigame yet.
                                print_med("\n- Oia, oia, sô, já falei pra não pegar a batata assim!")
                                print_med("- Eu sei que ocê quer muito conseguir uma, então é só ganhar no meu jogo, ora!")
                            
                            else:       # Checks if the player has already played the minigame.
                                print_med("\n- Na minha cara, sô? Tem vergonha não? Já te disse quié só ganhar meu jogo!")
                        
                        # Loop for the scarecrow's minigame.
                        while True:
                            print_fast("- Iaí? Vai tentar?")

                            print("\n] sim | não [")
                            potato_game = input(">>> ").lower()

                            if potato_game == "não" or potato_game == "nao":        # Breaks out of the loop, then breaks the next one and goes to the start of the first loop.
                                print_fast("\n- Uai, então pode ir embora!")
                                print_med("> Você sai da plantação de batatas sendo desaprovadamente encarado pelo espantalho.")
                                break

                            elif potato_game == "sim":
                                print_fast("\n- Aí senti firmeza!")

                                if farm_visits == 0:        # Explains the rules if it's the player's first time.
                                    
                                    # Updates how many times the minigame has been played.
                                    farm_visits += 1

                                    print_med("\n- Seguinte, fi, ocê tem 6 chance pra adivinhar quantas batata tem aqui.")
                                    print_med("- Eu posso dá umas dica: tá entre 100 e 200 e eu vou avisando se ocê tá próximo!")
                                    print_fast("- Certinho? Então podemo começa!")

                                else:
                                    
                                    # Updates how many times the minigame has been played.
                                    farm_visits += 1

                                    # Resets the number of guesses from the previous try.
                                    farm_guesses = 0

                                    print_med("\n- Bom ocê já sabe como funciona, então bora logo de uma vez!")

                                scarecrow_game()

                                if not potato_in_bag:       # If the player loses, they shouldn't have the potato, so it checkes that.
                                    if farm_visits < 3:         # Checks how many times the minigame has been played.
                                        print_med("\n- Uai, não conseguiu adivinhar? Mas se quiser dá pra tentar de novo outra vez, sô!")

                                    elif farm_visits == 3:      # Checks if the minigame has been played 3 times and triggers the scene.
                                        print_fast("> O espantalho olha sua direção com raiva.")
                                        print_med("\n- Caramba mas ocê já tentou 3 vezes e ainda não conseguiu? Ocê é ruim demais, uai!")
                                        print_med("- Se quer tanto minhas batata, toma essa logo, sô!")

                                        is_dead = True
                                        deaths = death_messages(3, deaths)

                                        # Exits the funcion dead, goes to the death check.
                                        return

                                    print_med("> Você sai da plantação cabisbaixo com a derrota.")
                                    break

                                break

                            else:       # Checks for invalid input in minigame question.
                                print_fast("\n- Sim ou não, uai!")

                        break

                    else:       # Checks for invalid input in "take the potato" question.
                        input_error(name)

        else:       # Checks for invalid input in "river or farm" question.
            input_error(name)


def scarecrow_game():
    """Plays the scarecrow's guessing game.
    """
    global bag
    global potato_in_bag
    global farm_guesses
    global farm_potatoes

    # Loop to limit the amount of guesses to 6 per try.
    while farm_guesses < 6:
        try:
            guess = int(input(">>> Escolha um número: "))

            if guess > farm_potatoes and farm_guesses < 5:      # Checks if it was wrong and if it wasn't the last guess.
                print_fast("\n- Mais pra baixo!\n")

            elif guess < farm_potatoes and farm_guesses < 5:        # Checks if it was wrong and if it wasn't the last guess.
                print_fast("\n- Pode subi que é mais pra cima!\n")

            # Updates the amount of guesses done.
            farm_guesses += 1

            if guess == farm_potatoes:      # Checks if the guess is correct.
                farm_guesses += 6
                potato_in_bag = True

                bag.append("batata")

                print_med("\n- ISSO MERMO! Acertou na mosca, sô!")
                print_med("- Tô impressionado! Acho que ocê merece uma batata minha finalmente...\n")

                ascii_potato()
                print_long("\n{ BATATA ADQUIRIDA }\n")

                print_med("- Bom agora que ocê já tem essa belezura acho que já pode ir embora...\n")
                print_med("> Com a saborosa batata guardada, você se despede do espantalho e sai da plantação.")

        # Catches inputs that aren't numbers.
        except ValueError:
            print_fast("\n- É pra escolher um número, sô!\n")


def main():
    """Main path of the game, all the different choices that result in a dead end (that don't have another branch) will branch from here.
    """
    global deaths
    global is_dead
    global deaths_seen

    global name

    if main_menu == 0:      # Checks if the player has choosen to quit while in the menus.
        quit()

    print_med("\n> Você acorda jogado no chão de terra, sem nenhuma lembrança do que lhe ocorreu.")

    # Main loop of the game, contains all the paths so if one of them ends or breaks out of their own loops, they still continue the game.
    while True:
        print_med("\n> A sua frente há uma bifurcação no caminho, que vai para a direita ou esquerda. Atrás de você há uma grande e misteriosa floresta.")
        print_fast("> Qual direção você pretende seguir?")

        print("\n] direita | esquerda | voltar [")
        path_1 = input(">>> ").lower()

        # First path option loop, goes from the bifurcation to all the others; it exists so the player can go back (by breaking out of it) and choose another path.   
        while True:
            if path_1 == "direita":  # Path to the river.
                print_med("\n> Seguindo essa direção você encontra um rio muito largo para pular por cima.")

                if "barco" in bag:      # Checks if the player has bought the boat to warn them they can traverse it now.
                    print_med("> Agora que você tem um barco, é possível ir em frente pelo rio em segurança.")

                else:       # Checks if the player hasn't bought the boat.
                    print_fast("> Você pode tentar ir em frente.")

                print_fast("> Para onde é melhor ir?")

                print("\n] rio | voltar [")
                path_2 = input(">>> ").lower()

                if path_2 == "voltar":       # Breaks out of the loop and goes back to the bifurcation at the start of the first one.
                    print_fast("\n> Você se afasta do rio.")
                    break

                elif path_2 == "rio":  # Path to the scarecrow.

                    if "barco" in bag:      # Checks if the player has the boat.
                        path_2_scarecrow()

                        if is_dead:

                            # Exits the function dead, goes to the death check.
                            return

                    else:       # Checks if the player doesn't have the boat.
                        print_med("\n> Você tenta nadar pelo rio mas logo sente várias mordidas pelo corpo.")

                        # Ending 0
                        is_dead = True
                        if 0 not in deaths_seen:
                            deaths_seen.append(0)
                        deaths = death_messages(0, deaths, deaths_seen)

                        # Exits the function dead, goes to the death check.
                        return

                else:       # Checks for invalid input in the river question.
                    input_error(name)

            elif path_1 == "esquerda":  # Path to the village
                print_med("\n> Seguindo a esquerda você se depara com uma vilinha pitoresca.")

                # Also a first path loop, but for all the village scenes.  
                while True:
                    print_med("\n> Há uma pequena loja à esquerda, uma casa suspeita em frente e à direita, uma taverna animada.")
                    print_fast("> Qual você pretende entrar?")

                    print("\n] esquerda | frente | direita | voltar [")
                    path_2 = input(">>> ").lower()

                    if path_2 == "voltar":      # Breaks out of this loop, then breaks out of the second and goes back to the bifurcation at the start of the first one.
                        break

                    elif path_2 == "esquerda":      # Path to the shop.
                        path_2_shop()

                        if is_dead:

                            # Exits the function dead, goes to the death check.
                            return

                    elif path_2 == "frente":        # Path to the strange house.
                        path_2_house()

                        if is_dead:

                            # Exits the function dead, goes to the death check.
                            return

                    else:       # Checks for invalid input in the "enter" question.
                        input_error(name)

                break

            elif path_1 == "voltar":  # Path to the forest.
                print_med("\n> Avançando para a floresta, o breu escurece sua vista. Você pode tentar desbravar em frente ou voltar para a segurança.")
                print_fast("> Qual direção você vai tomar?")

                print("\n] frente | voltar [")
                path_2 = input(">>> ").lower()

                if path_2 == "frente" and "vela" not in bag:        # Check if the player doesn't have the candle.
                    if potato_in_bag:       # But has the potato.
                        print_med("\n> A escuridão te apavora e você pega sua batata para te confortar.")
                        print_med("> Passos de algum ser ficam mais próximos.")

                        # Ending 4
                        is_dead = True
                        if 4 not in deaths_seen:
                            deaths_seen.append(4)
                        deaths = death_messages(4, deaths, deaths_seen)

                        # Exits the function dead, goes to the death check.
                        return

                    else:       # Nor has the potato.
                        print_med("\n> A escuridão te consome e você escuta passos vindo em sua direção.")

                        # Ending 2
                        is_dead = True
                        if 2 not in deaths_seen:
                            deaths_seen.append(2)
                        deaths = death_messages(2, deaths, deaths_seen)

                        # Exits the function dead, goes to the death check.
                        return

                elif path_2 == "frente" and "vela" in bag:      # Checks if the player has the candle.
                    if not potato_in_bag:       # But not the potato.
                        print_med("\n> Avançando com a vela, você consegue iluminar uma parte da floresta.")
                        print_med("> Um goblin aparentemente esfomeado aparece no seu campo de visão diminuto.")

                        # Ending 6
                        is_dead = True
                        if 6 not in deaths_seen:
                            deaths_seen.append(6)
                        deaths = death_messages(6, deaths, deaths_seen)

                        # Exits the function dead, goes to the death check.
                        return
                    
                    else:       # And the potato.
                        pass

                elif path_2 == "voltar":        # Breaks out of the loop and goes back to the bifurcation at the start of the first one.
                    break

                else:       # Checks for invalid input in the forest question
                    input_error(name)

            else:       # Checks for invalid input in the bifurcation question; has to break out of the loop to ask it again.
                input_error(name)
                break


# main() function loop.
while True:
    name = main_menu()

    while True:  
        main()
        is_dead = death_check(name, potato_in_bag, is_dead, deaths)
