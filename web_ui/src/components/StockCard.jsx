import React from 'react';
import { TrendingUp, TrendingDown } from 'lucide-react';

const StockCard = ({ symbol, name, price, change, changePercent }) => {
    const isPositive = change >= 0;

    return (
        <div style={{
            backgroundColor: 'var(--bg-card)',
            borderRadius: '16px',
            padding: '1.25rem',
            border: '1px solid var(--border)',
            display: 'flex',
            flexDirection: 'column',
            gap: '0.5rem',
            cursor: 'pointer',
            transition: 'transform 0.2s, border-color 0.2s'
        }}
            onMouseEnter={(e) => {
                e.currentTarget.style.transform = 'translateY(-2px)';
                e.currentTarget.style.borderColor = 'var(--accent-primary)';
            }}
            onMouseLeave={(e) => {
                e.currentTarget.style.transform = 'translateY(0)';
                e.currentTarget.style.borderColor = 'var(--border)';
            }}
        >
            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start' }}>
                <div>
                    <h4 style={{ fontSize: '1.1rem', fontWeight: '700' }}>{symbol}</h4>
                    <p style={{ fontSize: '0.8rem', color: 'var(--text-secondary)' }}>{name}</p>
                </div>
                <div style={{
                    padding: '0.25rem 0.5rem',
                    borderRadius: '6px',
                    backgroundColor: isPositive ? 'rgba(16, 185, 129, 0.1)' : 'rgba(239, 68, 68, 0.1)',
                    color: isPositive ? 'var(--success)' : 'var(--danger)',
                    fontSize: '0.8rem',
                    fontWeight: '600',
                    display: 'flex',
                    alignItems: 'center',
                    gap: '0.25rem'
                }}>
                    {isPositive ? <TrendingUp size={14} /> : <TrendingDown size={14} />}
                    {Math.abs(changePercent)}%
                </div>
            </div>

            <div style={{ marginTop: '0.5rem' }}>
                <h3 style={{ fontSize: '1.5rem', fontWeight: '700' }}>₹{price.toLocaleString()}</h3>
                <p style={{
                    fontSize: '0.85rem',
                    color: isPositive ? 'var(--success)' : 'var(--danger)',
                    display: 'flex',
                    alignItems: 'center',
                    gap: '0.25rem'
                }}>
                    {isPositive ? '+' : ''}{change} Today
                </p>
            </div>

            {/* Mini chart placeholder */}
            <div style={{ height: '40px', marginTop: '0.5rem', display: 'flex', alignItems: 'flex-end', gap: '2px', opacity: 0.5 }}>
                {[...Array(20)].map((_, i) => {
                    const height = 20 + Math.random() * 80;
                    return (
                        <div key={i} style={{
                            flex: 1,
                            height: `${height}%`,
                            backgroundColor: isPositive ? 'var(--success)' : 'var(--danger)',
                            borderRadius: '2px'
                        }}></div>
                    )
                })}
            </div>
        </div>
    );
};

export default StockCard;
