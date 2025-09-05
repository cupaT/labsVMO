import numpy as np


#2.1
a = np.array([0, 10, 20, 40, 60])
b = np.array([10, 30, 40])

common = np.intersect1d(a, b)
print(common)

#2.2
arr1 = np.array([10, 10, 20, 20, 30, 30])
unique1 = np.unique(arr1)
print(unique1)

arr2 = np.array([[1, 1], [2, 3]])
unique2 = np.unique(arr2)
print(unique2)

#2.3
arr_uniq = np.array([10, 10, 20, 10, 20, 20, 20, 30, 30, 50, 40, 40])
unique, counts = np.unique(arr_uniq, return_counts=True)

print(unique)
print(counts)

#2.4
arr_tile = np.array([1, 2, 3, 4])

print(np.tile(arr_tile, 1))
print(np.tile(arr_tile, 2))
print(np.tile(arr_tile, 3))

#2.5
arr1 = np.array([200., 300., np.nan, np.nan, np.nan, 700.])
filtered1 = arr1[~np.isnan(arr1)]
print(filtered1)

arr2 = np.array([[1., 2., 3.],
                 [np.nan, 0., np.nan],
                 [6., 7., np.nan]])
filtered2 = arr2[~np.isnan(arr2)]
print(filtered2)

#2.6
arr_sort = np.array([1., 7., 8., 2., 0.1, 3., 15., 2.5])
k = 4

smallest_k = np.sort(arr_sort)[:k]
print(smallest_k)

#2.7
arr = np.array([0.5, 1.8, 2.1, 3.5, 4.87, 5.13, 6.49])
value = 3.09066280756759

closest = arr[np.abs(arr - value).argmin()]
print(closest)

#2.8
a = np.array(['Python', 'PHP'])
b = np.array(['Java', 'C ++'])

result = np.char.add(a, ' ')
result = np.char.add(result, b)

print(result)

#2.9
arr = np.array(['Python', 'PHP', 'JS', ' examples', 'html'])

count_P = np.char.count(arr, 'P')
print(count_P)

#2.10
coeffs_a = [1, -4, 7]
roots_a = np.roots(coeffs_a)
print("x^2 - 4x + 7:", roots_a)

coeffs_b = [1, -11, 9, 11, -10]
roots_b = np.roots(coeffs_b)
print("x^4 - 11x^3 + 9x^2 + 11x - 10:", roots_b)


