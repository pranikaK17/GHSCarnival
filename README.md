# GHS Carnival – Official Sports Fest Website

## Overview
GHS Carnival is the annual college sports fest featuring multiple sports competitions between hostel blocks. This website serves as the central digital platform for live scores, schedules, team information, and official updates. Scores are updated manually through a secure admin panel by designated sport coordinators.

This repo is scaffolded as:
- `frontend/`: React (Vite) + TailwindCSS (no UI implemented)
- `backend/`: FastAPI + Prisma Client Python
- Database: Supabase Postgres (via `DATABASE_URL`)

---

## Objectives
- Display accurate live scores for all sports
- Allow manual score updates by authorized admins
- Centralize all fest-related information
- Provide a mobile-first, easy-to-use interface
- Support simultaneous updates for multiple sports

---

## Website Structure

### Public Website
- Landing Page
- Live Scores
  - Box Cricket
  - Football / Futsal
  - Basketball
  - Volleyball
  - Table Tennis
  - Other Sports
- Teams & Organising Committee
- Hostel Blocks & Captains
- About Us
- Guidelines / Rulebook

### Admin System (Restricted)
- Admin Login
- Sport-wise Score Update Panels
- Match & Schedule Management
- Announcements & Links Management
- Admin Activity Logs

---

## 1. Landing Page
**Purpose:** Entry point and overview of the fest

**Contents:**
- Fest branding, dates, and tagline
- Navigation menu
- Live match highlights
- Announcements
- Sports quick-access icons
- Footer with social links and contact info

---

## 2. Live Scores (Public)

### Purpose
Display real-time match information (read-only).

### Sports Selector
- Horizontal scrollable sports list
- Active sport highlighted

### Sport Live Score View
**Now Playing Section:**
- Teams playing
- Live indicator
- Score details (sport-specific)
- Match status

**Up Next Section:**
- Upcoming matches
- Date and time
- Venue (optional)

**Quick Links:**
- Official Instagram page
- Guidelines / Rulebook
- Cultural events updates

### Sport-Specific Score Data
- Box Cricket: Runs, wickets, balls, innings
- Football/Futsal: Goals, time, half
- Basketball: Score, quarter
- Volleyball: Sets, points
- Table Tennis: Sets, points

---

## 3. Teams & Organising Committee
**Purpose:** Display the people behind the fest

**Contents:**
- Core committee members
- Sub-committees
- Names, roles, photos, contact (optional)

---

## 4. Hostel Blocks & Captains
**Purpose:** Show participating hostel blocks and leadership

**Contents:**
- Block name
- Block captain name and photo
- Sports participation details
- Optional vice-captain information

---

## 5. About Us
**Purpose:** Describe the fest and its vision

**Contents:**
- History of GHS Carnival
- Vision and mission
- Values and sportsmanship
- Participation scale

---

## 6. Guidelines / Rulebook
**Purpose:** Provide official rules and regulations

**Contents:**
- General rules
- Sport-specific rules
- Match formats and scoring
- Code of conduct
- Disqualification policies
- Downloadable rulebook

---

## 7. Admin Panel

### Purpose
Allow authorized individuals to manually update scores and manage match data.

### Roles
- Super Admin: Full access to all sports, users, and content
- Sport Admin: Access limited to assigned sport

### Admin Login
- Secure authentication
- Role-based access control

### Admin Dashboard
- Assigned sport overview
- Ongoing and upcoming matches
- Match control actions

### Sport-wise Score Update
**Inputs (varies by sport):**
- Team names
- Score fields
- Time / balls / sets
- Match status (Live / Completed / Upcoming)

**Controls:**
- Increment/decrement score
- Manual correction fields
- Save/update actions
- Start/end match controls

### Live Sync
- Updates reflected instantly on public pages
- No public write access

### Safety & Validation
- Confirmation prompts
- Input validation
- Update logs with timestamps
- Rollback for recent updates

---

## 8. Announcements & Links Management
- Update social media links
- Update guideline links
- Push announcements to landing page

---

## Technical Considerations

### Frontend
- React (Vite) + TailwindCSS
- Pages are placeholder route shells only (your designs can be wired in)

### Backend
- FastAPI HTTP API
- Prisma schema + generated Prisma client for Python

### Database Entities
- Users (Admins)
- Sports
- Matches
- Scores
- Announcements

---

## Security
- Role-based permissions
- Secure admin authentication
- No public data modification
- Admin activity logging

---

## Future Enhancements
- Player statistics
- Match commentary
- Push notifications
- Progressive Web App support
- Admin mobile-optimized interface

---

## Local Development (Windows)

### 0) Prereqs
- Node.js 18+ (for Vite + Prisma CLI)
- Python 3.10+

### 1) Configure environment variables

Create `backend/.env` from `backend/.env.example` and set:
- `DATABASE_URL` to your Supabase Postgres connection string
- `CORS_ORIGINS` to include `http://localhost:5173`

Optionally also set `frontend/.env` with:
- `VITE_API_BASE_URL=http://127.0.0.1:8000`

### 2) Backend: install deps

```powershell
cd backend
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -U pip
pip install -r requirements.txt
```

### 3) Backend: Prisma generate + migrate

Prisma uses the schema at `backend/prisma/schema.prisma`.

```powershell
cd backend
prisma generate
# creates migrations and applies them (dev workflow)
prisma migrate dev
```

### 4) Run backend

```powershell
cd backend
.\.venv\Scripts\Activate.ps1
uvicorn app.main:app --reload --host 127.0.0.1 --port 8000
```

If you prefer running from `backend/app`:

```powershell
cd backend\app
..\venv\Scripts\Activate.ps1
uvicorn main:app --reload --host 127.0.0.1 --port 8000
```

Health check: `GET http://127.0.0.1:8000/health`

### 5) Frontend: install + run

```powershell
cd frontend
npm install
npm run dev
```

Frontend routes (placeholders only):
- `/` landing
- `/live-scores`
- `/teams`
- `/hostel-blocks`
- `/about`
- `/guidelines`
- `/admin/login`
- `/admin`

---

## Notes
- No UI has been implemented; only page shells and routing are provided.
- Authentication/role enforcement is not implemented yet; admin endpoints are placeholders.
