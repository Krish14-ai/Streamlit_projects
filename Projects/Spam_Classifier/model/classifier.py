import pandas as pd 
from sklearn.ensemble import RandomForestClassifier

from pathlib import Path
data_path = Path(__file__).resolve().parent.parent/"data"/"combined_data.csv"

df  = pd.read_csv(data_path)
print(df)