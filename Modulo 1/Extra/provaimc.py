nome = input('Digite o nome do paciente: ')

altura = float(input('Digite a altura do paciente: '))
peso = float(input('Digite o peso do paciente: '))

imc = peso / (altura * altura)

if imc < 18.5:
    print('abaixo do peso')
elif imc < 24.9:
    print('peso normal')
elif imc < 29.9:
    print('sobrepeso')
elif imc < 34.9:
    print('Obesidade grau I')
elif imc < 39.9:
    print('obesidade grau II')
else:
    print('obesidade grau III')

print(f'O paciente {nome} tem IMC = {imc:.2f}')