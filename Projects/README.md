# Projects

This folder contains two Streamlit application prototypes:

- **Marks Predictor** (`Marks_Pridector/`) - A form that collects student details and predicts placement using a scikit-learn logistic regression model. The model reads `Marks_Pridector/app/data/student_placement_data_100000.csv` and trains when a prediction is requested.
- **Spam Classifier** (`Spam_Classifier/`) - A basic email text-entry interface, alongside classifier-related files and a dataset. The interface is not yet connected to a trained model or prediction flow.

## Setup

Install the dependencies from the repository root (`Streamlit_projects/`):

```powershell
uv sync
```

## Run the apps

Run these commands from the repository root:

```powershell
uv run streamlit run Projects/Spam_Classifier/app/main.py
```

```powershell
uv run streamlit run Projects/Marks_Pridector/app/frontend/front.py
```

Streamlit displays a local URL in the terminal. Stop an app with `Ctrl+C`.

> **Note:** The placement app's model import may need adjustment to match the repository's package layout before it runs successfully.

## Data files

The placement predictor expects its CSV at `Marks_Pridector/app/data/student_placement_data_100000.csv`. The spam classifier's data script expects `Spam_Classifier/data/combined_data.csv`. The latter is a large file (over 100 MB) and may need to be obtained separately; CSV files are excluded by the repository's `.gitignore`.
