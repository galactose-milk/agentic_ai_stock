from fastapi import FastAPI, HTTPException, BackgroundTasks
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import uvicorn
import pandas as pd
import asyncio
from typing import List, Optional
from datetime import datetime

from scraper import fetch_historical_data, fetch_live_data
from analyzer import calculate_technical_indicators, analyze_fundamentals
from predictor import train_predict_model
from trading_agent import TradingAgent

app = FastAPI()

# Allow CORS for local development
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- Global State ---
agent = TradingAgent(mode="paper")
agent_running = False
agent_logs = []

# --- Models ---
class StockRequest(BaseModel):
    ticker: str
    period: str = "1y"

class TradeRequest(BaseModel):
    ticker: str
    action: str # "buy" or "sell"
    quantity: int
    price: float

class AgentControlRequest(BaseModel):
    action: str # "start" or "stop"

# --- Helper Functions ---
def log_agent_activity(msg: str, type: str = "info"):
    timestamp = datetime.now().strftime("%H:%M:%S")
    agent_logs.append({"time": timestamp, "type": type, "msg": msg})
    # Keep logs limited
    if len(agent_logs) > 50:
        agent_logs.pop(0)

async def run_agent_loop():
    global agent_running
    log_agent_activity("Agent background loop started", "success")
    
    watched_stocks = ["RELIANCE.NS", "TCS.NS", "INFY.NS", "HDFCBANK.NS"]
    
    while agent_running:
        for ticker in watched_stocks:
            if not agent_running: break
            try:
                log_agent_activity(f"Analyzing {ticker}...", "info")
                # In a real scenario, we would call agent.run_strategy(ticker) here
                # For now, we'll just simulate some activity
                await asyncio.sleep(2) 
                
                # Randomly log something interesting
                import random
                if random.random() < 0.3:
                     log_agent_activity(f"Volatility detected in {ticker}", "warning")
                     
            except Exception as e:
                log_agent_activity(f"Error analyzing {ticker}: {str(e)}", "error")
        
        await asyncio.sleep(5) # Pause between cycles

# --- Endpoints ---

@app.get("/")
def read_root():
    return {"message": "Indian Stock Market API is running"}

@app.get("/market/overview")
def get_market_overview():
    tickers = ["RELIANCE.NS", "TCS.NS", "INFY.NS", "HDFCBANK.NS", "TATAMOTORS.NS"]
    overview = []
    
    for ticker in tickers:
        try:
            live = fetch_live_data(ticker)
            if live:
                # Calculate change percent if not available (assuming live_data might lack it)
                # For this demo, we'll trust fetch_live_data or mock if needed
                overview.append({
                    "symbol": ticker,
                    "name": ticker.split('.')[0], # Simple name extraction
                    "price": live.get('current_price', 0),
                    "change": live.get('change', 0),
                    "changePercent": live.get('change_percent', 0)
                })
        except Exception as e:
            print(f"Error fetching overview for {ticker}: {e}")
            
    # Add Portfolio Summary
    summary = agent.engine.get_summary()
    
    return {
        "stocks": overview,
        "portfolio": summary
    }

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

@app.post("/trade")
def execute_trade(trade: TradeRequest):
    try:
        success = False
        if trade.action.lower() == "buy":
            success = agent.engine.buy(trade.ticker, trade.price, trade.quantity)
        elif trade.action.lower() == "sell":
            success = agent.engine.sell(trade.ticker, trade.price, trade.quantity)
        else:
            raise HTTPException(status_code=400, detail="Invalid action. Use 'buy' or 'sell'.")
            
        if success:
            return {"status": "success", "message": f"Order executed: {trade.action} {trade.quantity} {trade.ticker}"}
        else:
            raise HTTPException(status_code=400, detail="Order failed (insufficient funds or holdings)")
            
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/agent/status")
def get_agent_status():
    return {
        "running": agent_running,
        "logs": agent_logs
    }

@app.post("/agent/control")
async def control_agent(control: AgentControlRequest, background_tasks: BackgroundTasks):
    global agent_running
    
    if control.action == "start":
        if not agent_running:
            agent_running = True
            background_tasks.add_task(run_agent_loop)
            return {"status": "started", "message": "Agent started"}
        else:
            return {"status": "already_running", "message": "Agent is already running"}
            
    elif control.action == "stop":
        agent_running = False
        log_agent_activity("Agent stopped by user", "warning")
        return {"status": "stopped", "message": "Agent stopping..."}
        
    else:
        raise HTTPException(status_code=400, detail="Invalid action")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
