"""Script for running any/all command line tasks for this project.

All command line tasks should be defined in this file. The only
exception to this is managing dependencies via Pipenv.
"""

# Third-party dependencies:
from invoke import task


@task
def fmt(c):
    """Format code."""
    c.run("black tasks.py")
    c.run("mdformat README.md")
    c.run("mdformat doc")


@task
def lint(c):
    """Run the linter."""
    c.run("pylint tasks.py")


@task
def types(c):
    """Check types."""
    c.run("mypy tasks.py")


@task(pre=[fmt, lint, types])
def check(c):
    """Run all code checks."""
    # Also lint this file.
    c.run("pylint tasks.py")
