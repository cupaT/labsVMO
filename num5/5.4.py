import matplotlib.pyplot as plt

languages = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
popularity = [22.2, 17.6, 8.8, 8.0, 7.7, 6.7]

plt.figure(figsize=(6, 6))
bars = plt.bar(languages, popularity, color='blue')
plt.title('Popularity of Programming Language\nWorldwide, Oct 2017 compared to a year ago')
plt.ylabel('Popularity')
plt.grid(axis='y', color='red', linestyle='--', linewidth=0.5)

for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval + 0.3, f'{yval:.6f}', ha='center', va='bottom')

plt.show()