"""Console script for academic_stats."""
import sys
import click


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
    click.echo(
        "Replace this message by putting your code into " "academic_stats.cli.main"
    )
    click.echo("See click documentation at https://click.palletsprojects.com/")
    print(f"Pubmed {pubmed} Arxiv {arxiv}")
    print("This is run from cli")
    print("This is from within __main__")
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
