"""Console script for academic_stats."""
from collections import defaultdict
import sys
import click
from academic_stats.parsers.parser import PubMed, Arxiv, generic_parser


def process_xmls(xmlobjs: generic_parser):
    country_authors_dict = defaultdict(lambda: set([]))
    for author in xmlobjs:
        if author.countries != set([]):
            if author.name != "":
                for country in author.countries:
                    country_authors_dict[country].add(author.name)
    return country_authors_dict


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
        pubmed = PubMed(pubmed)
        country_authors_dict.update(process_xmls(pubmed))

    if arxiv is not None:
        arxiv = Arxiv(arxiv)
        country_authors_dict.update(process_xmls(arxiv))

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
