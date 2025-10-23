# syntax=docker/dockerfile:1.7
FROM node:20-alpine
ENV NODE_ENV=production \
    PORT=5000
WORKDIR /app
COPY package*.json ./
RUN npm ci --omit=dev
COPY . .
USER node
HEALTHCHECK --interval=10s --timeout=2s --retries=3 \
  CMD wget -qO- http://127.0.0.1:${PORT}/api/health || exit 1

EXPOSE 5000
CMD ["npm", "start"]
