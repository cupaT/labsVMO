import kagglehub
import pandas as pd
import os

# Загрузка датасетов
vg_dir = kagglehub.dataset_download("gregorut/videogamesales")
vg_path = os.path.join(vg_dir, "vgsales.csv")
vg_df = pd.read_csv(vg_path)
print(vg_df.head())

meta_dir = kagglehub.dataset_download("skateddu/metacritic-all-time-games-stats")
meta_path = os.path.join(meta_dir, "metacritic_games.csv")
meta_df = pd.read_csv(meta_path)
print(meta_df.head())

# 1. Все доступные платформы
platforms = vg_df['Platform'].dropna().unique()
print("1. Платформы, на которых выходила хотя бы одна игра:")
print(sorted(platforms))

# 2. Объединение с добавлением рейтинга
vg_df['Name_lower'] = vg_df['Name'].astype(str).str.lower().str.strip()
meta_df['name_lower'] = meta_df['name'].astype(str).str.lower().str.strip()
merged_df = pd.merge(
    vg_df,
    meta_df[['name_lower', 'rating']],
    left_on='Name_lower',
    right_on='name_lower',
    how='left'
)
merged_df = merged_df.rename(columns={'rating': 'metacritic_rating'})
print("\n2. Пример объединения с добавлением рейтинга (metacritic_rating):")
print(merged_df[['Name', 'metacritic_rating']].head())

# 3. Игры с рейтингом "M" и годом выпуска не ранее 2012 года
filtered_df = merged_df[
    (merged_df['metacritic_rating'] == "M") &
    (merged_df['Year'].fillna(0).astype(int) >= 2012)
]
print("\n3. Игры с рейтингом 'M' и годом выпуска не ранее 2012 года:")
print(filtered_df[['Name', 'Year', 'metacritic_rating']].drop_duplicates().head(10))

# 4. Описательные статистики для полученного списка
print("\n4. Описательные статистики для отфильтрованных игр (rating='M', Year>=2012):")
print(filtered_df.describe(include='all'))

# 5. Жанры с >=3 разными гласными и количеством игр
def count_distinct_vowels(s):
    return len(set([v for v in s.lower() if v in 'aeiou']))

genre_counts = merged_df['Genre'].value_counts()
genres_with_vowels = [genre for genre in genre_counts.index if count_distinct_vowels(str(genre)) >= 3]
print("\n5. Жанры с >=3 разными гласными и количеством игр:")
for genre in genres_with_vowels:
    print(f"{genre} - {genre_counts[genre]}")
