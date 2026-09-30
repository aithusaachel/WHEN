# Team Work Plan

This document tracks the actual division of work between Michael (Application/API) and Gabriel (Data/Infrastructure).

---

## Phase 1: Backend Foundation

### Task: Implement Core Configuration
**Owner:** Gabriel
**Reviewer:** Michael
**Concepts required:** Environment variables, Pydantic BaseSettings, Configuration singletons.
**Files:** `app/core/config.py`, `.env`, `.env.example`
**Integration:** Configuration consumed by `main.py`.
**Status:** Not started

### Task: Implement FastAPI Application Entry Point
**Owner:** Michael
**Reviewer:** Gabriel
**Concepts required:** FastAPI instantiation, ASGI, Uvicorn, API Routers.
**Files:** `app/main.py`, `app/api/routes/__init__.py`
**Integration:** Instantiates the app using Gabriel's config.
**Status:** Not started

---

## Phase 2: Database Foundation

### Task: Implement Database Session and Base Model
**Owner:** Gabriel
**Reviewer:** Michael
**Concepts required:** SQLAlchemy engines, sessionmakers, declarative base.
**Files:** `app/db/session.py`, `app/db/base.py`
**Integration:** Required for all future database operations.
**Status:** Not started

### Task: Configure Database Migrations (Alembic)
**Owner:** Gabriel
**Reviewer:** Michael
**Concepts required:** Database migrations, Alembic environment.
**Files:** `alembic/`, `alembic.ini`
**Integration:** Reads models from `base.py` to auto-generate migrations.
**Status:** Not started

---

## Phase 3: First Vertical Slice (User Registration)

*(To be filled out completely before we start Phase 3)*

### Task: Implement User Persistence
**Owner:** Gabriel
**Reviewer:** Michael
**Concepts required:** Relational databases, SQLAlchemy models, Repositories.
**Files:** `app/models/user.py`, `app/repositories/user_repository.py`, `alembic/versions/...`
**Status:** Not started

### Task: Implement User API and Business Logic
**Owner:** Michael
**Reviewer:** Gabriel
**Concepts required:** FastAPI routes, Pydantic schemas, Service layer logic.
**Files:** `app/api/routes/users.py`, `app/schemas/user.py`, `app/services/user_service.py`
**Status:** Not started
