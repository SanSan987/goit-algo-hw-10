import pulp

# Створення проблеми максимізації
model = pulp.LpProblem("Maximize Production", pulp.LpMaximize)

# Змінні рішень: кількість виробленого лимонаду і фруктового соку
lemonade = pulp.LpVariable('Lemonade', lowBound=0, cat='Continuous')
fruit_juice = pulp.LpVariable('Fruit_Juice', lowBound=0, cat='Continuous')

# Функція цілі: максимізація кількості виробленого лимонаду та фруктового соку
model += lemonade + fruit_juice, "Total Production"

# Обмеження на ресурси
model += 2 * lemonade + 1 * fruit_juice <= 100, "Water Constraint"
model += 1 * lemonade <= 50, "Sugar Constraint"
model += 1 * lemonade <= 30, "Lemon Juice Constraint"
model += 2 * fruit_juice <= 40, "Fruit Puree Constraint"

# Розв'язання задачі
model.solve()

# Виведення результатів
print(f"Status: {pulp.LpStatus[model.status]}")
print(f"Лимонад: {lemonade.varValue} одиниць")
print(f"Фруктовий сік: {fruit_juice.varValue} одиниць")
print(f"Максимальна кількість продуктів: {pulp.value(model.objective)} одиниць")

# Результат: Status: Optimal
# Лимонад: 30.0 одиниць
# Фруктовий сік: 20.0 одиниць
# Максимальна кількість продуктів: 50.0 одиниць