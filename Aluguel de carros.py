dias = int(input('Por quantos dias o carro foi alugado? '))
km = float(input('Quantos KM o carro andou? '))
pagamento = (dias * 60) + (km * 0.15)
print(f'O total a pagar pelo aluguel é R${pagamento:.2f}')
input('Pressione Enter para encerrar o programa...')
