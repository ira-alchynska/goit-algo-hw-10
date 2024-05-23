import matplotlib.pyplot as plt
import numpy as np
import scipy.integrate as spi

# Визначення функції та межі інтегрування
def f(x):
    return x ** 2

a = 0  # Нижня межа
b = 2  # Верхня межа

# Створення діапазону значень для x
x = np.linspace(-0.5, 2.5, 400)
y = f(x)

# Створення графіка
fig, ax = plt.subplots()

# Малювання функції
ax.plot(x, y, 'r', linewidth=2)

# Заповнення області під кривою
ix = np.linspace(a, b)
iy = f(ix)
ax.fill_between(ix, iy, color='gray', alpha=0.3)

# Налаштування графіка
ax.set_xlim([x[0], x[-1]])
ax.set_ylim([0, max(y) + 0.1])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')

# Додавання меж інтегрування та назви графіка
ax.axvline(x=a, color='gray', linestyle='--')
ax.axvline(x=b, color='gray', linestyle='--')
ax.set_title('Графік інтегрування f(x) = x^2 від ' + str(a) + ' до ' + str(b))
plt.grid()
plt.show()

# Метод Монте-Карло для обчислення інтегралу
N = 10000  # Кількість випадкових точок
x_random = np.random.uniform(a, b, N)
y_random = f(x_random)
integral_mc = (b - a) * np.mean(y_random)

print(f"Інтеграл методом Монте-Карло: {integral_mc}")

# Аналітичне обчислення інтегралу
result_analytical = (b**3 / 3) - (a**3 / 3)
print(f"Аналітичний інтеграл: {result_analytical}")

# Обчислення інтеграла за допомогою функції quad
result_quad, error = spi.quad(f, a, b)
print(f"Інтеграл з використанням scipy quad: {result_quad}")

# Порівняння результатів
print(f"Інтеграл методом Монте-Карло: {integral_mc}")
print(f"Аналітичний інтеграл: {result_analytical}")
print(f"Інтеграл з використанням scipy quad: {result_quad}")
