import { defineConfig } from 'vite';
import { resolve } from 'path';
import handlebars from 'vite-plugin-handlebars';

export default defineConfig({
  root: './',
  plugins: [
    handlebars({
      partialDirectory: resolve(__dirname, 'partials'),
    }),
  ],
  build: {
    outDir: 'dist',
    rollupOptions: {
      input: {
        main: resolve(__dirname, 'index.html'),
        story: resolve(__dirname, 'story.html'),
        programs: resolve(__dirname, 'programs.html'),
        press: resolve(__dirname, 'press.html'),
        contact: resolve(__dirname, 'contact.html'),
        donate: resolve(__dirname, 'donate.html'),
        notfound: resolve(__dirname, '404.html'),
      },
    },
  },
  server: {
    port: 5173,
    open: true,
  },
});
