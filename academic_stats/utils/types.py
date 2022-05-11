from collections import namedtuple

Author = namedtuple("Author", "name countries")
"""
	name: str
		Name of the author.
	countries: set
		Set of countries that the author is affiliated in.
"""

Publication = namedtuple("Publication", "title authorlist")
"""
    title: str
        Title of the Publication
    author_list: set of Author(s)
        Set of Authors who have co-authored the paper
"""
