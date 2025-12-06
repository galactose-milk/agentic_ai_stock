import argparse
from scraper import fetch_historical_data, fetch_live_data
from analyzer import calculate_technical_indicators, analyze_fundamentals
from trading_agent import TradingAgent

def main():
    parser = argparse.ArgumentParser(description="Indian Stock Market Scraper & Analyzer")
    parser.add_argument("--ticker", type=str, default="RELIANCE.NS", help="Stock ticker symbol (default: RELIANCE.NS)")
    parser.add_argument("--period", type=str, default="1y", help="Period for historical data (default: 1y)")
    parser.add_argument("--mode", type=str, default="analyze", choices=["analyze", "trade", "real"], help="Mode: analyze, trade (paper), or real (real money)")
    
    args = parser.parse_args()
    ticker = args.ticker
    
    if args.mode == "trade":
        # For real trading, we need to pass the mode
        # If user wants real trading, they should use --mode real-trade (or we can just use trade and ask for confirmation)
        # But to keep it simple with existing args, let's add a new choice or just assume 'trade' is paper and 'real' is real.
        # Let's update the arg parser choices first.
        pass

    if args.mode in ["trade", "real"]:
        mode = "real" if args.mode == "real" else "paper"
        agent = TradingAgent(mode=mode)
        agent.run_strategy(ticker)
        return

    print(f"--- Analyzing {ticker} ---")
    
    # 1. Fetch Live Data
    print("\n[1] Fetching Live Data...")
    live_data = fetch_live_data(ticker)
    if live_data:
        print(f"Live Data: {live_data}")
    else:
        print("Could not fetch live data.")

    # 2. Fetch Historical Data
    print(f"\n[2] Fetching Historical Data ({args.period})...")
    hist_data = fetch_historical_data(ticker, period=args.period)
    
    if not hist_data.empty:
        print(f"Fetched {len(hist_data)} records.")
        
        # 3. Analyze Technicals
        print("\n[3] Calculating Technical Indicators...")
        analyzed_data = calculate_technical_indicators(hist_data)
        
        # Display latest data
        latest = analyzed_data.iloc[-1]
        print(f"Latest Close: {latest['Close']:.2f}")
        print(f"SMA 50: {latest['SMA_50']:.2f}")
        print(f"SMA 200: {latest['SMA_200']:.2f}")
        print(f"RSI: {latest['RSI']:.2f}")
        
    else:
        print("No historical data found.")
        
    # 4. Analyze Fundamentals
    print("\n[4] Fetching Fundamentals...")
    fundamentals = analyze_fundamentals(ticker)
    if fundamentals:
        for key, value in fundamentals.items():
            print(f"{key}: {value}")
    else:
        print("Could not fetch fundamentals.")

if __name__ == "__main__":
    main()
