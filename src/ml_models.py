import torch
from transformers import pipeline
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import pandas as pd
import numpy as np

class SentimentAnalyzer:
    def __init__(self, model_name="distilbert-base-uncased-finetuned-sst-2-english"):
        print(f"Loading Sentiment Model: {model_name}...")
        try:
            self.nlp = pipeline("sentiment-analysis", model=model_name)
        except Exception as e:
            print(f"Error loading model {model_name}: {e}. Fallback to default.")
            self.nlp = pipeline("sentiment-analysis")

    def analyze(self, texts):
        """
        Analyzes a list of texts and returns the average sentiment score.
        Score range: -1 (Negative) to 1 (Positive).
        """
        if not texts:
            return 0.0
        
        results = self.nlp(texts)
        score_sum = 0
        for res in results:
            label = res['label']
            score = res['score']
            if label == 'NEGATIVE':
                score_sum -= score
            else:
                score_sum += score
        
        return score_sum / len(texts)

class PricePredictor:
    def __init__(self):
        self.model = RandomForestRegressor(n_estimators=100, random_state=42)
        self.is_trained = False

    def prepare_data(self, df):
        """
        Prepares data for training/prediction.
        Assumes df has technical indicators.
        Target: Next day's Close.
        """
        data = df.copy()
        data['Target'] = data['Close'].shift(-1)
        data = data.dropna()
        
        features = ['Open', 'High', 'Low', 'Close', 'Volume', 'SMA_50', 'SMA_200', 'RSI']
        # Ensure all features exist
        available_features = [f for f in features if f in data.columns]
        
        X = data[available_features]
        y = data['Target']
        return X, y, available_features

    def train(self, df):
        X, y, self.features = self.prepare_data(df)
        if len(X) < 50:
            print("Not enough data to train.")
            return
        
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)
        self.model.fit(X_train, y_train)
        self.is_trained = True
        
        predictions = self.model.predict(X_test)
        mse = mean_squared_error(y_test, predictions)
        print(f"Model Trained. MSE: {mse:.4f}")

    def predict(self, current_data):
        """
        Predicts next day's close price based on current data (latest row).
        """
        if not self.is_trained:
            print("Model not trained yet.")
            return None
            
        # Ensure input has same features
        input_data = current_data[self.features].values.reshape(1, -1)
        prediction = self.model.predict(input_data)
        return prediction[0]
