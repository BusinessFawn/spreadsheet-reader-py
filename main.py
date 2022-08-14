import argparse
from spreadsheet_reader.utils.xlsx_toucher import XlsxToucher


def do_it(parser):
	person_path = parser.path
	score_path = parser.path
	output_path = parser.path
	if person_arg := parser.person_path:
		person_path = person_arg
	if score_arg := parser.score_path:
		score_path = score_arg
	if output_arg := parser.output_path:
		output_path = output_arg

	if not all((person_path, score_path, output_path)):
		raise ValueError("Required input '--path' or all of ('--person-pat', '--score-path', '--output-path') is required")
	print(person_path, score_path, output_path)

	person_ss = XlsxToucher(person_path, XlsxToucher.PERSON_PATTERN)
	score_ss = XlsxToucher(score_path, XlsxToucher.SCORE_PATTERN)

	print(f'person shape {person_ss.get_dataframe().info()}')
	print(f'score shape {score_ss.get_dataframe().info()}')


if __name__ == '__main__':
	arg_parser = argparse.ArgumentParser()

	arg_parser.add_argument(
		'-p', '--path',
		help='Relative path to the directory holding the person and score data. Output will be saved as all_together_<datetime>.xlsx. '
			 'File names should end with *_person.xlsx and *_score.xlsx respectively. Collisions of the "ID" field in the *_person.xlsx will cause the program to fail.',
		type=str
	)
	arg_parser.add_argument(
		'-pp', '--person-path',
		help='Relative path to your directory holding the person data. File names should end with *_person.xlsx. Collisions of the "ID" field will cause the program to fail.',
		type=str
	)
	arg_parser.add_argument(
		'-sp', '--score-path',
		help='Relative path to your directory holding the score data. File names should end with *_score.xlsx.',
		type=str
	)
	arg_parser.add_argument(
		'-op', '--output-path',
		help='Relative path to the directory to save the output. Output will be saved as all_together_<datetime>.xlsx.',
		type=str
	)
	args = arg_parser.parse_args()
	do_it(args)
