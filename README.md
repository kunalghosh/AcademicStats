# AcademicStats
Given PubMed and Arxiv xml dumps, returns a list of countries sorted by the number of affiliated authors.

## Install

```bash
pip install git+https://github.com/kunalghosh/AcademicStats.git#egg=academic_stats
```

## Data
The Arxiv and PubMed data is stored in google drive. The link to the data can be found in the assignment homepage on [hackmd.io](hackmd.io/@wmvanvliet/S1QiaABZ9)

## Usage
Down the PubMed and Arxiv datasets. Each should be stored in a separate folder and contain one file per author.
```bash
$ python -m academic_stats --help
Usage: python -m academic_stats [OPTIONS]

  Console script for academic_stats.

Options:
  --pubmed PATH  Path to the pubmed directory with xml files.
  --arxiv PATH   Path to the arxiv directory with xml files.
  --help         Show this message and exit.
```

You can pass either `--pubmed`, `--arxiv` or both
```bash
$ python -m academic_stats --pubmed ~/Downloads/pubmed_and_arxiv_data/pubmed --arxiv ~/Downloads/pubmed_and_arxiv_data/arxiv
```

Sample output
```bash
$ python -m academic_stats --arxiv ~/Downloads/pubmed_and_arxiv_data/arxiv
China                       :   681
Italy                       :   504
Germany                     :   468
United States               :   448
France                      :   206
Spain                       :   193
...
```

We define an author type. It contains the name of the author and their affiliations.
```python
NamedTuple('Author','name countries')
	name: str
		Name of the author.
	countries: set
		Set of countries that the author is affiliated in.
```

```python
def affiliations_processor(affiliations: str):
	"""
	Given a string with affiliations returns dictionary of countries: count of affiliations

	affiliations: str
		A string of affiliations separated by ;
	
	Returns
	-------
	dict(country: str, count: int)
		Dictionary where keys are the countries that the author is affiliated to
		values correspond to the count of affiliations in that country.
```

Next we define a name processor
```python
def name_processor(name: str):
	"""
	Given a name as "Forename Initial Initial2 ... Lastname" returns a standardized name. 

	name: str
		Name as a single string
	
	Returns
	-------
	str
		Processed name which is a string with the following structure.
		"<Firstchar of forname><Firstchar of Initial1><Firstchar of Initial2><...> <Lastname without accents>"
```

We need two classes which would process `PubMed` and `Arxiv` xml files respectively

```python
class Arxiv:
	def __init__(self, path_to_dir):
		self.path = path_to_dir
		self.files = glob(f'{self.path}/*.xml')

	def __iter__(self):
		return self
	
	def __next__(self):
		"""
		Processes the next xml file and yields an author object
		"""
		for file in self.files:
			xml_data = self._get_xml_root(file)
			name = name_processor(_get_name(xml_data))
			countries = affiliations_processor(_get_affiliation(xml_data))
			yield Author(name, set(countries.keys()))
	
	def _get_name(xml_data: Elementree):
		pass
	
	def _get_affiliation(xml_data: Elementree):
		pass
```

Similar class for processing PubMed files. 
> TODO: Maybe abstract out the class implementations and just implement the `_get_name()` and `_get_affiliation()` in each

```python

class PubMed:
	def __init__(self, path_to_dir):
		self.path = path_to_dir
		self.files = glob(f'{self.path}/*.xml')

	def __iter__(self):
		return self

	def __next__(self):
		"""
		Processes the next xml file and yields an author object
		"""
		for file in self.files:
			xml_data = self._get_xml_root(file)
			authors = self._get_authors(xml_data)
			name = name_processor(_get_name(xml_data))
			countries = affiliations_processor(_get_affiliation(xml_data))
			yield Author(name, set(countries.keys()))

	def _get_xml_root(file: str):
		root = ET.parse.getroot(file)
		return root

	def _get_authors(xml_data: Elementree)
		author_list = xml_data.find('AuthorList')
		authors = author_list.findall('Author')
		return authors

	def _get_name(xml_data: Elementree):
		forename = xml_data.find('ForeName')
		initials = xml_data.find('Initials')
		lastname = xml_data.find('LastName')
		return f'{forname} {initials} {lastname}'

	def _get_affiliation(xml_data: Elementree):
		pass
```
