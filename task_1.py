
import pulp
print("PuLP successfully imported!")


# Створення проблеми максимізації
model = pulp.LpProblem("Maximize_Production", pulp.LpMaximize)

# Визначення змінних
x = pulp.LpVariable('Lemonade', lowBound=0, cat='Continuous')
y = pulp.LpVariable('Fruit_Juice', lowBound=0, cat='Continuous')

# Цільова функція
model += x + y, "Total_Products"

# Обмеження
model += 2 * x + y <= 100, "Water_Constraint"
model += x <= 50, "Sugar_Constraint"
model += x <= 30, "Lemon_Juice_Constraint"
model += 2 * y <= 40, "Fruit_Puree_Constraint"

# Розв'язання проблеми
model.solve()

# Вивід результатів
print(f"Status: {pulp.LpStatus[model.status]}")
print(f"Optimal number of Lemonade bottles to produce: {pulp.value(x)}")
print(f"Optimal number of Fruit Juice bottles to produce: {pulp.value(y)}")
