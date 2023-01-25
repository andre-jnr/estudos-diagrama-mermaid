print('Sempre subtrai pelo maior')

print('-' * 20)
n1 = int(input('Insira um número: '))
n2 = int(input('Insira um número: '))
print('-' * 20)

if (n1 > n2):
    diferença = n1 - n2
else:
    diferença = n2 - n1

print(f'Diferença: {diferença}')
