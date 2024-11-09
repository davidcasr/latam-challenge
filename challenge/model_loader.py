import pandas as pd

from challenge.model import DelayModel

def load_trained_model() -> DelayModel:
    # Initialize the DelayModel instance
    model = DelayModel()

    # Load or prepare training data
    data = pd.read_csv("data/data.csv")
    features, target = model.preprocess(data, target_column='delay')
    
    # Train the model
    model.fit(features, target)

    return model
