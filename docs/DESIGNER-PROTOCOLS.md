# APEX Designer Protocols - UI/UX Design System and Standards

> **Version:** 2.0.0 | **Last Updated:** July 25, 2026

---

## 1. Design Philosophy

Professional trading desktop app for Windows. Communicates trust, precision,
real-time awareness. Every pixel serves a purpose.

### Principles
1. Clarity Over Decoration
2. Dark-First Design (light theme secondary)
3. Real-Time Awareness (live data visually distinct)
4. Progressive Disclosure (summary first, details on demand)
5. Keyboard-First (power users operate via keyboard)
6. Consistent Spacing (4px base grid)
7. Accessible (WCAG 2.1 AA)

---

## 2. Color System

- Background Primary: #0a0a0f | Secondary: #12121a | Tertiary: #1a1a2e
- Text Primary: #e4e4e7 | Secondary: #a1a1aa | Muted: #52525b
- Accent: #6366f1 (indigo) | Hover: #818cf8
- Success/Profit: #22c55e | Danger/Loss: #ef4444 | Warning: #f59e0b | Info: #3b82f6
- Border: #27272a | Focus: #6366f1
- Status: Connected #22c55e (pulse), Disconnected #ef4444, Syncing #f59e0b, Idle #52525b

---

## 3. Typography

- Fonts: Inter (UI), JetBrains Mono (numbers, code, addresses)
- Base: 14px | Display: 28px bold | H1: 22px | H2: 18px | H3: 16px | Caption: 12px | Micro: 11px
- Line height: 1.5 body, 1.2 headings | Numbers: tabular-nums

---

## 4. Components

- **Buttons:** Primary (indigo, white text, 8px radius, 36px height), Secondary (transparent, indigo border), Danger (red), Ghost (text only)
- **Cards:** #12121a bg, 1px #27272a border, 12px radius, 16/24px padding, no shadow
- **Tables:** Header uppercase 11px, 40px rows, alternating bg, hover #1a1a2e, numeric right-aligned mono
- **Inputs:** 36px height, #0a0a0f bg, 8px radius, label above, API keys password with toggle
- **Modals:** rgba(0,0,0,0.6) overlay, #12121a panel, 12px radius, max 480px
- **Toasts:** Bottom-right, 5s auto-dismiss, colored left border, max 3 stacked
- **Tabs:** Underline style, active indigo plus white, 40px height

---

## 5. Layout

- Sidebar: 240px (collapsible to 64px icons)
- Top Bar: 48px (title, connection status, settings)
- Status Bar: 32px bottom (chains, gas, AI status)
- Min window: 1024x680 | Below 1280: sidebar collapses
- Desktop app only; mobile NOT a goal

---

## 6. Animation

- 150ms micro, 300ms transitions | cubic-bezier(0.4, 0, 0.2, 1)
- Live pulse 2s | Number flash 200ms | Page fade plus slide 10px
- No gratuitous animation

---

## 7. Icons

- Lucide React | 16/20/24px | 1.5px stroke | Custom only for chain logos

---

## 8. AI Settings Page Design

- Title: AI Configuration | Subtitle: Configure cloud AI providers
- Provider cards vertical (OpenAI, Anthropic, Custom)
- Fields: Base URL, Model Name, API Key (password)
- Buttons: Save (primary), Reset (secondary), Test (ghost)
- Status: green check / red X / gray dash
- API key masked, eye toggle | Save disabled until valid
- Unsaved: yellow dot plus confirm dialog

---

## 9. Theming

- Default: Dark | Light available | Toggle in top bar | Persisted in SQLite | System follow option

---

## 10. Accessibility

- Tab focusable | Focus ring 2px #6366f1 | Color never sole indicator
- Screen reader labels | Keyboard shortcuts in Help | DPI aware

---

*Design source of truth. All UI must follow these standards.*
