from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from app.services.gemini_service import generate_planner_recommendation


router = APIRouter()


class PlannerRequest(BaseModel):
    details: str
    budget: float = 0
    guests: int = 0
    occasion: str = ""


@router.post("/generate-home")
async def generate_home(request: PlannerRequest):

    try:

        result = await generate_planner_recommendation(
            planner="Home Planner",
            details=request.details,
            budget=request.budget
        )

        return {
            "planner": "Home Planner",
            "recommendation": result
        }

    except Exception as e:

        print("GEMINI ERROR:", repr(e))

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )


@router.post("/generate-party")
async def generate_party(request: PlannerRequest):

    try:

        details = f"""
Party requirements:
{request.details}

Number of guests:
{request.guests}

Occasion:
{request.occasion}
"""

        result = await generate_planner_recommendation(
            planner="Party Planner",
            details=details,
            budget=request.budget
        )

        return {
            "planner": "Party Planner",
            "recommendation": result
        }

    except Exception as e:

        print("GEMINI ERROR:", repr(e))

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )


@router.post("/generate-jewelry")
async def generate_jewelry(request: PlannerRequest):

    try:

        details = f"""
Jewelry requirements:
{request.details}

Occasion:
{request.occasion}
"""

        result = await generate_planner_recommendation(
            planner="Jewelry Planner",
            details=details,
            budget=request.budget
        )

        return {
            "planner": "Jewelry Planner",
            "recommendation": result
        }

    except Exception as e:

        print("GEMINI ERROR:", repr(e))

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )