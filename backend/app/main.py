import os
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from sqlalchemy.exc import IntegrityError
from fastapi.middleware.cors import CORSMiddleware
from app.routers import atms, branches, auth, service_calls
from app.config import settings

FRONTEND_ORIGIN = settings.frontend_origin

app = FastAPI(
    title="Cashcow ATM tracker",
    description="ATM Management for CashCow Project",
    version="0.2.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[FRONTEND_ORIGIN],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

