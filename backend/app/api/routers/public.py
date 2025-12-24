from __future__ import annotations

from fastapi import APIRouter

from app.db.prisma import prisma

router = APIRouter(prefix="/public", tags=["public"])


@router.get("/sports")
async def list_sports() -> dict:
    # Placeholder: returns empty list until DB is seeded
    sports = await prisma.sport.find_many(order={"name": "asc"})
    return {"items": sports}


@router.get("/matches")
async def list_matches() -> dict:
    matches = await prisma.match.find_many(order={"updatedAt": "desc"}, take=50)
    return {"items": matches}


@router.get("/announcements")
async def list_announcements() -> dict:
    items = await prisma.announcement.find_many(order={"updatedAt": "desc"}, take=20)
    return {"items": items}
