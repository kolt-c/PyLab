import pandas as pd

ex_series = pd.Series([5, 6, 7, 8, 9, 10])

print(ex_series)
print('\n')

print(ex_series.index)
print('\n')

print(ex_series.values)
print('\n')

print(ex_series[4])
print('\n')

ex_series2 = pd.Series([5, 6, 7, 8, 9, 10], index=['a', 'b', 'c', 'd', 'e', 'f'])
print(ex_series2['f'])
print('\n')

print(ex_series2[['a', 'b', 'f']])
print('\n')

ex_series2[['a', 'b', 'f']] = 0
print(ex_series2)
print('\n')
      
print(ex_series2[ex_series2 > 0])
print('\n')

print(ex_series2[ex_series2 > 0] * 2)
print('\n')

ex_series3 = pd.Series({'a': 5, 'b': 6, 'c': 7, 'd': 8})
print(ex_series3)
print('\n')

ex_series3.name = 'numbers'
ex_series3.index.name = 'letters'
print(ex_series3)
print('\n')

ex_series3.index = ['A', 'B', 'C', 'D']
print(ex_series3)
print('\n')


