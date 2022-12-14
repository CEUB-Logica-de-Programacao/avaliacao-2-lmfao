# Você recebe uma lista de preços onde o `preço[i]` é o preço de uma determinada ação no i-ésimo dia.
#
# Você quer maximizar seu lucro escolhendo um único dia para comprar uma ação e escolhendo um dia diferente no futuro para
# vender essa ação.
#
# Retorne o lucro máximo que você pode obter com esta transação. Se você não puder obter nenhum lucro, devolva 0.
#
# ### Exemplo 1
#
# ```
# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explicação: Compre no segundo dia (preço = 1) e venda no dia 5 (preço = 6), lucro = 6-1 = 5.
# ```
#
# ### Exemplo 2
#
# ```
# Input: prices = [7,6,4,3,1]
# Output: 0
# Explicação: Não é possível obter lucro, pois o preço de venda deve ser maior que o preço de compra.
# ```

def q3(prices):
    lucro_max = 0
    for i in range(len(prices) - 1):
        for j in range(i + 1, len(prices)):
            lucro = prices[j] - prices[i]
            if lucro > lucro_max:
                lucro_max = lucro
                
    return lucro_max
    


if __name__ == '__main__':
    print(q3([7, 1, 5, 3, 6, 4]))
