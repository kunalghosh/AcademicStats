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
    """
    print(f"Affiliations {affiliations}")
    return affiliations


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
    name = strip_accents(name)
    name_split = name.strip().split(" ")
    lastname = name_split[-1]
    first_and_initials = []
    for words in name_split[:-1]:
        first_and_initials.append(words[0].upper())
    return f"{''.join(first_and_initials)} {lastname}"


def strip_accents(s):
    return "".join(
        [c for c in unicodedata.normalize("NFD", s) if unicodedata.category(c) != "Mn"]
    )
