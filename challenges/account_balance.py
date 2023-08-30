saldo_atual = float(input("Informe seu saldo atual\n"))
valor_deposito = float(input("Informe o valor depositado\n"))
valor_retirado = float(input("Informe o valor retirado\n"))

# TODO: Calcular o saldo atualizado de acordo com a descrição deste desafio.

saldo_atual = saldo_atual + valor_deposito - valor_retirado
# TODO: Imprimir o a saída de conforme a tabela de exemplos (uma casa decimal).

print(f"Saldo atualizado na conta: {saldo_atual:.1f}")
