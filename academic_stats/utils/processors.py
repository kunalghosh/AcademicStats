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
    return name
