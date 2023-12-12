import pandas as pd
import numpy as np

temprature = pd.read_csv("dataset/temprature.csv")
n = len(temprature)
train_temp = temprature[0:int(n*0.7)]
test_temp = temprature[int(n*0.9):]
val_temp = temprature[int(n*0.7):int(n*0.9)]
def temprature():
    print(temprature.to_string())