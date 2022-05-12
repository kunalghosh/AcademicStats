"""Console script for academic_stats."""
from collections import defaultdict
from academic_stats.parsers.parser import PubMedParser, ArxivParser, generic_parser

import sys
import click


def process_xmls(xmlobjs: generic_parser, ca_dict=None):
    """
    Processes a bunch of Author Objects

    Returns
    -------
    ca_dict: dict
        Dictionary with country:str as key and set(author_names:str)
    """
    if ca_dict is None:
        ca_dict = defaultdict(lambda: set([]))

    # update the passed country_authors_dict
    for publication in xmlobjs:
        for author in publication.authorlist:
            if author.countries != set([]):
                if author.name != "":
                    for country in author.countries:
                        ca_dict[country].add(author.name)
    return ca_dict


@click.command()
@click.option(
    "--pubmed",
    type=click.Path(exists=True),
    default=None,
    required=False,
    help="Path to the pubmed directory with xml files.",
)
@click.option(
    "--arxiv",
    type=click.Path(exists=True),
    default=None,
    required=False,
    help="Path to the arxiv directory with xml files.",
)
def main(pubmed, arxiv):
    """Console script for academic_stats."""
    country_authors_dict = defaultdict(lambda: set([]))

    if pubmed is not None:
        pubmed = PubMedParser(pubmed)
        country_authors_dict = process_xmls(pubmed, ca_dict=country_authors_dict)

    if arxiv is not None:
        arxiv = ArxivParser(arxiv)
        country_authors_dict = process_xmls(arxiv, ca_dict=country_authors_dict)

    # compute number of authors in each country
    country_nauthor = dict(
        [(country, len(authors)) for country, authors in country_authors_dict.items()]
    )
    # sort by number of authors
    country_nauthor = sorted(country_nauthor.items(), key=lambda kv: kv[1])

    # sort by number of authors
    for country, nauthor in reversed(country_nauthor):
        print(f"{country:28}: {nauthor:5}")


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
