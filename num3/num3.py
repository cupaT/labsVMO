import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 1. Загрузите случайную выборку из этого набора
filename = "la-crimes-sample.csv"
df = pd.read_csv(filename)
print("1. df:\n", df.head())

# 2. Сколько строк и столбцов в таблице?
num_rows, num_cols = df.shape
print("\n2.\nЧисло строк:", num_rows)
print("Число столбцов:", num_cols)

# 3. Названия столбцов и типы данных
columns = df.columns.tolist()
dtypes = df.dtypes
print("\n3.\nНазвания столбцов:")
print(columns)
print("\nТипы данных столбцов:")
print(dtypes)

# 4. Количество уникальных значений в каждом столбце
unique_counts = df.nunique()
print("\n4.\nКоличество уникальных значений в каждом столбце:")
print(unique_counts)

# 5. Количество пропущенных значений в каждом столбце
missing_counts = df.isnull().sum()
print("\n5. Количество пропущенных значений в каждом столбце:")
print(missing_counts)

# 6. Верно ли, что женщины чаще оказываются жертвами по сравнению с мужчинами?
victim_sex_counts = df['Victim Sex'].value_counts(dropna=True)
more_female_victims = victim_sex_counts.get('F', 0) > victim_sex_counts.get('M', 0)
print("\n6.\nКоличество жертв по полу:")
print(victim_sex_counts)
if more_female_victims:
    print("Женщин-жертв больше, чем мужчин.")
else:
    print("Мужчин-жертв больше, чем женщин (или равное число).")

# 7. 10 самых распространённых преступлений в Лос-Анджелесе
top_10_crimes = df['Crime Code Description'].value_counts().head(10)
top_10_crimes.index = top_10_crimes.index.str.slice(0, 15) + '...'
print("\n7. 10 самых распространённых преступлений:", top_10_crimes)
plt.figure(figsize=(14, 7))
top_10_crimes.plot(kind='bar')
plt.title('10 самых распространённых преступлений в Лос-Анджелесе')
plt.xlabel('Преступление')
plt.ylabel('Количество')
plt.tight_layout()
plt.show()

# 8. От каких преступлений чаще страдают женщины, а от каких мужчины?
crime_sex = df.pivot_table(index='Crime Code Description', columns='Victim Sex', aggfunc='size', fill_value=0)
crime_sex['victim_group'] = np.where(crime_sex.get('F', 0) > crime_sex.get('M', 0), 'Женщины', 'Мужчины')
female_majority_crimes = crime_sex[crime_sex['victim_group'] == 'Женщины'].sort_values('F', ascending=False).head(5)
male_majority_crimes = crime_sex[crime_sex['victim_group'] == 'Мужчины'].sort_values('M', ascending=False).head(5)
print("\n8.\nТоп-5 преступлений, где чаще жертвами становятся женщины:")
print(female_majority_crimes[['F', 'M']])
print("\nТоп-5 преступлений, где чаще жертвами становятся мужчины:")
print(male_majority_crimes[['M', 'F']])

# 9. Люди какого происхождения чаще всего подвергаются преступлениям?
descent_counts = df['Victim Descent'].value_counts()
most_common_descent = descent_counts.idxmax()
print("\n9.\nРаспределение по происхождению жертв (Victim Descent):")
print(descent_counts)
print("\nЧаще всего подвергаются преступлениям:", most_common_descent)

# 10. Отсортировать районы по количеству преступлений и построить график
area_counts = df['Area Name'].value_counts()
print("\n10.\nРайоны по количеству преступлений:")
print(area_counts)
print("\nСамый опасный район:", area_counts.idxmax())
print("\nСамый безопасный район:", area_counts.idxmin())
plt.figure(figsize=(12, 6))
area_counts.plot(kind='bar')
plt.title('Количество преступлений по районам Лос-Анджелеса')
plt.xlabel('Район')
plt.ylabel('Количество преступлений')
plt.tight_layout()
plt.show()