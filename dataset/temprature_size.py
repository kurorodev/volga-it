import pandas as pd
import numpy as np

temprature_size = pd.read_csv("dataset/temprature_size.csv")
def tempratureSize():
    print(temprature_size.to_string())