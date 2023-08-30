# Entrada de dados
saldo_total = int(input())
valor_saque = int(input())

saldo_total = saldo_total - valor_saque

# TODO: Criar as condições necessárias para impressão da saída, vide tabela de exemplos.

print("Saldo insuficiente. Saque nao realizado!") if saldo_total < 0 else print(
    f"Saque realizado com sucesso. Novo saldo: {saldo_total}")
