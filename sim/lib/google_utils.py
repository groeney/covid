import csv
from typing import List

def write_tuples_to_file(tuples: List, file_path: str, tuple_type) -> None:
	"""Takes in a list of namedtuples and writes them to file.

	Args:
		tuples: list of namedtuple objects of type `tuple_type`
		file_path: should be a qualified file path + name + .csv. 
			e.g. ./relative/path/to/file.csv.

	Example:


	"""
	with open(file_path, 'w') as f_out:
		writer = csv.writer(f_out)
		writer.writerow(list(tuple_type._fields))
		for gc in tuples:
			writer.writerow(gc)

def write_dict_with_eq_length_values(d: dict, file_path: str, l: int) -> None:
	"""Takes in a dictionary (1, N) ndarray values and writes them to CSV.

	Args:
		d: dictionary of equal length (1,N) ndarray values.
	"""
	with open(file_path, 'w') as f_out:
		write = csv.writer(f_out)
		write.writerow(list(d.keys()))
		for row in d.values():
			row = row.flatten()
			assert(len(row) == l)
			write.writerow(row)
