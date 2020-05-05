"""
Command Line application
"""
import typer
import uvicorn


cli = typer.Typer()


@cli.command()
def dev(port: int = 5000):
    """
    Run the application in development mode.
    """
    uvicorn.run("backend:app", port=port, reload=True, access_log=False)


@cli.command()
def prod(port: int = 5000, access_lob: bool = False):
    """
    Run the application in production mode.
    """
    msg = typer.style("Not implemented yet!", fg=typer.colors.RED)
    typer.echo(msg)


def run():
    """
    Command Line Interface entrypoint.
    """
    cli()
