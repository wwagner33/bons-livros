import pandas as pd

def preprocess_data():
    # Load raw data
    df = pd.read_csv('../data/raw/dataset.csv')
    # Perform cleaning and preprocessing
    df.dropna(subset=['description'], inplace=True)
    df.to_csv('../data/processed/processed_dataset.csv', index=False)

if __name__ == '__main__':
    preprocess_data()
