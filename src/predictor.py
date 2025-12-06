import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

def prepare_data(df, lookback=5):
    """
    Prepares data for training/prediction.
    Uses the last 'lookback' days to predict the next day's Close.
    """
    data = df.copy()
    data['Target'] = data['Close'].shift(-1)
    data = data.dropna()
    
    X = []
    y = []
    
    # Simple feature engineering: use previous 'lookback' closes as features
    # This is a basic approach.
    values = data['Close'].values
    for i in range(lookback, len(values) - 1):
        X.append(values[i-lookback:i])
        y.append(values[i]) # The target is the next value, which we shifted already? 
                            # Wait, if we shifted Target, then data['Target'][i] is Close[i+1].
                            # Let's stick to a simpler sliding window on the raw array.
                            
    # Re-doing sliding window correctly
    X, y = [], []
    values = df['Close'].values
    for i in range(len(values) - lookback):
        X.append(values[i:i+lookback])
        y.append(values[i+lookback])
        
    return np.array(X), np.array(y)

def train_predict_model(df):
    """
    Trains a simple Linear Regression model and predicts the next price.
    """
    if len(df) < 50:
        return None, "Not enough data"
        
    X, y = prepare_data(df)
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)
    
    model = LinearRegression()
    model.fit(X_train, y_train)
    
    predictions = model.predict(X_test)
    mse = mean_squared_error(y_test, predictions)
    
    # Predict next day
    last_window = df['Close'].values[-5:].reshape(1, -1)
    next_price = model.predict(last_window)[0]
    
    return {
        "next_price_prediction": next_price,
        "mse": mse,
        "model": "LinearRegression"
    }
