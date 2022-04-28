from collections import namedtuple

Author = namedtuple("Author", "name countries")
"""
	name: str
		Name of the author.
	countries: set
		Set of countries that the author is affiliated in.
"""
