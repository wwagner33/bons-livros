import pandas as pd
import numpy as np
import os
import glob
import seaborn as sns
import scipy.stats as stats
import matplotlib.pyplot as plt
from sklearn.preprocessing import OrdinalEncoder

def preprocess_data():
    dirname = os.path.dirname(__file__)
    filesource = os.path.join(dirname, '../data/raw/dataset.csv')
    filetarget = os.path.join(dirname, '../data/processed/processed_dataset.csv')
    
    df=pd.read_csv(filesource)
  
    if 'description' in df.columns:
        df.dropna(subset=['description'], inplace=True)

    # Drop duplicates, reset index, and other preprocessing steps
    df.drop_duplicates(inplace=True)
    df.reset_index(drop=True, inplace=True)

    # Save the processed dataset
    df.to_csv(filetarget, index=False)

if __name__ == '__main__':
    preprocess_data()
