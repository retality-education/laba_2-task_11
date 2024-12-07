# -*- coding: cp1251 -*-
import matplotlib.pyplot as plt
import numpy as np

# Настройка параметров для графиков
colors = ['#A9A9A9', '#808080']  # Темно-серый и средний серый
linestyles = ['dashdot', 'dashdot']  # Штрих-пунктир
linewidths = [2, 2]
grids = [False, True]  # Сетка для графика A отсутствует, для графика B присутствует
grid_color = 'lightskyblue'  # Цвет сетки

# Окно
plt.figure("Построение графиков A и B", figsize=(12, 10))

# График A: |y| = x * sqrt(2 + 4*x ± 2*sqrt(1 - 4*x)) / (1 -+ sqrt(1-4x))
x_A = np.arange(-2, 0.25, 0.001)
y_A_plus = x_A * np.sqrt(2 + 4*x_A + 2*np.sqrt(1 - 4*x_A)) / (1 - np.sqrt(1 - 4*x_A))
y_A_minus = x_A * np.sqrt(2 + 4*x_A - 2*np.sqrt(1 - 4*x_A)) / (1 + np.sqrt(1 - 4*x_A))

# График A занимает область (0,0) до (1,1)
plt.subplot2grid((2, 3), (0, 0), rowspan=3)  
plt.plot(x_A, y_A_plus, color=colors[0], linestyle =linestyles[0], linewidth=linewidths[0], label='y+')
plt.plot(x_A, y_A_minus, color=colors[0], linestyle=linestyles[0], linewidth=linewidths[0], label='y-')
plt.plot(x_A, -y_A_plus, color=colors[0], linestyle=linestyles[0], linewidth=linewidths[0], label='y+')
plt.plot(x_A, -y_A_minus, color=colors[0], linestyle=linestyles[0], linewidth=linewidths[0], label='y-')
plt.title('График A: |y| = x * sqrt(2 + 4*x ± 2*sqrt(1 - 4*x)) / (1 -+ sqrt(1-4x))')
plt.xlabel('x')
plt.ylabel('y')
plt.axhline(0, color='black', lw=0.5, ls='dashdot')
plt.axvline(0, color='black', lw=0.5, ls='dashdot')

# Установка пределов для оси y
plt.ylim(-4, 4)  # Увеличиваем диапазон оси y
plt.xlim(-3, 1)

# Убираем сетку для графика A
if grids[0]:
    plt.grid(color=grid_color)

plt.legend()

# График B: Параметрические уравнения
t_B = np.linspace(0, 2 * np.pi, 400)

x_B = np.sin(9 * t_B)
y_B = np.sin(8 * t_B)

# График B занимает область (0,1) до (1,2)
plt.subplot2grid((2, 3), (0, 2), rowspan=3)  
plt.plot(x_B, y_B, color=colors[1], linestyle=linestyles[1], linewidth=linewidths[1])
plt.title('График B: Параметрические уравнения x = sin(9t), y = sin(8t)')
plt.xlabel('x')
plt.ylabel('y')
plt.axhline(0, color='black', lw=0.5, ls='dashdot')
plt.axvline(0, color='black', lw=0.5, ls='dashdot')
plt.ylim(-2.5, 2.5)
plt.xlim(-1.5, 1.5)

# Добавляем сетку для графика B
if grids[1]:
    plt.grid(color=grid_color)

plt.tight_layout()
plt.show()
