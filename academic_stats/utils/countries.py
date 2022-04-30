from functools import lru_cache
import pandas as pd
import pkgutil
import io


@lru_cache(maxsize=1)
def get_countries_as_set(fpath=pkgutil.get_data(__name__, "/AltCountries.csv").decode()):
    """
    Given a csv file with countries returns a set of strings from each word in the file
    """
    country_set = []
    str_to_country = None

    countries = pd.read_csv(io.StringIO(fpath))

    # get a dictionary of 'string' : 'Country Name'
    str_to_country = {}
    for tletters, name in zip(countries["3Letter"], countries["Name"]):
        for tletter in tletters.split(" "):
            # some countries have multiple three letter codes
            str_to_country[tletter] = name

    for alternatives, name in zip(countries["Alternatives"], countries["Name"]):
        for alt in alternatives.split("\t"):
            str_to_country[alt] = name

    str_to_country.update(dict(zip(countries["Name"], countries["Name"])))

    # set of all strings that could be country names
    country_set.extend(countries["3Letter"].to_list())
    country_set.extend(countries["Name"].to_list())
    for alt in countries["Alternatives"]:
        country_set.extend(alt.split("\t"))

    return set(country_set), str_to_country
