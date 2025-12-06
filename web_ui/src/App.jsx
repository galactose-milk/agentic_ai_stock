import React, { useState } from 'react';
import Sidebar from './components/Sidebar';
import Header from './components/Header';
import TradingPanel from './components/TradingPanel';
import AgentStatus from './components/AgentStatus';
import StockCard from './components/StockCard';
import './App.css';

function App() {
  const [activeTab, setActiveTab] = useState('dashboard');

  const stocks = [
    { symbol: 'RELIANCE.NS', name: 'Reliance Industries', price: 2450.50, change: 12.30, changePercent: 0.50 },
    { symbol: 'TCS.NS', name: 'Tata Consultancy Svcs', price: 3450.60, change: -15.40, changePercent: -0.45 },
    { symbol: 'INFY.NS', name: 'Infosys Ltd.', price: 1460.10, change: 8.50, changePercent: 0.59 },
    { symbol: 'HDFCBANK.NS', name: 'HDFC Bank Ltd.', price: 1635.20, change: 4.80, changePercent: 0.29 },
  ];

  return (
    <div className="app-container">
      <Sidebar activeTab={activeTab} setActiveTab={setActiveTab} />

      <main className="main-content">
        <Header />

        <div style={{ display: 'grid', gridTemplateColumns: '2fr 1fr', gap: '1.5rem', marginBottom: '1.5rem' }}>
          {/* Left Column: Stats & Charts */}
          <div style={{ display: 'flex', flexDirection: 'column', gap: '1.5rem' }}>

            {/* Portfolio Summary */}
            <div style={{
              display: 'grid',
              gridTemplateColumns: 'repeat(3, 1fr)',
              gap: '1rem'
            }}>
              <div style={{ backgroundColor: 'var(--bg-card)', padding: '1.5rem', borderRadius: '16px', border: '1px solid var(--border)' }}>
                <p style={{ color: 'var(--text-secondary)', fontSize: '0.9rem', marginBottom: '0.5rem' }}>Total Portfolio Value</p>
                <h3 style={{ fontSize: '1.8rem', fontWeight: '700' }}>₹1,24,592.00</h3>
                <span style={{ color: 'var(--success)', fontSize: '0.85rem', fontWeight: '600' }}>+12.5% All time</span>
              </div>
              <div style={{ backgroundColor: 'var(--bg-card)', padding: '1.5rem', borderRadius: '16px', border: '1px solid var(--border)' }}>
                <p style={{ color: 'var(--text-secondary)', fontSize: '0.9rem', marginBottom: '0.5rem' }}>Day's P&L</p>
                <h3 style={{ fontSize: '1.8rem', fontWeight: '700', color: 'var(--success)' }}>+₹1,240.50</h3>
                <span style={{ color: 'var(--success)', fontSize: '0.85rem', fontWeight: '600' }}>+1.02% Today</span>
              </div>
              <div style={{ backgroundColor: 'var(--bg-card)', padding: '1.5rem', borderRadius: '16px', border: '1px solid var(--border)' }}>
                <p style={{ color: 'var(--text-secondary)', fontSize: '0.9rem', marginBottom: '0.5rem' }}>Buying Power</p>
                <h3 style={{ fontSize: '1.8rem', fontWeight: '700' }}>₹45,200.00</h3>
                <span style={{ color: 'var(--text-secondary)', fontSize: '0.85rem' }}>Available Cash</span>
              </div>
            </div>

            {/* Market Overview / Watchlist */}
            <div>
              <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '1rem' }}>
                <h3 style={{ fontSize: '1.2rem', fontWeight: '600' }}>Market Overview</h3>
                <button style={{ color: 'var(--accent-primary)', background: 'none', border: 'none', cursor: 'pointer', fontWeight: '500' }}>View All</button>
              </div>
              <div style={{ display: 'grid', gridTemplateColumns: 'repeat(2, 1fr)', gap: '1rem' }}>
                {stocks.map(stock => (
                  <StockCard key={stock.symbol} {...stock} />
                ))}
              </div>
            </div>

          </div>

          {/* Right Column: Trading & Agent */}
          <div style={{ display: 'flex', flexDirection: 'column', gap: '1.5rem' }}>
            <TradingPanel />
            <AgentStatus />
          </div>
        </div>
      </main>
    </div>
  );
}

export default App;
