import pandas as pd

# 1. Загрузка данных
columns = [
    "index", "year", "month", "day",
    "min_t", "average_t", "max_t", "rainfall"
]
df = pd.read_csv(
    "Kemerovo.txt",
    sep=";",
    names=columns,
    header=None,
    skipinitialspace=True
)

# 2. Удаление столбца index
df = df.drop(columns=["index"])

# 3. Анализ пропущенных значений
print("\nКоличество пропущенных значений по столбцам:")
print(df.isnull().sum())
max_null_col = df.isnull().sum().idxmax()
print(f"\nБольше всего пропущенных значений в столбце: {max_null_col}")

# 4. Год с наибольшим количеством пропусков
df['null_count'] = df.isnull().sum(axis=1)
year_with_most_nulls = df.groupby('year')['null_count'].sum().idxmax()
print(f"\nВ данных за {int(year_with_most_nulls)} год больше всего пропусков.")
df = df.drop(columns=['null_count'])

# 5. Объединяем год, месяц, день в столбец "Дата"
df['Дата'] = pd.to_datetime(
    df[['year', 'month', 'day']],
    errors='coerce'
)
print("\nПример преобразования даты:")
print(df[['year', 'month', 'day', 'Дата']].head())

# 6. Размах температур и количество предшествующих дней без осадков
df['temp_range'] = df['max_t'] - df['min_t']

# Подсчёт количества подряд идущих дней без осадков до каждого дня
no_rain_days = []
count = 0
for rain in df['rainfall']:
    if pd.isnull(rain) or rain == 0.0:
        no_rain_days.append(count)
        count += 1
    else:
        no_rain_days.append(count)
        count = 0
df['no_rain_days_before'] = no_rain_days

# 7. Самый длинный период засухи
max_drought = max(no_rain_days)
print(f"\nСамый длинный период засухи: {max_drought} дней подряд без осадков.")

# 8. Среднегодовая температура и сумма осадков по годам
mean_temp_by_year = df.groupby('year')['average_t'].mean()
total_rain_by_year = df.groupby('year')['rainfall'].sum()

warmest_year = mean_temp_by_year.idxmax()
coldest_year = mean_temp_by_year.idxmin()
most_rain_year = total_rain_by_year.idxmax()
least_rain_year = total_rain_by_year.idxmin()

print("\nСреднегодовая температура по годам:")
print(mean_temp_by_year)
print("\nОбщее количество осадков по годам:")
print(total_rain_by_year)
print(f"\nСамый тёплый год: {warmest_year}")
print(f"Самый холодный год: {coldest_year}")
print(f"Больше всего осадков в году: {most_rain_year}")
print(f"Меньше всего осадков в году: {least_rain_year}")

# 9. Фильтрация по условиям
cold_days = df[df['average_t'] < -30]
hot_dry_days = df[(df['average_t'] > 27) & (df['no_rain_days_before'] > 3)]

print("\nНаблюдения со средней температурой ниже -30:")
print(cold_days[['Дата', 'average_t']])
print("\nНаблюдения со средней температурой выше 27 и количеством дней без осадков больше 3:")
print(hot_dry_days[['Дата', 'average_t', 'no_rain_days_before']])