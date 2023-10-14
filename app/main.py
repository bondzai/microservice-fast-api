from fastapi.middleware.cors import CORSMiddleware
from fastapi import Depends, FastAPI

from .dependencies import get_query_token, get_token_header
from .routers import items, users, admin

app = FastAPI(dependencies=[Depends(get_query_token)])

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(users.router)
app.include_router(items.router)
app.include_router(
    admin.router,
    prefix="/admin",
    tags=["admin"],
    dependencies=[Depends(get_token_header)],
    responses={418: {"description": "I'm a teapot"}},
)

@app.get("/")
async def root():
    return {"message": "Ok"}
