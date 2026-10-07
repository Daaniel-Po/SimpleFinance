##########Global Variables########
title = None
message = None

##############Lists################
info_users = []
category = []
menu_tui = ["1-Adicionar", "2-Remover", "3-Analisar", "4-Atualizar", "5-Sair"]


##########Interfaces##########
while True:
    ############MENU###############
    print("\n" * 100)
    print("======MENU======")
    if message != None:
        print(f"[Aviso]: {message}")
    print()
    print("1-Atualizar carteira")
    print("2-Modificar categorias")
    print("3-Analisar economia mensal")
    print("4-Modificar perfis")
    print("5-Sair")
    input_system = int(input("Digite uma opção em números:"))

    #########Conditions Menu########
    if input_system == 1:
        title = "Carteira"
        message = None

        while True:
            print("\n" * 100)

            ############TUI##############
            print(f"======{title}======")

            for item in menu_tui:
                print(item)
            input_action = int(input("Digite uma opção em números:"))

            ###########Conditions TUI###########
            match input_action:
                case 1:
                    pass
                case 2:
                    pass
                case 3:
                    pass
                case 4:
                    pass
                case 5:
                    break
                case _:
                    print("Número inválido")
    elif input_system == 2:
        title = "Categoria"
        message = "Funcionalidade em desenvolvimento."
    elif input_system == 3:
        title = "Economia Mensal"
        message = "Funcionalidade em desenvolvimento."
    elif input_system == 4:
        title = "Perfis"
        message = "Funcionalidade em desenvolvimento."
    elif input_system == 5:
        print("Programa encerrando!")
        break
    else:
        message = "Número inválido."