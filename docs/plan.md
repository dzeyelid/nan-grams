# Project Plan: nan-grams

## Vision
- Build a static ingredient reference that shows the gram equivalents of Japanese tablespoons and teaspoons.
- Start as a GitHub Pages hosted Astro site and leave clear extension points for community-contributed ingredients, moderation, and social feedback.

## Tech Stack
- **Frontend**: Astro (latest) with the standard starter template generated via CLI.
- **Styling**: Astro official Tailwind integration plus the default component patterns offered by the starter layout.
- **Tooling**: Prefer CLI commands for framework operations and package management (npm create astro@latest, astro add tailwind, npm run lint/build, etc.).
- **Future Backend**: Azure Functions (HTTP APIs) with Cosmos DB for ingredient submissions and reactions.
- **Moderation**: Azure OpenAI for safety checks before accepting new ingredients.
- **Automation**: GitHub Pages for initial deployments; later, GitHub Actions workflows inspired by `azure-samples` repositories for Azure Static Web Apps + Functions pipelines.

## Implementation Phases

### Phase 1: Static Site (current milestone)
1. `npm create astro@latest` (in repo root) → choose the standard minimal template, enable TypeScript.
2. Configure `astro.config.mjs` for static output and GitHub Pages (`output: "static"`, `build: { client: "..." }` as needed, set `base` when publishing under project pages).
3. `npx astro add tailwind` → accept defaults, ensure global stylesheet and PostCSS config are generated.
4. Define shared layout (`src/layouts/Base.astro`) with header, footer, and Tailwind-powered styling.
5. Model ingredient data:
   - `src/types/ingredient.ts` with id, name, gramPerTablespoon, gramPerTeaspoon, tags, notes placeholder.
   - `src/data/ingredients.ts` seed array with sample entries and meaningful tags.
   - `src/lib/useIngredients.ts` expose filter/find helpers and precomputed conversions.
6. Implement `src/pages/index.astro` with ingredient selector UI, gram results, and placeholders for likes/report/submission buttons (disabled for now).
7. Add documentation in `README.md` for local setup, CLI commands (`npm install`, `npm run dev`, `npm run build`, `npm run preview`).
8. Configure GitHub Pages deployment settings (e.g., add `.github/workflows/gh-pages.yml` once ready, using official Astro Pages action or GitHub Pages action).

### Phase 2: Community Submission Foundations (post-launch)
1. Design submission form component (modal or dedicated page) and wire to dummy handlers to clarify UX.
2. Document submission validation flow (client side hints + server side moderation).
3. Draft API contract for Azure Functions (create/list ingredients, react with likes, report content).
4. Outline moderation pipeline calling Azure OpenAI for harmful-content screening and verifying measurement plausibility.
5. Prepare Cosmos DB schema: partition by ingredient id, store metadata, aggregated likes, reports, audit timestamps.

### Phase 3: Azure Integration & Automation (future)
1. Scaffold Azure Functions app (JavaScript/TypeScript) via CLI, expose endpoints consumed by the Astro client.
2. Connect Functions to Cosmos DB; implement CRUD and moderation queue.
3. Integrate Azure OpenAI moderation step into submission API.
4. Transition hosting to Azure Static Web Apps if needed, while keeping GitHub Pages config for fallback/minimal builds.
5. Author GitHub Actions workflow(s) referencing samples under `https://github.com/azure-samples` for building Astro, deploying Functions, and managing infrastructure as code.

## Data & Tagging Strategy
- Tags: start with practical descriptors (e.g., `"liquid"`, `"powder"`, `"sugar"`, `"oil"`).
- Ensure utility functions can filter by tags to support future category views.
- Keep seed data small but representative, ready for expansion via Cosmos DB.

## Research To-Do
- Use Microsoft Learn MCP Server to gather official guidance on Azure Static Web Apps with Functions/Cosmos DB.
- Use GitHub MCP Server and Microsoft Learn MCP Server and discover `azure-samples` repositories that show GitHub Actions pipelines for Astro/Azure deployments.

## GitHub Copilot Coding Agent Prompt (for GitHub.com)
```
Repository: dzeyelid/nan-grams
Task: Implement Phase 1 of docs/plan.md. Use CLI steps described (npm create astro@latest, astro add tailwind). Create the Astro project, seed ingredient data, and wire the index page per the plan. Do not delete existing files. Commit changes with clear messages when logical milestones are reached.
```