import numpy as np

a11 = float(input("Введите a11: "))
a12 = float(input("Введите a12: "))
b1 = float(input("Введите b1: "))
a21 = float(input("Введите a21: "))
a22 = float(input("Введите a22: "))
b2 = float(input("Введите b2: "))

A = np.array([[a11, a12],
              [a21, a22]])
B = np.array([b1, b2])

det = np.linalg.det(A)

if np.isclose(det, 0):
    print("Система не имеет единственного решения (определитель равен 0).")
else:
    solution = np.linalg.solve(A, B)
    print(f"Решение системы: x = {solution[0]}, y = {solution[1]}")