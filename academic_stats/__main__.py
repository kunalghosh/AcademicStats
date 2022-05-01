"""Console script for academic_stats."""
from collections import defaultdict
import sys
import click
from academic_stats.parsers.parser import PubMed, Arxiv


@click.command()
@click.option(
    "--pubmed",
    type=click.Path(exists=True),
    default=None,
    required=True,
    help="Path to the pubmed directory with xml files.",
)
@click.option(
    "--arxiv",
    type=click.Path(exists=True),
    default=None,
    required=True,
    help="Path to the arxiv directory with xml files.",
)
def main(pubmed, arxiv):
    """Console script for academic_stats."""
    country_authors_dict = defaultdict(lambda: set([]))

    pubmed = PubMed(pubmed)
    for author in pubmed:
        if author.countries != set([]):
            if author.name != "":
                for country in author.countries:
                    country_authors_dict[country].add(author.name)

    arxiv = Arxiv(arxiv)
    for author in arxiv:
        if author.countries != set([]):
            if author.name != "":
                for country in author.countries:
                    country_authors_dict[country].add(author.name)

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
