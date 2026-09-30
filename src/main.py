##########Global Variables########
income = None
wage = None
expenses = None
economy_month = None
expense_month = None
title = None


##############Lists################
info_users = []
category = []


##########Interface##########
print("======MENU======")
print()
print("1-Atualizar carteira")
print("2-Modificar categorias")
print("3-Analisar economia mensal")
print("4-Modificar perfis")
print("5-Sair")
input_system = int(input("Digite uma opção em números:"))

##########Conditions###########
if input_system == 1:
    title = "Carteira"
elif input_system == 2:
    title = "Categoria"
elif input_system == 3:
    title = "Economia Mensal"
elif input_system == 4:
    title = "Perfis"
elif input_system == 5:
    exit()
else:
    print("Número inválido")

############TUI##############
print(f"======{title}======")
print("1-Adicionar")
print("2-Remover")
print("3-Analisar")
print("4-Atualizar")
print("5-Sair")
