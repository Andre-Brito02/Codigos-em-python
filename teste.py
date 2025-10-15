dia,mes,ano = input("Digite sua data de nascimento: ").split(" ")
print(dia, mes, ano)
separador = "/"
data_nascimento = separador.join([dia,mes,ano])
print(data_nascimento)