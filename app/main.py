from fastapi import FastAPI, status
from fastapi.responses import JSONResponse
from main_model import *


app = FastAPI(
    title="project-baselines/python-devcontainer-fastapi",
    version="0.1.0",
    responses={
        status.HTTP_404_NOT_FOUND: {"description": "The item was not found"},
        status.HTTP_422_UNPROCESSABLE_ENTITY: {"description": "Invalid ID supplied"},
        status.HTTP_200_OK: {"description": "Item requested by ID"},
    },
)


@app.post(
    path="/items",
    tags=["items"],
    description="Get item by ID",
    response_model=ItemsResponseModel,
)
async def read_item(body: ItemsRequestModel) -> ItemsResponseModel:
    if body.id == "foo":
        return {"value": "bar"}
    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND, content={"message": "Item not found"}
    )
