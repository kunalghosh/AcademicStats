"""Console script for academic_stats."""
import sys
import click


@click.command()
def main(args=None):
    """Console script for academic_stats."""
    click.echo("Replace this message by putting your code into "
               "academic_stats.cli.main")
    click.echo("See click documentation at https://click.palletsprojects.com/")
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
