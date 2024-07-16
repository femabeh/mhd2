from fastapi import APIRouter
from fastapi.responses import JSONResponse
from config.project import config

router = APIRouter(
    tags=["ROOT"]
)


@router.get("/")
def root():
    return JSONResponse(content={"project": config["project_name"], "version": config["version"]})
