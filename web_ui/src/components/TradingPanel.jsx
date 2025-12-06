import React, { useState } from 'react';
import React, { useState } from 'react';
import { TrendingUp, TrendingDown, Activity } from 'lucide-react';

const TradingPanel = () => {
    const [orderType, setOrderType] = useState('buy');
    const [price, setPrice] = useState('');
    const [quantity, setQuantity] = useState('');

    const handleSubmit = (e) => {
        e.preventDefault();
        console.log(`Order placed: ${orderType.toUpperCase()} ${quantity} @ ${price}`);
    };

    return (
        <div style={{
            backgroundColor: 'var(--bg-card)',
            borderRadius: '16px',
            padding: '1.5rem',
            border: '1px solid var(--border)',
            height: '100%'
        }}>
            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '1.5rem' }}>
                <h3 style={{ fontSize: '1.1rem', fontWeight: '600' }}>Quick Trade</h3>
                <Activity size={20} color="var(--text-secondary)" />
            </div>

            <div style={{ display: 'flex', gap: '0.5rem', marginBottom: '1.5rem', padding: '0.25rem', backgroundColor: 'var(--bg-dark)', borderRadius: '12px' }}>
                <button
                    onClick={() => setOrderType('buy')}
                    style={{
                        flex: 1,
                        padding: '0.6rem',
                        borderRadius: '8px',
                        border: 'none',
                        backgroundColor: orderType === 'buy' ? 'var(--success)' : 'transparent',
                        color: orderType === 'buy' ? '#fff' : 'var(--text-secondary)',
                        fontWeight: '600',
                        cursor: 'pointer',
                        transition: 'all 0.2s'
                    }}
                >
                    Buy
                </button>
                <button
                    onClick={() => setOrderType('sell')}
                    style={{
                        flex: 1,
                        padding: '0.6rem',
                        borderRadius: '8px',
                        border: 'none',
                        backgroundColor: orderType === 'sell' ? 'var(--danger)' : 'transparent',
                        color: orderType === 'sell' ? '#fff' : 'var(--text-secondary)',
                        fontWeight: '600',
                        cursor: 'pointer',
                        transition: 'all 0.2s'
                    }}
                >
                    Sell
                </button>
            </div>

            <form onSubmit={handleSubmit} style={{ display: 'flex', flexDirection: 'column', gap: '1rem' }}>
                <div>
                    <label style={{ display: 'block', color: 'var(--text-secondary)', fontSize: '0.85rem', marginBottom: '0.5rem' }}>Stock Symbol</label>
                    <input
                        type="text"
                        defaultValue="RELIANCE"
                        style={{
                            width: '100%',
                            padding: '0.75rem',
                            backgroundColor: 'var(--bg-dark)',
                            border: '1px solid var(--border)',
                            borderRadius: '10px',
                            color: 'var(--text-primary)',
                            fontWeight: '600'
                        }}
                    />
                </div>

                <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '1rem' }}>
                    <div>
                        <label style={{ display: 'block', color: 'var(--text-secondary)', fontSize: '0.85rem', marginBottom: '0.5rem' }}>Price</label>
                        <div style={{ position: 'relative' }}>
                            <span style={{ position: 'absolute', left: '10px', top: '50%', transform: 'translateY(-50%)', color: 'var(--text-secondary)', fontWeight: 'bold' }}>₹</span>
                            <input
                                type="number"
                                value={price}
                                onChange={(e) => setPrice(e.target.value)}
                                placeholder="0.00"
                                style={{
                                    width: '100%',
                                    padding: '0.75rem 0.75rem 0.75rem 2rem',
                                    backgroundColor: 'var(--bg-dark)',
                                    border: '1px solid var(--border)',
                                    borderRadius: '10px',
                                    color: 'var(--text-primary)'
                                }}
                            />
                        </div>
                    </div>
                    <div>
                        <label style={{ display: 'block', color: 'var(--text-secondary)', fontSize: '0.85rem', marginBottom: '0.5rem' }}>Quantity</label>
                        <input
                            type="number"
                            value={quantity}
                            onChange={(e) => setQuantity(e.target.value)}
                            placeholder="0"
                            style={{
                                width: '100%',
                                padding: '0.75rem',
                                backgroundColor: 'var(--bg-dark)',
                                border: '1px solid var(--border)',
                                borderRadius: '10px',
                                color: 'var(--text-primary)'
                            }}
                        />
                    </div>
                </div>

                <div style={{ display: 'flex', justifyContent: 'space-between', fontSize: '0.85rem', color: 'var(--text-secondary)', marginTop: '0.5rem' }}>
                    <span>Total</span>
                    <span style={{ color: 'var(--text-primary)', fontWeight: '600' }}>
                        ₹{(Number(price) * Number(quantity)).toFixed(2)}
                    </span>
                </div>

                <button
                    type="submit"
                    style={{
                        marginTop: '1rem',
                        padding: '0.9rem',
                        backgroundColor: orderType === 'buy' ? 'var(--success)' : 'var(--danger)',
                        border: 'none',
                        borderRadius: '10px',
                        color: '#fff',
                        fontWeight: '600',
                        cursor: 'pointer',
                        display: 'flex',
                        alignItems: 'center',
                        justifyContent: 'center',
                        gap: '0.5rem',
                        transition: 'opacity 0.2s'
                    }}
                >
                    {orderType === 'buy' ? <TrendingUp size={18} /> : <TrendingDown size={18} />}
                    {orderType === 'buy' ? 'Place Buy Order' : 'Place Sell Order'}
                </button>
            </form>
        </div>
    );
};

export default TradingPanel;
