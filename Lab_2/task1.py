money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов

print("Количество месяцев, которое можно протянуть без долгов:", ...)

money_capital = 20000
salary = 5000
spend = 6000
increase = 0.05

months = 0

while True:
    money = money_capital + salary

    if money >= spend:
        months += 1
        money_capital -= (spend - salary)
        spend *= (1 + increase)

    else:
        break

print("Количество месяцев, которое можно протянуть без долгов:", months)
