import numpy as np

# 1.1
arr = np.array([1, 7, 13, 105])
print("Исходный массив:", arr)

print("Массив занимает", arr.nbytes, "байта")

np.savetxt('array.txt', arr, fmt='%d')
print("Массив сохранён в 'array.txt' (текстовый файл)")

arr.tofile('array.bin')
print("Массив сохранён в 'array.bin' (бинарный файл)")

arr_txt_loaded = np.loadtxt('array.txt', dtype=int)
print("array.txt:", arr_txt_loaded)

arr_bin_loaded = np.fromfile('array.bin', dtype=int)
print("array.bin:", arr_bin_loaded)

# 1.2
zeros = np.zeros(10, dtype=int)
ones = np.ones(10, dtype=int)
fives = np.full(10, 5, dtype=int)

print("Массив из 10 нулей:",  zeros)
print("Массив из 10 единиц:", ones)
print("Массив из 10 пятерок:", fives)

# 1.3
arr_30 = np.arange(30, 71, 2)
print("Массив последовательности четных целых чисел от 30 до 70:", arr_30)

# 1.4
arr_50 = np.linspace(5, 50, 10, dtype=int)
print("Массив из 10 элементов со значениями, равномерно распределенными между 5 и 50:", arr_50)

# 1.5
arr_3x3x3 = np.random.randint(1, 101, (3, 3, 3))
print("Массив 3x3x3 из 27 случайных чисел в диапазоне от 1 до 100:\n", arr_3x3x3)

# 1.6
arr_3x4 = np.random.randint(30, 42, (3, 4))
print("Массив 3х4, заполненной значениями от 30 до 4:\n", arr_3x4)

# 1.7
arr_10x10 =np.zeros((10, 10), dtype=int)
arr_10x10[0, :] = 1
arr_10x10[-1, :] = 1
arr_10x10[:, 0] = 1
arr_10x10[:, -1] = 1
print("Массив 10x10, в котором элементы на границах равны 1, а внутри 0:\n", arr_10x10)

# 1.8
arr_5x5 = np.zeros((5, 5), dtype=int)
np.fill_diagonal(arr_5x5, [1, 2, 3, 4, 5])
print("Массив 5x5 из нулей с элементами на главной диагонали равными 1, 2, 3, 4, 5:\n", arr_5x5)

# 1.9

arr_4x4 = np.indices((4, 4)).sum(axis=0) % 2
print("Массив 4x4, в котором 0 и 1 расположены в шахматном порядке, с нулями на главной диагонали:\n", arr_4x4)

# 1.10
dates = np.arange('2017-03-01', '2017-04-01', dtype='datetime64[D]')
print("Массив, заполненный всеми днями марта 2017 года:", dates)
