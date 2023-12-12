import pandas as pd
import numpy as np

home_specific = pd.read_csv("dataset/home_specific.csv")
def homeSpecific():
    home_specific.describe().transpose()
    
    print(home_specific.to_string())
