from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, classification_report

import numpy as np
import pandas as pd

import pandas as pd
from pathlib import Path

DATA_PATH = Path(__file__).resolve().parent.parent / "data" / "student_placement_data_100000.csv"

def train( X_tst):
    df = pd.read_csv(DATA_PATH)

    X = df.drop(columns = ["student_id","placed"])
    y = df["placed"]

    sc = StandardScaler()

    sc.fit(X)
    X_sc = sc.transform(X)

    X_tr,a ,y_tr,b, = train_test_split(X_sc,y, test_size= 0.2, random_state= 212)

    model = LogisticRegression()
    model.fit(X_tr, y_tr)

    tst = np.array(X_tst).reshape(1, -1)
    y_pred = model.predict(tst)
    return y_pred

