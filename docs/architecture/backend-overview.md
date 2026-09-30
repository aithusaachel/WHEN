# WHEN Backend Architecture Overview

## A. CURRENT STATE
- **Infrastructure:** Empty FastAPI structure with initialized subdirectories (`app/api`, `app/core`, `app/models`, etc.). No actual code exists yet.
- **Tools:** Git repository initialized and pushed. Virtual environment exists.
- **Documentation:** Initial planning structure created. 
- **Code:** All python files (`main.py`, `__init__.py`) are currently empty (0 bytes).

## B. TARGET ARCHITECTURE
The backend follows a layered architecture optimized for separation of concerns and clear ownership:

Mobile App
     │
     ▼
Middleware (Cross-cutting processing)
     │
     ▼
API Routes (Entry points, HTTP logic)
     │
     ▼
Schemas (Pydantic validation, serializing)
     │
     ▼
Services (Business logic, orchestration)
     │
     ▼
Repositories (Data access layer abstraction)
     │
     ▼
Models / ORM (SQLAlchemy, Database structure)
     │
     ▼
PostgreSQL

## C. GAP ANALYSIS
Missing components to reach the target architecture:
- Project dependencies (`requirements.txt` / environment setup)
- Application initialization (`main.py` and FastAPI app instance)
- Configuration management (`core/config.py`)
- Database connection lifecycle (`db/session.py`)
- SQLAlchemy Base model (`db/base.py`)
- Alembic for migrations (`alembic/`)
- User persistence layer (Models, Repositories)
- User application layer (Services, Schemas, Routes)
- Authentication and Security logic (`core/security.py`)
- Error handling strategies and Middleware
- Automated Tests (`tests/`)

## D. IMPLEMENTATION ROADMAP
1. **Backend project foundation** (Setup, Config, `main.py`)
2. **Database foundation** (Session, Base model, Alembic setup)
3. **First vertical slice: User registration** 
   - Gabriel: User model, User repository, Migration
   - Michael: User schema, User service, User route
   - Together: Integration, debugging, e2e check
4. **Authentication** (Security primitives, Token generation, Auth routes)
5. **Core product features** (TBD based on When features: Events, Friends, etc.)
6. **Testing integration** (Unit/Integration testing structure)
7. **Security hardening & Error handling**

## E. MICHAEL'S WORKSTREAM (APPLICATION/API)
**Owner of:**
- `app/main.py`
- `app/api/routes/`
- `app/schemas/`
- `app/services/`
- `app/middleware/`

**Responsibilities:**
- HTTP semantics, routing, validation, application logic, and cross-cutting HTTP middleware.

## F. GABRIEL'S WORKSTREAM (DATA/INFRASTRUCTURE)
**Owner of:**
- `app/core/`
- `app/db/`
- `app/models/`
- `app/repositories/`
- `alembic/`
- `tests/`

**Responsibilities:**
- Configuration, database schema, queries, migrations, security primitives, and testing infrastructure.

## G. SHARED WORK
- Overall architecture definitions and API contracts.
- Database ↔ API integration.
- Authentication flow design.
- Error-handling strategy.
- Code review and Cross-training.

## H. INTEGRATION POINTS
- **Service → Repository:** Where Michael's business logic consumes Gabriel's data access layer.
- **Route → Schema → Service:** Michael's internal data flow mapping HTTP requests to internal actions.
- **Config → App:** Gabriel's configuration loading into Michael's `main.py`.

## I. LEARNING ATTACHED TO EACH WORKSTREAM
- **Michael:** FastAPI, Pydantic, Dependency Injection, REST APIs, Service-layer pattern.
- **Gabriel:** SQLAlchemy, Alembic, PostgreSQL, Repository pattern, Pytest.
- **Both:** Request/Response lifecycle from HTTP to Database and back.

## J. DOCUMENTATION PLAN
- `docs/architecture/`: For design decisions, API contracts, and layer overviews.
- `docs/learning/`: For tracking the team's conceptual progress and work assignments.
- *Rule:* Only create documentation about *our specific implementation*, not generic tutorials.
