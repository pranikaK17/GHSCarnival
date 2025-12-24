from __future__ import annotations

from typing import Any

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from app.db.prisma import prisma

router = APIRouter(prefix="/admin", tags=["admin"])


class UpsertMatchBody(BaseModel):
    sportSlug: str
    teamA: str
    teamB: str
    status: str = "UPCOMING"
    startTime: str | None = None
    venue: str | None = None
    score: dict[str, Any] | None = None


@router.post("/matches")
async def create_match(body: UpsertMatchBody) -> dict:
    sport = await prisma.sport.find_unique(where={"slug": body.sportSlug})
    if sport is None:
        raise HTTPException(status_code=404, detail="Sport not found")

    match = await prisma.match.create(
        data={
            "sportId": sport.id,
            "teamA": body.teamA,
            "teamB": body.teamB,
            "status": body.status,
            "venue": body.venue,
            "score": body.score,
        }
    )
    return {"item": match}
