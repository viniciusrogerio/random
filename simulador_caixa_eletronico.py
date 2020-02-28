print('== CAIXA ELETRÔNICO ==')
print('Cédulas disponíveis: R$ 100, R$ 50, R$ 20 e R$ 10\n\n')
valor = int(input('Digite o valor a ser sacado em R$: '))
notas_100, notas_50, notas_20, notas_10 = 0,0,0,0
saque_possivel = True

while valor>0:
    if valor//100 > 0:
        notas_100 = valor//100
        valor -= notas_100*100
        if valor == 0:
            break
    if valor//50 > 0:
        notas_50 = valor//50
        valor -= notas_50*50
        if valor == 0:
            break
    if valor//20 > 0:
        notas_20 = valor//50
        valor -= notas_20*20
        if valor == 0:
            break
    if valor//10 > 0:
        notas_10 = valor//10
        valor -= notas_10*10
        if valor == 0:
            break            
    else:
        print('Impossível sacar o valor informado. Favor atentar para as notas disponíveis.')
        saque_possivel = False
        break

if(saque_possivel):     
    print('Saque realizado: ')
    if(notas_100>0):
        print(f'{notas_100} notas de R$ 100')
    if(notas_50>0):
        print(f'{notas_50} notas de R$ 50')
    if(notas_20>0):
        print(f'{notas_20} notas de R$ 20')
    if(notas_10>0):
        print(f'{notas_10} notas de R$ 10')