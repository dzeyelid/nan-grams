# nan-grams
いろんな素材の大さじ、小さじが何グラムかを表示するアプリ

A static ingredient reference that shows the gram equivalents of Japanese tablespoons (大さじ) and teaspoons (小さじ).

## Features

- 📊 Instant conversion from tablespoons/teaspoons to grams
- 🏷️ Tagged ingredients (liquid, powder, seasoning, etc.)
- 📱 Responsive design with Tailwind CSS
- 🚀 Built with Astro for fast static site generation

## Local Setup

### Prerequisites

- Node.js (version 18 or higher)
- npm

### Installation

```bash
# Clone the repository
git clone https://github.com/dzeyelid/nan-grams.git
cd nan-grams

# Install dependencies
npm install
```

### Development

```bash
# Start the development server
npm run dev
# The site will be available at http://localhost:4321/ (or another port if 4321 is in use)

# Build for production
npm run build

# Preview the production build
npm run preview
```

## Project Structure

```
/
├── public/           # Static assets (favicon, etc.)
├── src/
│   ├── data/        # Ingredient seed data
│   ├── layouts/     # Astro layouts
│   ├── lib/         # Utility functions
│   ├── pages/       # Astro pages
│   └── types/       # TypeScript type definitions
├── astro.config.mjs # Astro configuration
├── tailwind.config.mjs # Tailwind CSS configuration
└── package.json
```

## Available Scripts

- `npm run dev` - Start development server
- `npm run build` - Build for production (includes type checking)
- `npm run preview` - Preview the production build locally
- `npm run astro` - Run Astro CLI commands

## Future Plans

See [docs/plan.md](docs/plan.md) for the complete project roadmap, including:

- Community ingredient submissions
- Like and report functionality  
- Azure Functions + Cosmos DB integration
- Azure OpenAI moderation
- GitHub Actions deployment pipelines

## Tech Stack

- **Framework**: [Astro](https://astro.build/) v5
- **Styling**: [Tailwind CSS](https://tailwindcss.com/)
- **Language**: TypeScript (strict mode)
- **Deployment**: GitHub Pages (planned)

## License

See [LICENSE](LICENSE) file.

