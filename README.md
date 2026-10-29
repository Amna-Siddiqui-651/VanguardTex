# 🧵 VanguardTex
### Gamified Industrial Simulation & Quality Intelligence Platform
*Developed by a Textile Sciences Student at NED University*

VanguardTex is a modern, enterprise-grade backend simulation framework that bridges industrial textile engineering with gamified enterprise economies. Built using Python 3.13, FastAPI, and SQLAlchemy, the system simulates real-time sensor streams from a textile factory floor and processes them through a deterministic Lab Logic Engine to grade manufacturing output.

---

## 🚀 Project Overview & Key Features

*   **Industrial Telemetry Simulation:** Simulates real-time telemetry datasets from actual machines: `Spinning-Frame-01`, `Weaving-Loom-X`, and `Dyeing-Jet-Alpha`.
*   **The Lab Logic Engine (Phase 6):** Runs programmatic, deterministic checks on Yarn Count deviations, Mechanical Loom Efficiency, Pick Density (PPI), and fluid chemistry pH bounds.
*   **Gamified Factory Economy:** Integrates execution costs and business rewards directly into database tracking. Simulates financial workflows where Grade A production earns higher global market export valuation.
*   **Secure Access Management:** Equipped with an encrypted JWT Token Authorization workflow using native `bcrypt` routines, complete with direct Swagger UI login capability.

---

## ⚙️ Core Technical Stack & Modules Used

*   **`fastapi` & `uvicorn`** - High-performance web framework and ASGI server suite driving the API execution.
*   **`sqlalchemy` & `sqlite3`** - Object-Relational Mapper (ORM) powering programmatic queries against `vanguardtex.db`.
*   **`pydantic` & `email-validator`** - Data parsing validation wrappers enforcing runtime schema restrictions.
*   **`bcrypt` & `pyjwt`** - Cryptographic layer encoding user credentials and issuing cryptographically signed bearer tokens.
*   **`random`** - Native library utilized to model physical hardware metric variances.

---

## 🗺️ Project Lifecycle & Roadmap

- [x] **Phase 1: Professional Development Workspace Setup** - Environment setup and core installations.
- [x] **Phase 2: Database Structural Design (Models)** - Relational data models definition for Users and Factory Machines.
- [x] **Phase 3: Industrial Access Management** - Secure JWT Auth Engine integration.
- [x] **Phase 4: Textile Production Telemetry** - Dynamic real-time manufacturing telemetry simulations.
- [x] **Phase 5: Factory Gamification Economy** - Active accounting ledger processing (`-Rs. 1,000` per process run) and dynamic leveling curves.
- [x] **Phase 6: Predictive Quality Analyzer (The Lab Logic)** - Standalone grading interface (`/simulation/analyze-quality`) for dynamic Export Ready vs. Local Market routing.
- [ ] **Phase 7: AI/ML Quality Intelligence (Future Capstone Goal)** - Replacing conditional handlers with predictive Machine Learning classifiers.

---

## 💻 How to Run Locally

1. Clone this repository to your local directory:
   ```bash
   git clone https://github.com
   cd VanguardTex
   ```

2. Activate your Virtual Environment:
   ```powershell
   # Windows PowerShell Execution
   Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
   venv\Scripts\Activate.ps1
   ```

3. Initialize the FastAPI Uvicorn Development Server:
   ```powershell
   python -m uvicorn app.main:app --reload
   ```

4. Open your local browser to access the dynamic interactive documentation dashboard:
   ```text
   http://127.0.0
   ```
