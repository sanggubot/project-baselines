from fastapi import FastAPI, status
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field

app = FastAPI(
    title="project-baselines/python-devcontainer-fastapi",
    version="0.1.0",
)

responses = {
    status.HTTP_404_NOT_FOUND: {"description": "The item was not found"},
    status.HTTP_422_UNPROCESSABLE_ENTITY: {"description": "Invalid ID supplied"},
    status.HTTP_200_OK: {"description": "Item requested by ID"},
}


class RequestModel(BaseModel):
    id: str = Field(title="id of item", description="id of item")

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "id": "foo",
                },
                {
                    "id": "foo2",
                },
            ]
        }
    }


class ResponseModel(BaseModel):
    value: str = Field(title="value of item", description="value of item")

    class Config:
        json_schema_extra = {
            "example": {
                "value": "bar",
            }
        }


@app.post(
    path="/items",
    tags=["items"],
    description="Get item by ID",
    response_model=ResponseModel,
    responses=responses,
)
async def read_item(body: RequestModel) -> ResponseModel:
    if body.id == "foo":
        return {"value": "bar"}
    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND, content={"message": "Item not found"}
    )
