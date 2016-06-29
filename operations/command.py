#!/usr/bin/env python
from argparse import ArgumentParser
from setul_de_operatii import compute_sum, compute_prod

def process_sum():
	parser = ArgumentParser(description = "Compute sum of two numbers")
	
	parser.add_argument('x', type=int)
	parser.add_argument('y', type = int)
	
	arguments = parser.parse_args()

	print compute_sum(arguments.x, arguments.y)

def process_prod():
	parser = ArgumentParser(description = "Compute sum of two numbers")
	
	parser.add_argument('x', type=int)
	parser.add_argument('y', type = int)
	
	arguments = parser.parse_args()

	print compute_prod(arguments.x, arguments.y)

if __name__ == "__main__":
	process_sum()
	process_prod()
	
