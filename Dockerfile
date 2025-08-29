version: "3.8"
services:
  buyback-bot:
    build: .
    restart: unless-stopped
    env_file: .env
    volumes:
      - ./keys:/app/keys:ro
