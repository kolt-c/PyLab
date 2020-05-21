import pandas as pd
import matplotlib

frameTitanic = pd.read_csv('titanic.csv')
print(frameTitanic.head())
print('\n')

print(frameTitanic.groupby(['Sex', 'Survived'])['PassengerID'].count())
print('\n')

print(frameTitanic.groupby(['PClass', 'Survived'])['PassengerID'].count())
print('\n')

svod_table = frameTitanic.pivot_table(index=['Sex'], columns=['PClass'], values='Name', aggfunc='count')
print(svod_table)
print('\n')

print(svod_table.loc['female', ['1st', '2nd', '3rd']])
print('\n')

frameApple = pd.read_csv('apple.csv', index_col='Date', parse_dates=True)
frameApple = frameApple.sort_index()
print(frameApple.info())
print('\n')

print(frameApple.loc['2012-Feb', 'Close'].mean())
print('\n')

print(frameApple.loc['2012-Feb': '2015-Feb', 'Close'].mean())
print('\n')

print(frameApple.resample('W')['Close'].mean())
print('\n')

sample = frameApple.loc['2012-Feb': '2017-Feb', ['Close']]
sample.plot()
matplotlib.pyplot.show()
