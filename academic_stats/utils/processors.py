from academic_stats.utils.countries import get_countries_as_set
import re
import unicodedata


def get_triples(it):
    """
    Accepts an iterators and returns i,i+1, i+2 entries

    Returns
    --------
    i,i+1, i+2
    i+1,i+2, i+3
    i, ..., None
    i, None, None

    Examples
    --------
    >>> [_ for _ in get_triples("ABC")]
    [('A', 'B', 'C'), ('B', 'C', None), ('C', None, None)]
    """
    first, second, third = None, None, None
    for idx, element in enumerate(it):
        first = element
        try:
            second = it[idx + 1]
        except:
            # couldn't find element two
            second = None
        try:
            third = it[idx + 2]
        except:
            # couldn't find third element
            third = None
        yield first, second, third


def affiliations_processor(affiliations: str):
    """
    Given a string with affiliations returns dictionary of countries: count of affiliations

    affiliations: str
            A string of affiliations separated by ;

    Returns
    -------
    List of affiliated countries
    """
    assert (
        type(affiliations) == str
    ), f"Affiliation must be a string, but is {type(affiliations)}"

    countries = []

    # affiliations could have multiple affiliations separated by ;
    affiliations = affiliations.strip().split(";")
    for affiliation in affiliations:
        # remove non alphabets
        country_set, str_to_country = get_countries_as_set()
        affiliation = re.sub("[^A-Za-z ]", "", affiliation)

        # is any word, two consecutive words, three consecutive words in country set ?
        words = affiliation.split(" ")
        for w1, w2, w3 in get_triples(words):
            if w1 in country_set:
                countries.append(str_to_country[w1])
                break
            elif w2 in country_set:
                countries.append(str_to_country[w2])
                break
            elif w3 in country_set:
                countries.append(str_to_country[w3])
                break
    return countries


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
    """
    # preprocess names
    name = strip_accents(name)
    name = " ".join(name.split())
    if len(name) == 0:
        # name string is empty nothing to process
        return ""

    name_split = name.split(" ")
    lastname = name_split[-1]
    first_and_initials = []
    for words in name_split[:-1]:
        first_and_initials.append(words[0].upper())
    return f"{''.join(first_and_initials)} {lastname}"


def strip_accents(s):
    return "".join(
        [c for c in unicodedata.normalize("NFD", s) if unicodedata.category(c) != "Mn"]
    )
