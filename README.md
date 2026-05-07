# chatgpt2api Lite

A lightweight, Web-UI-free version of [chatgpt2api](https://github.com/TriTue2011/chatgpt2api) — an OpenAI-compatible proxy for the ChatGPT Web API.

## Features

- ✅ **No Web UI** — Minimal footprint, API-only
- ✅ **OpenAI-compatible endpoints** — `/v1/chat/completions`, `/v1/responses`, `/v1/models`, `/v1/images/generations`, `/v1/images/edits`, `/v1/messages`
- ✅ **Multi-account via environment variables** — `CHATGPT_TOKEN_1`, `CHATGPT_TOKEN_2`, etc.
- ✅ **HTTP 413 protection** — Automatic payload truncation prevents "Request Entity Too Large" errors
- ✅ **Home Assistant compatible** — Works with `hass_local_openai_llm`
- ✅ **Minimal Docker image** — Single-stage build, no Node.js/Next.js dependencies

## Quick Start

1. Clone the repo:
   ```bash
   git clone https://github.com/TriTue2011/chatgpt2apiLite.git
   cd chatgpt2apiLite
   ```

2. Edit `docker-compose.yml` and set your configuration:
   ```yaml
   environment:
     - CHATGPT2API_AUTH_KEY=sk-your-secret-key
     - CHATGPT_TOKEN_1=your_chatgpt_token_here
   ```

3. Build and run:
   ```bash
   docker compose up -d --build
   ```

4. The API is now available at `http://localhost:3030`

## Configuration

| Environment Variable | Required | Description |
|---------------------|----------|-------------|
| `CHATGPT2API_AUTH_KEY` | Yes | Authentication key for API access |
| `CHATGPT_TOKEN_1` | Yes | Your ChatGPT access token |
| `CHATGPT_TOKEN_2..N` | No | Additional tokens for multi-account |
| `STORAGE_BACKEND` | No | Storage backend: `json` (default), `sqlite`, `postgres`, `git` |
| `DATABASE_URL` | No | Database URL (for `sqlite`/`postgres` backends) |
| `GLOBAL_SYSTEM_PROMPT` | No | Custom system prompt for all conversations |

## API Endpoints

| Method | Path | Description |
|--------|------|-------------|
| `GET` | `/v1/models` | List available models |
| `POST` | `/v1/chat/completions` | Chat completion (OpenAI-compatible) |
| `POST` | `/v1/responses` | Responses API (OpenAI-compatible) |
| `POST` | `/v1/messages` | Messages API (Anthropic-compatible) |
| `POST` | `/v1/images/generations` | Generate images |
| `POST` | `/v1/images/edits` | Edit images |

## Credits

Based on [chatgpt2api](https://github.com/TriTue2011/chatgpt2api) by [TriTue2011](https://github.com/TriTue2011).
