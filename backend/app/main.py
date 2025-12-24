from __future__ import annotations

import os
import sys
from pathlib import Path

from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

if __package__ is None or __package__ == "":
    backend_root = Path(__file__).resolve().parents[1]
    sys.path.insert(0, str(backend_root))

from app.api.main import api_router  # noqa: E402
from app.db.prisma import connect_prisma, disconnect_prisma  # noqa: E402

load_dotenv()

app = FastAPI(title="GHS Carnival API")

cors_origins = [o.strip() for o in os.getenv("CORS_ORIGINS", "").split(",") if o.strip()]
if cors_origins:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=cors_origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )


@app.on_event("startup")
async def on_startup() -> None:
    await connect_prisma()


@app.on_event("shutdown")
async def on_shutdown() -> None:
    await disconnect_prisma()


app.include_router(api_router)
