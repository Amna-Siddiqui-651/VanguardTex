<p align="left">
  <img src="https://unsplash.com" width="100%" alt="VanguardTex Banner" />
</p>

# VanguardTex

An enterprise-grade industrial simulation platform and gamified engine built using Python 3.13, FastAPI, and SQLAlchemy. This project bridges the foundational principles of **Textile Sciences (1st Semester, NED University)** with high-performance Industry 4.0 backend workflows.

The system extracts real-time mechanical telemetry from factory floors, processes data streams through a deterministic Lab Logic Engine, and securely tracks financial transactions inside an active user accounting database.

---

## 🔥 Key Technical Elements

*   **Industrial Telemetry Execution:** Simulates variable physics data sensors for `Spinning-Frame-01` (Yarn Count/Ne), `Weaving-Loom-X` (Picks Per Inch Density), and `Dyeing-Jet-Alpha` (Chemistry pH fluids testing & temperature metrics).
*   **The Lab Logic Engine (Phase 6):** Runs isolated data verification sequences via the `/simulation/analyze-quality` endpoint to automatically grade output batches into **Grade A (Export Ready)** or **Grade B (Local Market)** based on strict tolerance bounds.
*   **Factory Gamification Economy:** Processes real-time ledger updates where each production run triggers a `-Rs. 1,000` operational cost while generating points to compute immediate level ups.
*   **Cryptographic Access Gateway:** Implements a token-based secure authorization network backed by native `bcrypt` password encryption routines and direct Swagger UI Form-Login support.

---

## 🗺️ Project Architecture & Status

*   **Phase 1:** Professional Workspace, Virtual Env, & Core Packages Installation ➔ **[COMPLETE ✅]**
*   **Phase 2:** Database Structural Mapping & Relational ORM Models Definition ➔ **[COMPLETE ✅]**
*   **Phase 3:** Industrial Access Management & JWT Security Protocols Integration ➔ **[COMPLETE ✅]**
*   **Phase 4:** Textile Production Telemetry Automation & Crash Fallback Logic ➔ **[COMPLETE ✅]**
*   **Phase 5:** Operating Cost Accounting Ledger & Level Shifting Curves ➔ **[COMPLETE ✅]**
*   **Phase 6:** Predictive Quality Analyzer & Parameter Diagnostics Framework ➔ **[COMPLETE ✅]**
*   **Phase 7:** AI/ML Quality Intelligence Integration via Neural Networks ➔ *[Next Semester Target 🔮]*

---

## ⚙️ Core Technology Stack

*   `fastapi` & `uvicorn` — Driving high-speed RESTful application architectures and server execution.
*   `sqlalchemy` — Object-Relational Mapper handling state updates without programmatic SQL scripts.
*   `pydantic` & `email-validator` — Executing raw data validation, field filtering, and input syntax parsing.
*   `bcrypt` & `pyjwt` — Encoding sensitive records and generating secure verification token keys.
*   `random` — Managing data variations and generating synthetic physical sensor metrics.

---

## 💻 Local Workspace Installation

```powershell
# 1. Access codebase directory
git clone https://github.com
cd VanguardTex

# 2. Trigger environment runtime wrapper (Windows PowerShell)
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
venv\Scripts\Activate.ps1

# 3. Fire up the backend engine
python -m uvicorn app.main:app --reload
```

Interactive REST Testing API documentation endpoint will become live at:  
👉 **[http://127.0.0](http://127.0.0)**

---
Developed by **Amna Khurram** | Student of Textile Sciences, NED University of Engineering and Technology, Karachi 🏛️
