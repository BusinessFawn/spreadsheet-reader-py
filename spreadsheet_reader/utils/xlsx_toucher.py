import glob

import pandas as pd


class XlsxToucher:
	PERSON_PATTERN = '*_person.xlsx'
	SCORE_PATTERN = '*_score.xlsx'

	def __init__(self, path_to_files: str, matching_pattern: str):
		self.df = pd.DataFrame()
		full_path = path_to_files
		if not path_to_files.endswith('/'):
			full_path = f'{path_to_files}/'
		full_path = f"{full_path}{matching_pattern}"
		list_of_files = glob.glob(full_path)
		print(list_of_files)
		for f in list_of_files:
			print(f)
			df = pd.read_excel(f)
			print(df.info())

	def get_dataframe(self):
		return self.df
