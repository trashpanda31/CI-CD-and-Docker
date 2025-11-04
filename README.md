# 🐳 Docker & CI/CD Labs

Welcome to the collection of **Docker** and **CI/CD** labs.  
A repository of five projects demonstrating Docker + CI/CD in practice. 
It starts with a static site under Nginx; then moves to services on Node/Express and FastAPI; then a client + API pair behind Nginx; and ends with a small stack (Postgres + API + frontend). Along the way: lean images, pinned base images, health probes, per-lab PR pipelines, and a simple promotion flow (PR > master > registry) with the tags `latest` and `<short-sha>`.

## ✨ Quick links
*  **Docker Hub:** [trashpanda31](https://hub.docker.com/u/trashpanda31) — published images.
*  **Pipelines:** [.github/workflows](.github/workflows)
*  **Pull Requests:** [PR tab](../../pulls) — open and closed change requests.
*  **CI/CD runs:** [Actions tab](../../actions) — latest per-lab CI and `CD_to_Registry` runs.
*  **Code structure:** `lab01…lab05` + Dockerfiles/Compose in their respective folders.

## 🔥 Two key pipelines

### **1) Pipeline for Pipelines (PR)**
* **Trigger:** `pull_request` for changes in `.github/workflows/**`.
* **Purpose:** checks the **quality of the workflows themselves**.
* **Result:** the PR won’t pass until the workflow files comply with the rules.

### **2) CD to Registry**
* **Trigger:** `push` to `master`.
* **Purpose:** detects changed `labXX`, builds images, and **pushes to the registry**. 
* **Tags:** `labXX:latest` + `labXX:<short-sha>`

_In short:_  
* PR > **CI** (lint + build + test)   `>>>`   master > **CD** (detect + build + push) 

##  💥 Per-lab details

### Lab 01 — Nginx static site
- Focus: minimal containerized static hosting with an HTTP health check.
- Dockerfile: `lab01/Dockerfile`
- Pipeline: `.github/workflows/lab01_pipe.yml` — PR: hadolint > buildx build > save artifact > smoke HTTP.

### Lab 02 — Node/Express (multi-stage, cache)
- Focus: reproducible multi-stage build with dependency caching.
- Dockerfile: `lab02/Dockerfile`
- Pipeline: `.github/workflows/lab02_ci_pipe.yml` — PR: hadolint > npm ci/lint/test > build > save artifact > HTTP probe.

### Lab 03 — FastAPI service (runtime image)
- Focus: slim Python runtime and non-root execution.
- Dockerfile: `lab03/Dockerfile`
- Pipeline: `.github/workflows/lab03_ci_pipe.yml` — PR: hadolint > Ruff lint > build > save artifact > HTTP probe.

### Lab 04 — React client + Node API under Compose
- Focus: two images (API + client) with Nginx reverse proxy; prod Compose.
- Docker: `lab04/src/server/Dockerfile`, `lab04/src/client/Dockerfile`, 
- Compose: `lab04/src/docker-compose.prod.yml`
- Pipelines:  
  - Server: `.github/workflows/lab04_server_ci_pipe.yml` — PR: hadolint > build > save artifact > run & probe.  
  - Client: `.github/workflows/lab04_client_ci_pipe.yml` — PR: hadolint > build > save artifact > run & wait > show rendered nginx config.

### Lab 05 — Postgres + API + frontend behind Nginx (dev/prod)
- Focus: small near-production stack with separate dev/prod Compose.
- Docker: `lab05/backend/Dockerfile`, `lab05/frontend/Dockerfile`,
- Compose: `lab05/docker-compose.dev.yml`, `lab05/docker-compose.prod.yml`
- Pipelines:  
  - Backend: `.github/workflows/lab05_server_ci.yml` — PR: hadolint > build > save artifact > start temp Postgres > run & probe > cleanup.  
  - Frontend: `.github/workflows/lab05_client_ci.yml` — PR: hadolint > build > save & upload image artifact.

## 📌 Summary

- **End-to-end delivery:** Every lab has its own PR CI; a push to `master` runs **CD to Registry** with `latest` and `<short-sha>` tags. I practiced selective builds (only changed `labXX`) to keep pipelines fast.
- **Image craftsmanship:** Multi-stage builds, cache-aware installs, **slim** bases, deterministic tags, and non-root runtimes smaller, reproducible images ready for CI smoke runs.
- **Health & readiness:** Consistent HTTP health probes; in CI I spin up containers and verify endpoints before publishing.
- **Workflow hygiene:** A dedicated **pipeline-for-pipelines** validates workflows (YAML/lint, pinned `uses`, safe triggers, minimal `permissions`) so unsafe or sloppy CI doesn’t reach `master`.
- **Artifacts over flakes:** Built images are saved as CI artifacts for repeatable smoke tests and quick triage without re-building.
- **Operational clarity:** Simple, predictable tagging and a clear promotion path (PR checks > main > registry) make it obvious what’s running and where it came from.


