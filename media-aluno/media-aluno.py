notas = []

print('Média aluno')
print()

for i in range(1, 4):
    notas.append(float(input(f'Insira a {i}° nota: ')))

media = sum(notas) / len(notas)

if media >= 5:
    status = 'Aprovado'
else:
    status = 'Reprovado'

print(f'Média: {media:.2f}')
print('Status:', status)
