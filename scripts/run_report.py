"""Run the forecasting notebook and rebuild its charts and HTML report."""

from __future__ import annotations

import json
import os
import sys
import tempfile
from pathlib import Path

import nbformat
from nbclient import NotebookClient
from nbconvert import HTMLExporter
import nbconvert


PROJECT_ROOT = Path(__file__).resolve().parents[1]
NOTEBOOK_PATH = PROJECT_ROOT / "spy_risk_forecasting.ipynb"
HTML_PATH = PROJECT_ROOT / "reports" / "spy_risk_forecasting.html"
REQUIRED_INPUTS = (
    PROJECT_ROOT / "data" / "market_training_data.csv",
    PROJECT_ROOT / "data" / "market_development.csv",
    PROJECT_ROOT / "data" / "market_holdout.csv",
)


def check_inputs() -> None:
    """Show a useful error if a required snapshot is missing."""
    missing = [path for path in REQUIRED_INPUTS if not path.is_file()]
    if missing:
        names = ", ".join(str(path.relative_to(PROJECT_ROOT)) for path in missing)
        raise FileNotFoundError(f"Missing input file(s): {names}")


def execute_notebook() -> nbformat.NotebookNode:
    """Run every notebook cell from the repository root with this Python env."""
    notebook = nbformat.read(NOTEBOOK_PATH, as_version=4)
    previous_jupyter_path = os.environ.get("JUPYTER_PATH")

    with tempfile.TemporaryDirectory(prefix="spy-forecast-kernel-") as directory:
        kernel_directory = Path(directory) / "kernels" / "python3"
        kernel_directory.mkdir(parents=True)
        kernel_config = {
            "argv": [sys.executable, "-m", "ipykernel_launcher", "-f", "{connection_file}"],
            "display_name": "Python 3",
            "language": "python",
        }
        (kernel_directory / "kernel.json").write_text(json.dumps(kernel_config))
        os.environ["JUPYTER_PATH"] = directory

        try:
            client = NotebookClient(
                notebook,
                timeout=900,
                kernel_name="python3",
                resources={"metadata": {"path": str(PROJECT_ROOT)}},
            )
            client.execute()
        finally:
            if previous_jupyter_path is None:
                os.environ.pop("JUPYTER_PATH", None)
            else:
                os.environ["JUPYTER_PATH"] = previous_jupyter_path

    nbformat.validate(notebook)
    return notebook


def save_report(notebook: nbformat.NotebookNode) -> None:
    """Save the executed notebook and its browser-friendly HTML version."""
    nbformat.write(notebook, NOTEBOOK_PATH)

    previous_jupyter_path = os.environ.get("JUPYTER_PATH")
    for parent in Path(nbconvert.__file__).resolve().parents:
        candidate = parent / "share" / "jupyter"
        if (candidate / "nbconvert" / "templates" / "lab").is_dir():
            paths = [str(candidate)]
            if previous_jupyter_path:
                paths.insert(0, previous_jupyter_path)
            os.environ["JUPYTER_PATH"] = os.pathsep.join(paths)
            break

    try:
        html, _ = HTMLExporter().from_notebook_node(notebook)
    finally:
        if previous_jupyter_path is None:
            os.environ.pop("JUPYTER_PATH", None)
        else:
            os.environ["JUPYTER_PATH"] = previous_jupyter_path

    HTML_PATH.parent.mkdir(parents=True, exist_ok=True)
    HTML_PATH.write_text(html, encoding="utf-8")


def main() -> None:
    check_inputs()
    notebook = execute_notebook()
    save_report(notebook)
    print("Updated the notebook, nine graphs, and HTML report.")


if __name__ == "__main__":
    main()
