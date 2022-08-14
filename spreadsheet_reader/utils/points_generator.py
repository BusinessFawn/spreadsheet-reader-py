from random import randint
from datetime import date, timedelta
import pandas as pd


def do_it():
	dates = []
	for i in range(500):
		point_dict = {
			"ID": randint(1, 10),
			"Date": date.today() - timedelta(days=randint(20,500)),
			"Points": randint(15, 300)
		}
		dates.append(point_dict)

	df = pd.DataFrame(dates)

	print(df)
	df.to_excel('../../tests/data/2022-08-01_score.xlsx')


if __name__ == '__main__':
	do_it()