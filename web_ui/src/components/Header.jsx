import React from 'react';
import { Search, Bell, User } from 'lucide-react';

const Header = () => {
    return (
        <header style={{
            display: 'flex',
            justifyContent: 'space-between',
            alignItems: 'center',
            paddingBottom: '2rem'
        }}>
            <div>
                <h2 style={{ fontSize: '1.5rem', fontWeight: '700' }}>Dashboard</h2>
                <p style={{ color: 'var(--text-secondary)', fontSize: '0.9rem' }}>Welcome back, Trader</p>
            </div>

            <div style={{ display: 'flex', alignItems: 'center', gap: '1.5rem' }}>
                <div style={{ position: 'relative' }}>
                    <Search size={20} style={{ position: 'absolute', left: '12px', top: '50%', transform: 'translateY(-50%)', color: 'var(--text-secondary)' }} />
                    <input
                        type="text"
                        placeholder="Search stocks..."
                        style={{
                            backgroundColor: 'var(--bg-card)',
                            border: '1px solid var(--border)',
                            borderRadius: '12px',
                            padding: '0.6rem 1rem 0.6rem 2.5rem',
                            color: 'var(--text-primary)',
                            outline: 'none',
                            width: '280px',
                            transition: 'border-color 0.2s'
                        }}
                        onFocus={(e) => e.target.style.borderColor = 'var(--accent-primary)'}
                        onBlur={(e) => e.target.style.borderColor = 'var(--border)'}
                    />
                </div>

                <button style={{
                    position: 'relative',
                    background: 'var(--bg-card)',
                    border: '1px solid var(--border)',
                    padding: '0.6rem',
                    borderRadius: '12px',
                    color: 'var(--text-secondary)',
                    cursor: 'pointer'
                }}>
                    <Bell size={20} />
                    <span style={{
                        position: 'absolute',
                        top: '-2px',
                        right: '-2px',
                        width: '10px',
                        height: '10px',
                        backgroundColor: 'var(--danger)',
                        borderRadius: '50%',
                        border: '2px solid var(--bg-dark)'
                    }}></span>
                </button>

                <div style={{ display: 'flex', alignItems: 'center', gap: '0.75rem' }}>
                    <div style={{
                        width: '40px',
                        height: '40px',
                        borderRadius: '12px',
                        backgroundColor: 'var(--bg-card)',
                        display: 'flex',
                        alignItems: 'center',
                        justifyContent: 'center',
                        border: '1px solid var(--border)'
                    }}>
                        <User size={20} color="var(--accent-primary)" />
                    </div>
                </div>
            </div>
        </header>
    );
};

export default Header;
