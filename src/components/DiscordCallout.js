import React from 'react';
import { FaDiscord } from 'react-icons/fa';

export default function DiscordCallout({ children }) {
  return (
    <div
      style={{
        display: 'flex',
        alignItems: 'center',

        backgroundColor: 'var(--ifm-background-surface-color)',
        borderRadius: 'var(--ifm-border-radius)',
        padding: '1.5rem',
        marginBottom: '1rem',
        boxShadow: '0 2px 8px rgba(0, 0, 0, 0.1)',
        border: '1px solid var(--ifm-color-emphasis-300)',
      }}
    >
      <FaDiscord
        style={{
          fontSize: '5rem',
          color: '#5865f2',
          marginRight: '1.5rem',
          flexShrink: 0,
        }}
      />

      <div style={{ fontSize: '1.1rem', lineHeight: '1.6' }}>
        {children}
      </div>
    </div>
  );
}