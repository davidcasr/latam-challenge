import pandas as pd
from challenge.preprocessing import get_delay
from sklearn.linear_model import LogisticRegression
from typing import Tuple, Union, List

class DelayModel:

    def __init__(self):
        self._model = LogisticRegression(
            random_state=1,
            class_weight='balanced', 
            max_iter=1000
        )

    def preprocess(
        self,
        data: pd.DataFrame,
        target_column: str = None
    ) -> Union[Tuple[pd.DataFrame, pd.DataFrame], pd.DataFrame]:
        """
        Prepare raw data for training or prediction.

        Args:
            data (pd.DataFrame): raw data.
            target_column (str, optional): if set, the target is returned.

        Returns:
            Tuple[pd.DataFrame, pd.DataFrame]: features and target.
            or
            pd.DataFrame: features.
        """
        # Apply the function to calculate 'delay' and 'min_diff'
        data = get_delay(data)

        # Ensure the 'delay' column is present if specified
        if target_column and target_column not in data.columns:
            raise ValueError(f"The specified target column '{target_column}' is not in the DataFrame.")

        # Select the top 10 most important features as per data analysis
        top_features = [
            "OPERA_Latin American Wings", 
            "MES_7",
            "MES_10",
            "OPERA_Grupo LATAM",
            "MES_12",
            "TIPOVUELO_I",
            "MES_4",
            "MES_11",
            "OPERA_Sky Airline",
            "OPERA_Copa Air"
        ]

        # Preprocessing: dummy encoding
        features = pd.concat([
            pd.get_dummies(data['OPERA'], prefix='OPERA'),
            pd.get_dummies(data['TIPOVUELO'], prefix='TIPOVUELO'),
            pd.get_dummies(data['MES'], prefix='MES')
        ], axis=1)

        # Ensure only the top features are selected
        features = features.reindex(columns=top_features, fill_value=0)

        if target_column:
            target = data[[target_column]] 
            return features, target
        else:
            return features

    def fit(
        self,
        features: pd.DataFrame,
        target: pd.DataFrame
    ) -> None:
        """
        Fit model with preprocessed data.

        Args:
            features (pd.DataFrame): preprocessed data.
            target (pd.DataFrame): target.
        """
        # Fit the model
        self._model.fit(features, target.values.ravel())

    def predict(
        self,
        features: pd.DataFrame
    ) -> List[int]:
        """
        Predict delays for new flights.

        Args:
            features (pd.DataFrame): preprocessed data.
        
        Returns:
            (List[int]): predicted targets.
        """
        predictions = self._model.predict(features)
        return predictions.tolist()