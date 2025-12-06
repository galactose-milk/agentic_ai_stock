import React, { useState } from 'react';
import { Play, Square, Zap, Terminal } from 'lucide-react';

const AgentStatus = () => {
    const [isRunning, setIsRunning] = useState(false);
    const [logs, setLogs] = useState([
        { time: '10:30:01', type: 'info', msg: 'Agent initialized' },
        { time: '10:30:05', type: 'success', msg: 'Connected to market data stream' },
        { time: '10:31:12', type: 'warning', msg: 'Volatility spike detected' },
        { time: '10:32:45', type: 'info', msg: 'Analyzing RELIANCE signals...' },
    ]);

    return (
        <div style={{
            backgroundColor: 'var(--bg-card)',
            borderRadius: '16px',
            padding: '1.5rem',
            border: '1px solid var(--border)',
            display: 'flex',
            flexDirection: 'column',
            height: '100%'
        }}>
            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '1.5rem' }}>
                <div style={{ display: 'flex', alignItems: 'center', gap: '0.75rem' }}>
                    <div style={{
                        padding: '0.5rem',
                        backgroundColor: 'rgba(6, 182, 212, 0.1)',
                        borderRadius: '8px',
                        color: 'var(--accent-secondary)'
                    }}>
                        <Zap size={20} />
                    </div>
                    <div>
                        <h3 style={{ fontSize: '1.1rem', fontWeight: '600' }}>Auto Agent</h3>
                        <div style={{ display: 'flex', alignItems: 'center', gap: '0.4rem', marginTop: '0.2rem' }}>
                            <span style={{
                                width: '8px',
                                height: '8px',
                                borderRadius: '50%',
                                backgroundColor: isRunning ? 'var(--success)' : 'var(--text-secondary)',
                                boxShadow: isRunning ? '0 0 8px var(--success)' : 'none'
                            }}></span>
                            <span style={{ fontSize: '0.85rem', color: isRunning ? 'var(--success)' : 'var(--text-secondary)' }}>
                                {isRunning ? 'Running' : 'Stopped'}
                            </span>
                        </div>
                    </div>
                </div>

                <button
                    onClick={() => setIsRunning(!isRunning)}
                    style={{
                        padding: '0.6rem 1.2rem',
                        borderRadius: '10px',
                        border: 'none',
                        backgroundColor: isRunning ? 'rgba(239, 68, 68, 0.1)' : 'rgba(16, 185, 129, 0.1)',
                        color: isRunning ? 'var(--danger)' : 'var(--success)',
                        fontWeight: '600',
                        cursor: 'pointer',
                        display: 'flex',
                        alignItems: 'center',
                        gap: '0.5rem',
                        transition: 'all 0.2s'
                    }}
                >
                    {isRunning ? <Square size={16} fill="currentColor" /> : <Play size={16} fill="currentColor" />}
                    {isRunning ? 'Stop Agent' : 'Start Agent'}
                </button>
            </div>

            <div style={{
                flex: 1,
                backgroundColor: '#000',
                borderRadius: '12px',
                padding: '1rem',
                fontFamily: 'monospace',
                fontSize: '0.85rem',
                overflowY: 'auto',
                border: '1px solid var(--border)'
            }}>
                <div style={{ display: 'flex', alignItems: 'center', gap: '0.5rem', marginBottom: '0.75rem', color: 'var(--text-secondary)', borderBottom: '1px solid #333', paddingBottom: '0.5rem' }}>
                    <Terminal size={14} />
                    <span>Live Logs</span>
                </div>
                <div style={{ display: 'flex', flexDirection: 'column', gap: '0.5rem' }}>
                    {logs.map((log, i) => (
                        <div key={i} style={{ display: 'flex', gap: '0.75rem' }}>
                            <span style={{ color: '#666' }}>[{log.time}]</span>
                            <span style={{
                                color: log.type === 'success' ? 'var(--success)' :
                                    log.type === 'warning' ? 'var(--warning)' :
                                        log.type === 'error' ? 'var(--danger)' : 'var(--text-primary)'
                            }}>
                                {log.msg}
                            </span>
                        </div>
                    ))}
                    {isRunning && (
                        <div style={{ display: 'flex', gap: '0.75rem', animation: 'pulse 1.5s infinite' }}>
                            <span style={{ color: '#666' }}>[{new Date().toLocaleTimeString('en-US', { hour12: false })}]</span>
                            <span style={{ color: 'var(--accent-secondary)' }}>Scanning market opportunities...</span>
                        </div>
                    )}
                </div>
            </div>
        </div>
    );
};

export default AgentStatus;
