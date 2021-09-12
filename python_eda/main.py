import pandas as pd
import sweetviz as sv
from pathlib import Path
import typer

app = typer.Typer()


@app.command()
def report(input_path: str):
    """Generates and render an HTML report of your dataset's EDA.

    Args:
        input_path (str): path to CSV input file.
    """
    # Get dataset name
    dataset_name = Path(input_path).stem.capitalize()

    # Read CSV file from the argument
    df = pd.read_csv(input_path)

    # Generate a reporte.
    report = sv.analyze([df, dataset_name])

    # Render HTML report in your default browser.
    report.show_html()


# -------------------- MORE FEATURES HERE, LATER -----------------
@app.command()
def compare(dataset1: str, dataset2: str):
    """Generate and render an EDA report for comparison of two datasets.

    Args:
        dataset1 (str): Path to main CSV file.
        dataset2 (str): Path to comparison CSV file.
    """

    # Read CSV files from the arguments
    df1, df2 = pd.read_csv(dataset1), pd.read_csv(dataset2)

    # Get dataset names
    dataset1_name, dataset2_name = (
        Path(dataset1).stem.capitalize(),
        Path(dataset2).stem.capitalize(),
    )

    # Generate a comparison report
    report = sv.compare([df1, dataset1_name], [df2, dataset2_name])

    # Render the HTML in your default browser
    report.show_html()


@app.command()
def target(input_path: str, target: str):
    """Generate and render an EDA report against a target variable.

    Args:
        input_path (str): Path to CSV data file
        target (str): Target variable.
    """

    # Read CSV file from the argument
    df = pd.read_csv(input_path)

    # Get dataset name
    dataset_name = Path(input_path).stem.capitalize()

    # Generate a reporte.
    report = sv.analyze([df, dataset_name], target)

    # Render HTML report in your default browser.
    report.show_html()


@app.command()
def compare_with_target(dataset1: str, dataset2: str, target: str):
    """Generate and render EDA report comparing two files against a target variable.

    Args:
        dataset1 (str): Path to main CSV dataset
        dataset2 (str): Path to comparison CSV Dataset
        target (str): Target variable name
    """

    # Read CSVs from arguments
    df1, df2 = pd.read_csv(dataset1), pd.read_csv(dataset2)

    # Get dataset names
    dataset1_name, dataset2_name = (
        Path(dataset1).stem.capitalize(),
        Path(dataset2).stem.capitalize(),
    )

    # Generate a comparison report against the target variable
    report = sv.compare([df1, dataset1_name], [df2, dataset2_name], target)

    # Render HTML report in your default browser
    report.show_html()


if __name__ == "__main__":
    app()
