"""Command line interface."""

import typer

cli = typer.Typer()


@cli.command()
def hello(name: str) -> None:
    typer.echo(f"Hello {name}")
