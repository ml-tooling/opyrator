"""Command line interface."""

import os
import sys

import typer
from pydantic.error_wrappers import ValidationError

from opyrator.export import ExportFormat

cli = typer.Typer()


@cli.command()
def launch_ui(opyrator: str, port: int = 8501) -> None:
    """Start a graphical UI server for the opyrator.

    The UI is auto-generated from the input- and output-schema of the given function.
    """
    from opyrator.ui.streamlit_ui import launch_ui  # type: ignore

    launch_ui(opyrator, port)


@cli.command()
def launch_api(opyrator: str, port: int = 8080, host: str = "0.0.0.0") -> None:
    """Start a HTTP API server for the opyrator.

    This will launch a FastAPI server based on the OpenAPI standard and with an automatic interactive documentation.
    """
    # Add the current working directory to the sys path
    # This is required to resolve the opyrator path
    sys.path.append(os.getcwd())

    from opyrator.api.fastapi_app import launch_api  # type: ignore

    launch_api(opyrator, port, host)


@cli.command()
def call(opyrator: str, input_data: str) -> None:
    """Execute the opyrator from command line."""
    # Add the current working directory to the sys path
    # This is required to resolve the opyrator path
    sys.path.append(os.getcwd())

    try:
        from opyrator import Opyrator

        output = Opyrator(opyrator)(input_data)
        if output:
            typer.echo(output.json(indent=4))
        else:
            typer.echo("Nothing returned!")
    except ValidationError as ex:
        typer.secho(str(ex), fg=typer.colors.RED, err=True)


@cli.command()
def export(
    opyrator: str, export_name: str, format: ExportFormat = ExportFormat.ZIP
) -> None:
    """Package and export an opyrator."""
    typer.secho(
        "[WIP] This feature is not finalized yet. You can track the progress and vote for the feature here: https://github.com/ml-tooling/opyrator/issues",
        fg=typer.colors.BRIGHT_YELLOW,
    )


@cli.command()
def deploy(opyrator: str) -> None:
    """Deploy an opyrator to a cloud platform.

    This provides additional features such as SSL, authentication, API tokens, unlimited scalability, load balancing, and monitoring.
    """
    typer.secho(
        "[WIP] This feature is not finalized yet. You can track the progress and vote for the feature here: https://github.com/ml-tooling/opyrator/issues",
        fg=typer.colors.BRIGHT_YELLOW,
    )
