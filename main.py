from random import choice, shuffle

def embaralhar(listaSenha):
    listaSenha = shuffle(listaSenha)

lista_letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
lista_numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
lista_simbolos = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Bem vindo ao Gerador de senhas")
num_letras = int(input("Quantidade de LETRAS na senha: "))
num_numero  = int(input("Quantidade de NUMEROS na senha: "))
num_simbolos = int(input("Quantidade de SIMBOLOS na senha: "))

listaSenha = []

## lista = [novo_item for _ in range(inicio, fim)]
listaSenha = [choice(lista_letras) for _ in range(0, num_letras)]
listaSenha += [choice(lista_numeros) for _ in range(0, num_numero)]
listaSenha += [choice(lista_simbolos) for _ in range(0, num_simbolos)]

resp = str(input("Deseja embaralhar a senha: ")).upper()
if (resp == "S"):
    embaralhar(listaSenha)

## join (junta todos os itens da "lista senha" em uma string)
senha_final = "".join(listaSenha)

print(f"Nova senha: {senha_final}")

