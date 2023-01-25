# Leia o Readme

idade = int(input('Digite qualquer idade: '))

if idade < 12:
    faixa_etaria = 'Criança'

elif idade < 18:
    faixa_etaria = 'Adolescente'

elif idade < 30:
    faixa_etaria = 'Jovem'

elif idade < 60:
    faixa_etaria = 'Adulto'

else:
    faixa_etaria = 'Idoso'

print(faixa_etaria)
