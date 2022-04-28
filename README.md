# AcademicStats
Given PubMed and Arxiv xml dumps, returns a summary

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
class PubMed:
	def __init__(self, path_to_pubmed_dir):
		self.path = path_to_pubmed_dir
		self.files = glob(f'{self.path}/*.xml')

	def __iter__(self):
		return self
	
	def __next__(self):
		"""
		Processes the next xml file and yields an author object
		"""
		for file in self.files:
			xml_data = self._process_xml(file)
			name = name_processor(_get_name(xml_data))
			countries = affiliations_processor(_get_affiliation(xml_data))
			yield Author(name, set(countries.keys()))
	
	def _get_name(xml_data: Elementree):
		pass
	
	def _get_affiliation(xml_data: Elementree):
		pass
```

Similar class for processing Arxiv files. 
> TODO: Maybe abstract out the class implementations and just implement the `_get_name()` and `_get_affiliation()` in each

```

