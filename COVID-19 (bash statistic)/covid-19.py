import requests
import pandas as pd
from datetime import date


url = "https://www.statista.com/statistics/1102935/coronavirus-cases-by-region-in-russia/"
html = requests.get(url).content

df = pd.read_html(html)[0]
df.set_axis(['Регион', 'Умерло', 'Выздоровело', 'Активные', 'Выявлено'], axis = 1, inplace = True)

print('---------ДАННЫЕ НА', date.today().strftime("%d.%m.%Y")+'----------')

print(df)

print("\n ---------СТАТИСТИКА------------")
print(f"Всего выявленных случаев: {df['Выявлено'].sum()} \nВсего умерло: {df['Умерло'].sum()} \nВсего выздоровело: {df['Выздоровело'].sum()}")


stats_region = input('\nХотите узнать статистику в выбранном регионе? [y/n]: ')

if stats_region.lower() == 'y' or stats_region.lower() == 'д':
	print("\n---------УЗНАТЬ СТАТИСТИКУ В РЕГИОНЕ---------")
	while True:
		city = input('\nВведите город: ')
		if len(df[df['Регион'] == city]) > 0:
			print(df[df['Регион'] == city])
			break
		elif city.lower() == "exit":
			break
		else:
			print('Регион не найден')
