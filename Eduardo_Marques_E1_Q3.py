n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
n3 = float(input("Digite a terceira nota: "))
frequencia = float(input('Qual a frequência do aluno em % ? '))

media = ((n1 + n2 + n3) / 3)
if frequencia >= 75 and  media >= 7: 
    print('A média do aluno é: ',media,' e ele está aprovado.')
else: 
    print('A média do aluno é: ',media,' e ele está reprovado.')
