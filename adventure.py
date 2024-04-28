import time
import random


def print_fast(text):
    """Prints and waits a small interval. Used for quick texts.
    """
    print(text)
    time.sleep(1)


def print_med(text):
    """Print and waits a slight bigger interval. Used for dialogues.
    """
    print(text)
    time.sleep(2)


def print_long(text):
    """Prints and waits a big interval. Used for dramatic pauses.
    """
    print(text)
    time.sleep(4)


name = input("Insira seu nome: ")

print(f"- Bem-vindo, {name}, a essa aventura!")

print("\nPara as respostas, por favor limite-se a opções simples como: ")
print_long("Direita, esquerda, frente, atacar, voltar, etc.")

print_med(f"\n- Agora, {name}, sua aventura pode começar...")

deaths = 0
is_dead = False

bag = []
money = 0
potato_in_bag = False

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


def death_messages(num):
    """Prints out a death message and the total number of endings found.
    """
    global deaths
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

    print_med(messages[num])
    print_med(f"Final: {num + 1} de {len(messages)} | Vistos: {deaths}")


def input_error():
    """Randomly picks an error message to print if the user inputs something that they shouldn't.
    """
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


def death_check():
    """Checks if the player can and wants to continue playing after a death; if not, ends the game.
    """
    global is_dead
    global bag

    if is_dead:
        time.sleep(3)
        print_med("\n- Parece-me que sua aventura chegou ao fim...")

        if potato_in_bag:
            print_med("- Mas vejo que já conseguiu....")
            print_med("- ...ela.")
            print_med("- Pois bem, se você quiser, eu posso te levar de volta ao início. Ela ainda tem um destino para cumprir.")
            print("- O que me diz? Sim ou não? Pense bem.")
            reset = input(">>> Vai continuar? ").lower()

            if reset == "sim":
                is_dead = False
                time.sleep(1)
                print_med("\n- Excelente... realmente excelente...")
                print_med(f"- Boa sorte, {name}, vai precisar.")
                print_long("\n> Um clarão te cega e você desmaia, caíndo no que parece ser o infinito.")

            else:
                time.sleep(1)
                print_med("\n- Que assim seja.")
                quit()

        else:
            print_med("- Infelizmente você não cumpriu o requisito para continuar a aventura...")
            print_long("- Mas não é nada pessoal, entenda; é a burocracia, a papelada, essas coisas, sabe?")
            print_med(f"\n- Bom, acho que isso é um adeus, {name}.")
            quit()


def path_2_shop():
    """Takes care of the shop.
    """
    global is_dead
    global bag
    global potato_in_bag
    global money
    global shop
    global store
    global shop_visits
    global shop_visits_potato

    if potato_in_bag and not shop_visits_potato:
        print_med("\n> Você entra na loja e o vendedor começa a fungar, como se estivesse cheirando algo.")
        print_long("- Isso é... Tem que ser... Não tem como confundir! Você conseguiu uma batata daquele espantalho! Elas são tão...")
        print_long("- ...preciosas.")
        print_long("- Hm esse cheiro de batata me deixou com fome... Eu não vou conseguir trabalhar com o desejo da batata...")
        print_long("- Ei, o que acha de você me vender essa batata? Vamos lá, eu te vendi o barco, lembra? Eu pago bem por ela, é sério! E aí? Sim ou não?\n")

        potato_bargain = input(">>> Você vende a batata? ").lower()
        if potato_bargain == "sim":
            time.sleep(1)
            print_long("\n> Você está prestes a colocar a batata no balcão mas não encontra forças para isso. E como se a batata não quisesse se separar de você...")
            print_med("> Você desiste e guarda a batata na mochila.")
            print_long("> O vendedor te olha furioso.")
            print_med("> E se joga em cima de você.")

            is_dead = True
            death_messages(5)
            return

        elif potato_bargain == "não" or "nao":
            shop_visits_potato = True
            money += 1
            time.sleep(1)
            print_med("\n- Bom a batata é sua, então você decide. Mas saiba que perdeu uma oferta milionária!")
            print_med("- O problema é que agora é que fiquei com fome e nem é horário de almoço ainda...")
            print_med("- Que tal assim: eu te dou um dinheiro como compensação por não te atender agora, você sai daqui e eu faço meu lanchinho!")
            print_med("- Sim, eu sei que eu sou generoso.")
            print_long("\n{ 1 DINHEIRO ADQUIRIDO }\n")
            print_long(f"> Você agora tem {money} dinheiro!")
            print_fast("\n> Você sai da loja para o vendedor comer e confuso quanto ao poder da batata")

    if store[0] == "" and store[1] == "" and store[2] == "":
        print_fast("\n- Bom me desculpe, mas você já comprou tudo que eu tinha! Volte aqui quando eu tiver novos produtos.")

    elif shop_visits == 0:
        shop_visits += 1
        time.sleep(1)
        print("\n- Ora vejam só um freguês novo! Faz um bom tempo que não recebo dinheiro vindo de outras bandas!")
        print(f"- {store[0]}{store[1]}{store[2]} É tudo seu, isso se você tiver o dinheiro suficiente!")
        shop = input("- Então, o que vai ser? ").lower()

    else:
        if shop_visits_potato:
            time.sleep(1)
            print("\n- Olha só é o cara batata! Já sabe:")
        else:
            time.sleep(1)
            print("\n- Você de novo? Bom, já sabe:")

        print(f"-{store[0]}{store[1]}{store[2]} Tudo pode ser seu com um pouco de dinheiro")
        shop = input("- Então, já se decidiu? ").lower()

    if shop == "barco" and store[0] == "Barco? ":
        if money == 0:
            print_fast("\n- Mas você não tem nenhum dinheiro! Some daqui!")
        else:
            money -= 1
            print_med("\n- Pois bem aqui está seu barco, não me pergunte como você vai guardar isso.")
            print_long("\n{ BARCO ADQUIRIDO }")
            bag.append("barco")
            store.remove("Barco? ")
            store.insert(0, "")

    elif shop == "corda" and store[1] == "Corda? ":
        if money == 0:
            print_fast("\n- Eu vou é te amarrar com a corda se você vier aqui sem dinheiro de novo!")
        else:
            money -= 1
            print_med("\n- Uma corda para outra corda... ou algo assim, não sei.")
            print_long("\n{ CORDA ADQUIRIDA }")
            bag.append("corda")
            store.remove("Corda? ")
            store.insert(1, "")

    elif shop == "vela" and store[2] == "Vela? ":
        if money == 0:
            print_fast("\n- A chama queimou seu dinheiro? Não? Então volta com um!")
        else:
            money -= 1
            print_med("\n- Aqui está! Ela ilumina muito bem! Mas acho que você já sabe disso...")
            print_long("\n{ VELA ADQUIRIDA }")
            bag.append("vela")
            store.remove("Vela? ")
            store.insert(2, "")

    elif shop == "voltar" or shop == "sair":
        print_fast("\n- Já vai embora? Pois bem, fique a vontade.")

    else:
        print_fast("\n- Acho que não temos isso no estoque, meu bom. Por que você não procura lá fora?")


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
    
    chosen = random.sample(hints, 3)
    print_fast(f"{chosen[0]}")
    print_fast(f"{chosen[1]}")
    print_fast(f"{chosen[2]}")



def path_2_house():
    """Takes care of the strange house.
    """
    global is_dead
    global money
    global bag
    global potato_in_bag
    global house_visits
    global house_visits_potato

    if house_visits < 3:

        if house_visits == 0:
            print_med("\n> Você empurra a porta velha e revela uma sala escura com uma pessoa no centro.")
            answer = input("\n- Hm seu rosto é novo por aqui... Qual seu nome? ")

            if answer != name:
                print_med(f"\n- É MENTIRA!!!! Eu sei tudo sobre você, {name} inclusive o que vai acontecer agora!")

                is_dead = True
                death_messages(1)
                return

            else:
                money += 1
                print_fast("\n- Bom eu já sabia disso, só queria checar sua honestidade.")
                print_med("- Aqui, pega um dinheiro como recompensa. Vai lá, pode pegar, você mereceu.")
                print_long("\n{ 1 DINHEIRO ADQUIRIDO }\n")
                print_long(f"> Você agora tem {money} dinheiro!")
                print_fast("\n- Se você veio aqui imagino que esteja procurando por direções...")
                print_med("- Não posso dizer exatamente seu destino, mas posso lhe oferecer dicas:\n")

        elif house_visits > 0:
            print_fast("\n- Hugh, você de novo? Quer mais dicas ou quer que eu repita? Que seja:\n")

        house_visits += 1

        house_hints()
        print_med("\n- Isso é tudo que tenho a dizer, e não tenho tanta paciência então maneire nas visitas.")
        print_med("> Ela te empurra para fora da casa e fecha a porta na sua cara.")

        if potato_in_bag and not house_visits_potato:
            house_visits += 4
            time.sleep(2)
            print_med("\n> Você está prestes a sair quando ouve a porta runhir.")
            print_med("\n- Na verdade tem mais uma coisa... Tem a ver com essa sua batata cuja presença é difícil de não notar.")
            print_long("- Muitos vão cobiça-la, mas eu sei que você vai dá-la apenas para quem a merece, mesmo que esse seja um sujeito diferente...")
            print_long("- Eu mesma sinto uma certa atração por tamanho vegetal... Mas consigo me conter... Eu acho...")
            print_med("- Na verdade é melhor você sair logo daqui com ela, antes que eu perca a razão. Confie em mim, é para o bem de nós dois.")
            print_fast("\n> Você sai da casa apreensivo quanto ao destino da batata e escuta a porta sendo trancada.")

    elif house_visits == 3:
        house_visits += 1
        print_fast("\n- Já falei que não quero você me visitando toda hora! Sai fora daqui de uma vez!")
        print_med("> Você é empurrado para fora da casa e escuta a porta sendo trancada.")

    elif house_visits > 3:
        print_fast("\n> É inútil, a porta está trancada")


def path_2_scarecrow():
    """Takes care of the scarecrow encounter.
    """
    global is_dead
    global bag
    global potato_in_bag
    global farm_guesses
    global farm_visits
    global scarecrow_visits
    global scarecrow_visits_potato
    global farm_seen

    print("\n> O barco te leva tranquilamente até a outra margem do extenso rio.")
    print_fast("> Você atraca o barco num pilar de madeira convenientemente colocado e segue reto.")

    while True:
        print("\n> No horizonte a frente, você avista uma extensa plantação com o que parece ser um homem parado no centro.")
        path_3 = input(">>> Qual caminho você vai escolher? ")

        if path_3 == "voltar":
            print_fast("\n> Você volta para o barco e retorna para a outra margem.")
            break

        elif path_3 == "frente":
            if potato_in_bag:
                if scarecrow_visits_potato < 2:
                    scarecrow_visits_potato += 1
                    print_fast("\n- Mas o que ocê veio fazer aqui de novo, uai? Cê me perdoa mas eu não vou te dar mais nenhuma batatinha não, viu!")
                    print_med("- Então pode ir dando a volta, uma já basta.")
                    print_med("> Você dá meia volta e se afasta da plantação.")

                else:
                    print("\n- Ok agora já chega! Ocê já tem uma batata, se tá vindo aqui toda hora de novo é porque quer roubar mais uma!")
                    print_med("- Pois eu não vou deixar não, uai!")

                    is_dead = True
                    death_messages(7)
                    return

            else:
                if not farm_seen:
                    farm_seen = True
                    print_fast("\n> Avançando um pouco mais, você consegue ver que se trata de uma enorme plantação de batatas.")
                    print_fast("> Em uma inspeção mais próxima, você vê que o misterioso homem é na verdade um grande espantalho.")
                    print_med("> Ele parece se movimentar um pouco, talvez seja devido ao vento.\n")

                elif farm_seen and not scarecrow_visits:
                    print_med("\n> O espantalho continua balançando solitariamente no campo de batatas.\n")

                else:
                    print_med("\n> O espantalho vigia atentamente suas batatas a procura de pessoas como você.\n")

                while True:
                    if farm_visits == 0:
                        print("> A fragrância batatal te enche de determinação.")
                        path_4 = input(">>> Você pode tentar pegar uma batata ou ir embora. O que fazer? ")
                    
                    else:
                        path_4 = input("\n- Oia sô, ocê voltou! Vai tenta pega minhas batata dinovo? ")

                    if path_4 == "voltar":
                        if not scarecrow_visits:
                            print_fast("\n> Enquanto volta, pelo canto do olho, você percebe o espantalho se movendo.")
                            break
                    
                        else:
                            print_fast("\n- Inté!")
                            print_med("> Você vai embora acenando para o espantalho enquanto se questiona como ele fala.")
                            break

                    elif path_4 == "pegar":

                        if not scarecrow_visits:
                            scarecrow_visits = True
                            print_med("\n> Você se prepara para puxar uma batata suculenta da terra.")
                            print_med("> O espantalho se move.")
                            print_med("\n- EI! EI! EI! Pode ir parando aí, sô! Tá pegando minhas batata porque?")
                            print_long("- Essas batatinhas são minhas e só minhas! Tira essas mãos di gente da cidade delas! Vai matar as coitada!")
                            print_long("- Nem adianta tenta pega elas, eu tô sempre de vigia, sô!\n")
                            print("- Mas intão, o que é que ocê faz aqui no meu batatal?")
                            print_med("- Quer uma batata, né? Elas são muito preciosa pra mim...")
                            print_long("- Mas eu acho que posso te dar uma, sô. Se ocê conseguir adivinhar quantas batata tem aqui na minha plantação todinha!")

                        else:
                            if farm_visits == 0:
                                print("\n- Oia, oia, sô, já falei pra não pegar a batata assim!")
                                print_med("- Eu sei que ocê quer muito conseguir uma, então é só ganhar no meu jogo, ora!")
                            
                            else:
                                print_med("\n- Na minha cara, sô? Tem vergonha não? Já te disse quié só ganhar meu jogo!")

                        while True:
                            potato_game = input("- Iaí? Vai tentar? Sim ou não? ").lower()

                            if potato_game == "não" or potato_game == "nao":
                                print_fast("\n- Uai, então pode ir embora!")
                                print_med("> Você sai da plantação de batatas sendo desaprovadamente encarado pelo espantalho.")
                                break

                            elif potato_game == "sim":
                                print_fast("\n- Aí senti firmeza!")

                                if farm_visits == 0:
                                    farm_visits += 1
                                    print_fast("\n- Seguinte, fi, ocê tem 6 chance pra adivinhar quantas batata tem aqui.")
                                    print_long("- Eu posso dá umas dica: tá entre 100 e 200 e eu vou avisando se ocê tá próximo!")
                                    print_med("- Certinho? Então podemo começa!")

                                else:
                                    farm_visits += 1
                                    farm_guesses = 0
                                    print_med("\n- Bom ocê já sabe como funciona, então bora logo de uma vez!")

                                scarecrow_game()

                                if not potato_in_bag:
                                    if farm_visits < 3:
                                        print_fast("\n- Uai, não conseguiu adivinhar? Mas se quiser dá pra tentar de novo outra vez, sô!")

                                    elif farm_visits == 3:
                                        print_fast("> O espantalho olha sua direção com raiva.")
                                        print("\n- Caramba mas ocê já tentou 3 vezes e ainda não conseguiu? Ocê é ruim demais, uai!")
                                        print_med("- Se quer tanto minhas batata, toma essa logo, sô!")

                                        is_dead = True
                                        death_messages(3)
                                        return

                                    print_med("> Você sai da plantação cabisbaixo com a derrota.")
                                    break

                                break

                            else:
                                print("\n- Sim ou não, uai!\n")

                        break

                    else:
                        input_error()

        else:
            input_error()


def scarecrow_game():
    """Plays the scarecrow's guessing game.
    """
    global farm_guesses
    global farm_potatoes
    global bag
    global potato_in_bag

    while farm_guesses < 6:
        try:
            guess = int(input(">>> Escolha um número: "))

            if guess > farm_potatoes and farm_guesses < 5:
                print_fast("\n- Mais pra baixo!\n")

            elif guess < farm_potatoes and farm_guesses < 5:
                print_fast("\n- Pode subi que é mais pra cima!\n")

            farm_guesses += 1

            if guess == farm_potatoes:
                farm_guesses += 6
                potato_in_bag = True
                bag.append("batata")
                print_med("\n- ISSO MERMO! Acertou na mosca, sô!")
                print_med("- Tô impressionado! Acho que ocê merece uma batata minha finalmente...")
                print_long("\n{ BATATA ADQUIRIDA }\n")
                print_med("- Bom agora que ocê já tem essa belezura acho que já pode ir embora...\n")
                print_med("> Com a saborosa batata guardada, você se despede do espantalho e sai da plantação.")

        except ValueError:
            print("\n- É pra escolher um número, sô!\n")


def main():
    """Main path of the game, all the different choices that result in a dead end (that don't have another branch) will branch from here.
    """
    global is_dead

    print_fast("\n> Você acorda jogado no chão de terra, sem nenhuma lembrança do que lhe ocorreu.")

    while True:
        print("\n> A sua frente há uma bifurcação no caminho, que vai para a direita ou esquerda. Atrás de você há uma grande e misteriosa floresta a qual você pode voltar.")
        path_1 = input(">>> Qual direção você pretende seguir? ").lower()

        while True:
            if path_1 == "direita":  # rio
                print_fast("\n> Seguindo essa direção você encontra um rio muito largo para pular por cima.")

                if "barco" in bag:
                    print("> Agora que você tem um barco, é possível ir em frente pelo rio em segurança.")
                else:
                    print("> Você pode tentar ir em frente.")

                path_2 = input(">>> Para onde é melhor ir? ").lower()

                if path_2 == "voltar":
                    print_fast("\n> Você se afasta do rio.")
                    break

                elif path_2 == "frente":  # espantalho

                    if "barco" in bag:
                        path_2_scarecrow()

                        if is_dead:
                            return

                    else:
                        print_med("\n> Você tenta nadar pelo rio mas logo sente várias mordidas pelo corpo.")

                        is_dead = True
                        death_messages(0)
                        return

                else:
                    input_error()

            elif path_1 == "esquerda":  # vila
                print_fast("\n> Seguindo a esquerda você se depara com uma vilinha pitoresca.")

                while True:
                    print("\n> Há uma pequena loja à esquerda, uma casa suspeita em frente e à direita, uma taverna animada.")
                    path_2 = input(">>> Qual direção você pretende seguir? ").lower()

                    if path_2 == "voltar":
                        break

                    elif path_2 == "esquerda":  # loja
                        path_2_shop()

                        if is_dead:
                            return

                    elif path_2 == "frente":  # casa
                        path_2_house()

                        if is_dead:
                            return

                    else:
                        input_error()

                break

            elif path_1 == "voltar":  # floresta
                print("\n> Avançando para a floresta, o breu escurece sua vista. Você pode tentar desbravar em frente ou voltar para a segurança.")
                path_2 = input(">>> Qual direção você vai tomar? ").lower()

                if path_2 == "frente" and "vela" not in bag:
                    if potato_in_bag:
                        print("\n> A escuridão te apavora e você pega sua batata para te confortar.")
                        print_med("> Passos de algum ser ficam mais próximos.")

                        is_dead = True
                        death_messages(4)
                        return

                    else:
                        print_med("\n> A escuridão te consome e você escuta passos vindo em sua direção.")

                        is_dead = True
                        death_messages(2)
                        return

                elif path_2 == "frente" and "vela" in bag:
                    if not potato_in_bag:
                        print("\n> Avançando com a vela, você consegue iluminar uma parte da floresta.")
                        print_med("> Um goblin aparentemente esfomeado aparece no seu campo de visão diminuto.")

                        is_dead = True
                        death_messages(6)
                        return

                elif path_2 == "voltar":
                    break

                else:
                    input_error()

            else:
                input_error()
                break


while True:
    main()
    death_check()
