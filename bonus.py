# Dada uma lista de números inteiros não-negativos, organize-os de modo que formem o maior número e devolva-o.
#
# Como o resultado pode ser muito grande, é preciso devolver uma string em vez de um número inteiro.
#
# ### Exemplo 1
#
# ```
# Input: nums = [10,2]
# Output: "210"
# ```
#
# ### Exemplo 2
#
# ```
# Input: nums = [3,30,34,5,9]
# Output: "9534330"
# ```


def bonus(nums):
    current_max = ""
    ans = ""
    nums=[str(i) for i in nums]
    while nums:
        for i in nums:
            if not current_max:
                current_max=i
            else:
                # Comparator
                if i+current_max>current_max+i:
                    current_max=i
        ans+=current_max
        nums.remove(current_max)
        current_max=""
    return ans if not ans.startswith("0") else "0"


if __name__ == '__main__':
    print(bonus([3, 30, 34, 5, 9]))
