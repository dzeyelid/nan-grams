import { defineConfig } from 'astro/config';
import tailwind from '@astrojs/tailwind';

// https://astro.build/config
export default defineConfig({
  output: 'static',
  integrations: [tailwind()],
  // Uncomment and set base when deploying to GitHub Pages under a project path
  // base: '/nan-grams',
});
