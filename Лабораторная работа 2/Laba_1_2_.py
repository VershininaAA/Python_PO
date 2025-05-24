capital = 20000  # ѕодушка безопасности
salary = 5000  # ≈жемес€чна€ зарплата
wastes = 6000  # “раты за первый мес€ц
inflation = 0.05  # ≈жемес€чный рост цен


months = 0
while capital >= 0:
    capital += salary - wastes
    wastes *= (1 + inflation)
    if capital < 0:
        break
    months += 1

print(' оличество мес€цев, которое можно прот€нуть без долгов:', months)
