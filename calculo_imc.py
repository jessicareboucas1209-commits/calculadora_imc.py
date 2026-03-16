nome_paciente = input("Digite o nome do paciente: ")
peso_kg = float(input(f"Digite o peso de {nome_paciente} em kg: "))
altura = float(input(f"Qual a altura de {nome_paciente} em metros: "))

peso_gramas = peso_kg * 1000
imc = peso_kg / (altura ** 2)

print("-" * 30)
print(f"RELATÓRIO MÉDICO")
print(f"Paciente: {nome_paciente}")
print(f"Peso: {peso_gramas} gramas")
print(f"IMC: {imc:.2f}")

input("\nProcesso finalizado. Aperte ENTER para sair.")
