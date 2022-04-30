"""Console script for academic_stats."""
import sys
import click
from academic_stats.parsers.parser import PubMed


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
    pubmed = PubMed(pubmed)
    for author in pubmed:
        print(author)


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
