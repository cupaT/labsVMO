import pandas as pd

# 1. Загрузка и очистка данных
polit = pd.read_csv(
    'polit.csv',
    sep=';',
    decimal=',',
    na_values=['', ' '])
print(polit.head())
polit = polit.dropna()
print("1. Датафрейм после удаления пропущенных значений:\n", polit.head())

# 2. Страны с индексом Freedom House (fh09) выше 5
fh_above_5 = polit[polit['fh09'] > 5]
print("\n2. Страны с fh09 > 5:\n", fh_above_5[['ctry', 'fh09']])

# 3. Страны Африки с долей женщин в парламенте выше 30%
afri_women30 = polit[(polit['afri'] == 1) & (polit['fparl08'] > 30)]
print("\n3. Африканские страны с fparl08 > 30:\n", afri_women30[['ctry', 'afri', 'fparl08']])

# 4. Страны Африки или Латинской Америки с polity09 >= 8
afri_lati_polity = polit[((polit['afri'] == 1) | (polit['lati'] == 1)) & (polit['polity09'] >= 8)]
print("\n4. Африка или Латинская Америка с polity09 >= 8:\n", afri_lati_polity[['ctry', 'afri', 'lati', 'polity09']])

# 5. Добавление столбца с округлением corr0509
polit['corr_round'] = polit['corr0509'].round(2)
print("\n5. Добавлен столбец corr_round:\n", polit[['ctry', 'corr0509', 'corr_round']].head())

# 6. Добавление статуса свободы страны по fh09
def get_fh_status(fh09):
    if fh09 <= 2.5:
        return 'free'
    elif fh09 <= 5.5:
        return 'partly free'
    else:
        return 'not free'

polit['fh_status'] = polit['fh09'].apply(get_fh_status)
print("\n6. Добавлен столбец fh_status:\n", polit[['ctry', 'fh09', 'fh_status']].head())

# 7. Группировка по fh_status: min, mean, max gini по группам
gini_stats = polit.groupby('fh_status')['gini'].agg(['min', 'mean', 'max'])
print("\n7. gini по группам fh_status:\n", gini_stats)

# 8. Сохранение строк по fh_status в отдельные csv
for status in polit['fh_status'].unique():
    polit[polit['fh_status'] == status].to_csv(f"polit_{status}.csv", index=False)
print("\n8. CSV-файлы по группам fh_status сохранены: polit_free.csv, polit_partly free.csv, polit_not free.csv")