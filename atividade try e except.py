



Idade = 0
try:
    while Idade <= 0:
        nome = str(input("Qual o seu nome?"))
        email = str(input("Digite o seu E-Mail:"))
        Idade = int(input("Digite a sua Idade:"))
    if Idade >= 18:
        print("Situação: Maior de Idade")
    else:
        print("Situação: Menor de Idade")

    if Idade <= 0:
        print("Por favor, insira uma idade valida.")
except TypeError:
    print("Erro de caractere inválido!")


with open("Cadastros.txt" , "a") as cadastros:
    cadastros.write(f"=== Dados Cadastrados === \n Nome: {nome} \n E-mail: {email} \n Idade: {Idade} \n")
    if Idade <= 17:
        cadastros.write("Situação: Menor de Idade")
 

    
