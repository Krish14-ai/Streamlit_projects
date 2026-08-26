from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, classification_report

import numpy as np
import pandas as pd

def train( X_tst):
    df = pd.read_csv(r"C:\Users\Krish\Downloads\Streamlit_projects\Streamlit_projects\Marks_Pridector\data\student_placement_data_100000.csv")

    X = df.drop(columns = ["student_id","placed"])
    y = df["placed"]

    sc = StandardScaler()

    X_sc = sc.fit_transform(X)

    X_tr,a ,y_tr,b, = train_test_split(X_sc,y, test_size= 0.2, random_state= 212)

    model = LogisticRegression()
    model.fit(X_tr, y_tr)

    y_pred = model.predict(X_tst)
    return y_pred

