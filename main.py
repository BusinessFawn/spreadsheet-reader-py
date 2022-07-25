import argparse


def do_it():
	print('hello!')


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
	arg_parser.parse_args()
	do_it()
