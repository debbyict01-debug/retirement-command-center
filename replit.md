# Workspace

## Overview

pnpm workspace monorepo using TypeScript. Each package manages its own dependencies.

Current primary user-facing artifact:

- **退休進擊戰情室** (`artifacts/retirement-war-room`) — a mobile-first React/Vite data dashboard for tracking a Taiwanese retirement stock portfolio. It uses local browser storage for editable holdings/cash values and includes KPI cards, weak-position alerts, charts, table health checks, CSV export, PDF print export, and dark mode.
- The retirement dashboard supports CSV-style holdings editing (`名稱或代號,成本,股數`) and fetches live Taiwan stock prices through the shared API server at `/api/stock-prices` using Yahoo Finance data with a 5-minute in-memory cache. It includes a broad built-in mapping for common Taiwan stocks/ETFs and also accepts direct symbols such as `2330`, `0050`, or `6290.TWO`.
- The dashboard also includes a potential-stock radar powered by `/api/stock-analysis`. It fetches 3-month Yahoo Finance daily chart data, scores current holdings and candidate Taiwan stocks/ETFs using trend, momentum, pullback, and volatility heuristics, and presents ranked research candidates with a clear non-advice disclaimer.

## Stack

- **Monorepo tool**: pnpm workspaces
- **Node.js version**: 24
- **Package manager**: pnpm
- **TypeScript version**: 5.9
- **API framework**: Express 5
- **Database**: PostgreSQL + Drizzle ORM
- **Validation**: Zod (`zod/v4`), `drizzle-zod`
- **API codegen**: Orval (from OpenAPI spec)
- **Build**: esbuild (CJS bundle)
- **Frontend dashboard**: React + Vite + Tailwind + Recharts

## Key Commands

- `pnpm run typecheck` — full typecheck across all packages
- `pnpm run build` — typecheck + build all packages
- `pnpm --filter @workspace/api-spec run codegen` — regenerate API hooks and Zod schemas from OpenAPI spec
- `pnpm --filter @workspace/db run push` — push DB schema changes (dev only)
- `pnpm --filter @workspace/api-server run dev` — run API server locally

See the `pnpm-workspace` skill for workspace structure, TypeScript setup, and package details.
