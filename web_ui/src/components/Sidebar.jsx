import React from 'react';
import { LayoutDashboard, LineChart, Bot, Settings, LogOut } from 'lucide-react';

const Sidebar = ({ activeTab, setActiveTab }) => {
    const menuItems = [
        { id: 'dashboard', icon: LayoutDashboard, label: 'Dashboard' },
        { id: 'market', icon: LineChart, label: 'Market Analysis' },
        { id: 'agent', icon: Bot, label: 'Auto Agent' },
        { id: 'settings', icon: Settings, label: 'Settings' },
    ];

    return (
        <div style={{
            width: '260px',
            backgroundColor: 'var(--bg-card)',
            borderRight: '1px solid var(--border)',
            display: 'flex',
            flexDirection: 'column',
            padding: '1.5rem'
        }}>
            <div style={{ display: 'flex', alignItems: 'center', gap: '0.75rem', marginBottom: '3rem' }}>
                <div style={{
                    width: '32px',
                    height: '32px',
                    background: 'linear-gradient(135deg, var(--accent-primary), var(--accent-secondary))',
                    borderRadius: '8px',
                    display: 'flex',
                    alignItems: 'center',
                    justifyContent: 'center'
                }}>
                    <LineChart size={20} color="white" />
                </div>
                <h1 style={{ fontSize: '1.25rem', fontWeight: '700', letterSpacing: '-0.025em' }}>
                    Stock<span style={{ color: 'var(--accent-secondary)' }}>AI</span>
                </h1>
            </div>

            <nav style={{ flex: 1 }}>
                {menuItems.map((item) => {
                    const Icon = item.icon;
                    const isActive = activeTab === item.id;
                    return (
                        <button
                            key={item.id}
                            onClick={() => setActiveTab(item.id)}
                            style={{
                                width: '100%',
                                display: 'flex',
                                alignItems: 'center',
                                gap: '0.75rem',
                                padding: '0.75rem 1rem',
                                marginBottom: '0.5rem',
                                backgroundColor: isActive ? 'rgba(59, 130, 246, 0.1)' : 'transparent',
                                border: 'none',
                                borderRadius: '12px',
                                color: isActive ? 'var(--accent-primary)' : 'var(--text-secondary)',
                                cursor: 'pointer',
                                transition: 'all 0.2s ease',
                                textAlign: 'left',
                                fontSize: '0.95rem',
                                fontWeight: isActive ? '600' : '500'
                            }}
                        >
                            <Icon size={20} />
                            {item.label}
                        </button>
                    );
                })}
            </nav>

            <button style={{
                display: 'flex',
                alignItems: 'center',
                gap: '0.75rem',
                padding: '0.75rem 1rem',
                backgroundColor: 'transparent',
                border: 'none',
                color: 'var(--danger)',
                cursor: 'pointer',
                fontSize: '0.95rem',
                fontWeight: '500',
                marginTop: 'auto'
            }}>
                <LogOut size={20} />
                Logout
            </button>
        </div>
    );
};

export default Sidebar;
