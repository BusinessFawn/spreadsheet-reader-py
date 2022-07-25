import pandas as pd
import glob

class XlsxToucher:

	def __init__(self, path_to_files: str, matching_pattern: str):
		df = pd.DataFrame()
		list_of_files = glob.glob(glob.escape(path_to_files) + f"/{matching_pattern}")
		for f in list_of_files:
			df.concat(pd.read_csv(path_to_files))