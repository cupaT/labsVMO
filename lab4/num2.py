import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt

# 1. Загрузка и изучение датасета
df = pd.read_csv('howpop_train.csv')
df = df.drop(columns=[col for col in df.columns if 'Unnamed' in col])
# Исправление типов данных для числовых столбцов
cols_to_float = [
    'views', 'votes_plus', 'votes_minus', 'content_len',
    'views_lognorm', 'favs_lognorm', 'comments_lognorm'
]
for col in cols_to_float:
    if col in df.columns:
        df[col] = df[col].astype(str).str.replace(',', '.', regex=False)
        df[col] = pd.to_numeric(df[col], errors='coerce')

print("\nПервые строки датафрейма:")
print(df.head())

print("\nИнформация о столбцах:")
print(df.info())

print("\nНазвания столбцов:")
print(df.columns)

# 2. Удаление столбцов, заканчивающихся на _lognorm
df.drop(
    filter(lambda c: c.endswith("_lognorm"), df.columns),
    axis=1,
    inplace=True,
)

print("\nНазвания столбцов после удаления _lognorm:")
print(df.columns)

# 3. Преобразование published к типу datetime
df["published"] = pd.to_datetime(df.published, yearfirst=True)

print("\nПервые значения столбца published после преобразования:")
print(df["published"].head())

# 4. Создание новых столбцов на основе времени публикации
df["year"] = [d.year for d in df.published]
df["month"] = [d.month for d in df.published]
df["dayofweek"] = [d.isoweekday() for d in df.published]
df["hour"] = [d.hour for d in df.published]

print("\nПервые значения новых столбцов year, month, dayofweek, hour:")
print(df[["year", "month", "dayofweek", "hour"]].head())

# 5. Визуализация: в каком месяце и году было больше всего публикаций
sb.countplot(x="month", hue="year", data=df)
plt.title("Число публикаций по месяцам и годам")
plt.xlabel("Месяц")
plt.ylabel("Число публикаций")
plt.legend(title="Год")
print("\nГрафик числа публикаций по месяцам и годам построен.")
plt.show()

# 6. Визуализация: число публикаций по дням недели с hue по году
sb.countplot(x="dayofweek", hue="year", data=df)
plt.title("Число публикаций по дням недели с разбивкой по годам")
plt.xlabel("День недели (1=Пн, 7=Вс)")
plt.ylabel("Число публикаций")
plt.legend(title="Год")
print("\nГрафик числа публикаций по дням недели построен.")
plt.show()

# 7. Визуальный анализ утверждений (barplot)

# 7.1 Средние просмотры по часам публикации
sb.barplot(x='hour', y='views', data=df, estimator='mean')
plt.title("Средние просмотры по часам публикации")
plt.xlabel("Час публикации")
plt.ylabel("Среднее число просмотров")
plt.show()
print("\nBarplot: средние просмотры по часам публикации построен.")

# 7.2 Среднее число комментариев по часам публикации
sb.barplot(x='hour', y='comments', data=df, estimator='mean')
plt.title("Среднее число комментариев по часам публикации")
plt.xlabel("Час публикации")
plt.ylabel("Среднее число комментариев")
plt.show()
print("\nBarplot: среднее число комментариев по часам публикации построен.")

# 7.4 Среднее число комментариев на Geektimes по часам публикации
if 'domain' in df.columns:
    sb.barplot(x='hour', y='comments', data=df[df['domain'] == 'geektimes.ru'], estimator='mean')
    plt.title("Среднее число комментариев на Geektimes по часам публикации")
    plt.xlabel("Час публикации")
    plt.ylabel("Среднее число комментариев")
    plt.show()
    print("\nBarplot: среднее число комментариев на Geektimes по часам публикации построен.")

# 7.5 Среднее число комментариев на Хабре по часам публикации
if 'domain' in df.columns:
    sb.barplot(x='hour', y='comments', data=df[df['domain'] == 'habrahabr.ru'], estimator='mean')
    plt.title("Среднее число комментариев на Хабре по часам публикации")
    plt.xlabel("Час публикации")
    plt.ylabel("Среднее число комментариев")
    plt.show()
    print("\nBarplot: среднее число комментариев на Хабре по часам публикации построен.")

# 8. Визуальный анализ: кого из топ-20 авторов чаще всего минусуют

# Найдём топ-20 авторов по количеству публикаций
top_authors = df['author'].value_counts().head(20).index.tolist()
df_top_authors = df[df['author'].isin(top_authors)]

# Barplot по среднему количеству минусов
plt.figure(figsize=(14, 6))
sb.barplot(x='author', y='votes_minus', data=df_top_authors, estimator='mean')
plt.xticks(rotation=45)
plt.title("Среднее количество минусов по топ-20 авторам")
plt.xlabel("Автор")
plt.ylabel("Среднее количество минусов")
plt.tight_layout()
plt.show()
print("\nBarplot: среднее количество минусов по топ-20 авторам построен.")

# 9. Сравнение суббот и понедельников по времени публикации
plt.figure(figsize=(10,6))
sb.histplot(df[df['dayofweek'] == 1]['hour'], color='salmon', label='Понедельник', kde=False, stat='count', binwidth=1)
sb.histplot(df[df['dayofweek'] == 6]['hour'], color='skyblue', label='Суббота', kde=False, stat='count', binwidth=1)
plt.legend()
plt.title("Сравнение публикационной активности по часам: суббота vs понедельник")
plt.xlabel("Час публикации")
plt.ylabel("Число публикаций")
plt.show()
print("\nГрафик сравнения субботы и понедельника построен.")