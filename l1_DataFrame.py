import pandas as pd

frame = pd.DataFrame({
    'country': ['Kazakhstan', 'Russia', 'Belarus', 'Ukraine'],
    'population': [17.04, 143.5, 9.5, 45.5],
    'square': [2724902, 17125191, 207600, 603628]})
print(frame)
print('\n')

print(frame['country'])
print('\n')

print(frame.columns)
print('\n')

print(frame.index)
print('\n')

frame1 = pd.DataFrame({
    'country': ['Kazakhstan', 'Russia', 'Belarus', 'Ukraine'],
    'population': [17.04, 143.5, 9.5, 45.5],
    'square': [2724902, 17125191, 207600, 603628]}, index=['KZ', 'RU', 'BY', 'UA'])
print(frame1)
print('\n')

frame2 = pd.DataFrame({
    'country': ['Kazakhstan', 'Russia', 'Belarus', 'Ukraine'],
    'population': [17.04, 143.5, 9.5, 45.5],
    'square': [2724902, 17125191, 207600, 603628]})
frame2.index = ['KZ', 'RU', 'BY', 'UA']
frame2.index.name = 'Country code'
print(frame2)
print('\n')

print(frame2['country'])
print('\n')

print(frame2.loc['KZ'])
print('\n')

print(frame2.iloc[0])
print('\n')

print(frame2.loc[['KZ', 'RU'], 'population'])
print('\n')

print(frame2.loc['KZ': 'BY', :])
print('\n')

print(frame2[frame2.population > 10][['country', 'square']])
print('\n')

frame2.reset_index()
print(frame2)
print('\n')

frame2['density'] = frame2['population'] / frame2['square'] * 1000000
print(frame2)
print('\n')

print(frame2.drop(['density'], axis='columns'))
print('\n')

del frame2['density']
print(frame2)
print('\n')

frame2 = frame2.reset_index()
frame2 = frame2.rename(columns={'Country code': 'country_code'}) 
print(frame2)
print('\n')

frame2.to_csv('coutry.csv')

frame3 = pd.read_csv('coutry.csv', sep=',')
print(frame3)
print('\n')

