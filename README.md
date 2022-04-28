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
	Given a string with affiliations returns the corresponding countries and count of affiliations in each country.

	affiliations: str
		A string of affiliations separated by ;
	
	Returns
	-------
	dict(country: str, count: int)
		Dictionary where keys are the countries that the author is affiliated to
		values correspond to the count of affiliations in that country.
```

Next we define a name processor
```
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

We need two classes which would process PubMed and Arxiv xml files respectively
