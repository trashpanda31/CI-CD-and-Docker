FROM node:18-alpine

# hadolint ignore=DL3018
RUN apk add --no-cache curl ca-certificates

WORKDIR /app
COPY package*.json ./
RUN npm ci --only=production --no-audit --no-fund
COPY . .

ENV NODE_ENV=production
ENV PORT=4000
EXPOSE 4000

HEALTHCHECK --interval=30s --timeout=3s --start-period=10s --retries=3 \
  CMD curl -fsS http://127.0.0.1:4000/api/users || exit 1

CMD ["node", "./bin/www"]

LABEL org.opencontainers.image.title="lab04-server" \
      org.opencontainers.image.part-of="lab04" \
      org.opencontainers.image.component="server"
