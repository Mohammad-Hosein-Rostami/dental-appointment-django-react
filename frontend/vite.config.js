import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// https://vitejs.dev/config/
export default defineConfig({
  base: "/",
 plugins: [react()],
 preview: {
  port: 3000,
  strictPort: true,
 },
 server: {
  watch: {
    usePolling: true,
  },
  host: true, // needed for the Docker Container port mapping to work
  strictPort: true,
  port: 3000, // you can replace this port with any port
}
})
