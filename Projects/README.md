# Projects

This folder contains two Streamlit application prototypes:

- **Marks Predictor** (`Marks_Pridector/`) - A form that collects student details and predicts placement using a scikit-learn logistic regression model. The model reads `Marks_Pridector/app/data/student_placement_data_100000.csv` and trains when a prediction is requested.
- **Spam Classifier** (`Spam_Classifier/`) - A basic email text-entry interface, alongside classifier-related files and a dataset. The interface is not yet connected to a trained model or prediction flow.

## Setup

Install the dependencies from the repository root (`Streamlit_projects/`):

```powershell
uv sync
```

