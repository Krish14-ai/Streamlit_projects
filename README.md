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

