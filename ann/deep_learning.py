import numpy as np
import pandas as pd 
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score



data = load_breast_cancer(as_frame=True).frame   
x,y =  load_breast_cancer(return_X_y = True, as_frame = True)
x_train , x_test , y_train , y_test = train_test_split(x,y,test_size=0.2,random_state=42)

scaler = StandardScaler()
x_train = scaler.fit_transform(x_train)


model = MLPClassifier(hidden_layer_sizes=(100,), max_iter=1000, random_state=42)
model.fit(x_train, y_train)
score = model.score(x_train, y_train)
print(f"Training accuracy: {score:.4f}")
