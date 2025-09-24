import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Исходные данные
data = [
    ["Вжик", "Zipper the Fly", "fly", "0.7"],
    ["Гайка", "Gadget Hackwrench", "mouse", None],
    ["Дейл", "Dale", "chipmunk", "1"],
    ["Рокфор", "Monterey Jack", "mouse", "0.8"],
    ["Чип", "Chip", "chipmunk", "0.2"]
]

# 1. Создание датафрейма
df = pd.DataFrame(data)
print("1. df:\n", df)

# 1. Проверяем, что последний столбец числовой, если нет — приводим к float
df[3] = pd.to_numeric(df[3], errors='coerce')

# 2. Число строк датафрейма
num_rows = len(df)
print("\n2. Число строк:", num_rows)

# 3. Число заполненных (не NaN) ячеек в последнем столбце
non_nan_cheer = df[3].count()
print("\n3. Число заполненных в 'cheer':", non_nan_cheer)

# 4. Значение на пересечении третьей строки и второго столбца (индексация с нуля)
cell_3_2 = df.iloc[2, 1]
print("\n4. Значение на пересечении 3-й строки и 2-го столбца:", cell_3_2)

# 5. Сохраняем в df1 строки 2–4 (включительно) и столбцы 1–3 (включительно)
df1 = df.iloc[1:4, 0:3]
print("\n5. df1:\n", df1)

# 6. Присваиваем новые имена столбцам
df.columns = ['ru_name', 'en_name', 'class', 'cheer']

# 7. Добавляем столбец logcheer (логарифм по основанию e)
df['logcheer'] = np.log(df['cheer'])
print("\n6-7. df:\n", df)

# 8. Уникальные значения столбца class и их частоты
x = df['class'].unique()
y = df['class'].value_counts().reindex(x).values
print("\n8.\nx:", x)
print("y:", y)

# Столбиковая диаграмма (barplot)
plt.figure(figsize=(10,6))
plt.bar(x, y)
plt.title('Частоты значений class')
plt.xlabel('class')
plt.ylabel('Частота')
plt.show()