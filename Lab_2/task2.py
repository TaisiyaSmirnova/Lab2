salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен

# TODO Рассчитайте подушку безопасности, чтобы протянуть 10 месяцев без долгов

print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", ...)

salary = 5000
spend = 6000
months = 10
increase = 0.03

money_capital = 0
for month in range(1, months + 1):
    if month > 1:
        spend *= (1 + increase)

    shortage = max(spend - salary, 0)

    money_capital += shortage

required_cushion = round(money_capital)
print("Подушка безопасности, чтобы протянуть 10 месяцев без долгов:", required_cushion)
