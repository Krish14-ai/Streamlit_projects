# Streamlit Projects

A collection of Python and Streamlit learning examples and small application prototypes. The examples cover basic Streamlit widgets, page layout, data display, and simple interactive apps.

## Requirements

- Python 3.14 or newer
- [uv](https://docs.astral.sh/uv/) for managing the project environment and dependencies

## Setup

From this directory, install the project dependencies:

```powershell
uv sync
```

## Run an example

Start any Streamlit script from the project directory with `uv run streamlit run`. For example:

```powershell
uv run streamlit run Introduction/Intro.py
```

Other introductory examples:

```powershell
uv run streamlit run "Introduction/clmns_&_layout.py"
uv run streamlit run Introduction/widgits.py
uv run streamlit run Introduction/data_representation.py
uv run streamlit run Introduction/api.py
```

Streamlit prints a local URL in the terminal; open it in a browser to use the app. Stop the server with `Ctrl+C`.

## Contents

- `Introduction/` - Small demonstrations of Streamlit text and selection widgets, columns and layout, beverage customization, CSV upload and filtering, and a currency-conversion example.
- `Projects/Marks_Pridector/` - A placement-prediction prototype with a Streamlit form and a scikit-learn model.
- `Projects/Spam_Classifier/` - A spam-classifier prototype with a simple Streamlit interface and classifier-related files.
- `src/streamlit_projects/` - Python package scaffold.

The project applications are works in progress. In particular, the spam-classifier interface is not yet connected to a prediction flow. Some examples also rely on external services or local CSV data.