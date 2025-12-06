from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import uvicorn
import pandas as pd

from scraper import fetch_historical_data, fetch_live_data
from analyzer import calculate_technical_indicators, analyze_fundamentals
from predictor import train_predict_model

app = FastAPI()

# Allow CORS for local development
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class StockRequest(BaseModel):
    ticker: str
    period: str = "1y"

@app.get("/")
def read_root():
    return {"message": "Indian Stock Market API is running"}

@app.get("/analyze/{ticker}")
def analyze_stock(ticker: str, period: str = "1y"):
    try:
        # 1. Fetch Data
        live_data = fetch_live_data(ticker)
        hist_data = fetch_historical_data(ticker, period=period)
        
        if hist_data.empty:
            raise HTTPException(status_code=404, detail="No historical data found")
            
        # 2. Analyze Technicals
        analyzed_data = calculate_technical_indicators(hist_data)
        
        # Prepare chart data (last 100 points to keep payload small)
        chart_data = analyzed_data.tail(100).reset_index()
        chart_data['Date'] = chart_data['Date'].astype(str) # Convert to string for JSON
        chart_data_list = chart_data[['Date', 'Close', 'SMA_50', 'SMA_200', 'RSI']].to_dict(orient='records')
        
        # 3. Fundamentals
        fundamentals = analyze_fundamentals(ticker)
        
        # 4. Prediction
        prediction = train_predict_model(analyzed_data)
        
        return {
            "ticker": ticker,
            "live_data": live_data,
            "fundamentals": fundamentals,
            "technical_summary": {
                "latest_close": analyzed_data['Close'].iloc[-1],
                "rsi": analyzed_data['RSI'].iloc[-1],
                "sma_50": analyzed_data['SMA_50'].iloc[-1],
                "sma_200": analyzed_data['SMA_200'].iloc[-1]
            },
            "prediction": prediction,
            "chart_data": chart_data_list
        }
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
