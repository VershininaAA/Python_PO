import math
salary = 5000  # ≈жемес€чна€ зарплата
wastes = 6000  # “раты за первый мес€ц
months = 10  #  оличество мес€цев
inflation = 0.03  # ≈жемес€чный рост цен


required_cushion = 0

for _ in range(months):
    deficit = max(0, wastes - salary)
    required_cushion += deficit
    wastes *= (1 + inflation)
print(f'ѕодушка безопасности, чтобы прот€нуть 10 мес€цев без долгов:', math.ceil(required_cushion))
